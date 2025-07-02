from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from prompts import NL_TO_SQL_PROMPT
import sqlite3
import os

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Define the state
class AgentState(TypedDict):
    user_query: str
    sql_query: Optional[str]
    raw_results: Optional[List]
    chart_path: Optional[str]
    error: Optional[str]

# Load schema
def get_schema():
    conn = sqlite3.connect('sample_data/sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table'")
    schema = "\n".join([row[0] for row in cursor.fetchall()])
    conn.close()
    return schema

# Node: Generate SQL
def generate_sql(state: AgentState):
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        schema = get_schema()
        prompt = NL_TO_SQL_PROMPT.invoke({
            "schema": schema,
            "query": state["user_query"]
        })
        response = llm.invoke(prompt.to_string())
        sql_query = response.content.strip()
        return {"sql_query": sql_query}
    except Exception as e:
        return {"error": f"Error generating SQL: {e}"}

# Node: Execute SQL
from db_utils import execute_query

def execute_sql(state: AgentState):
    if state.get("error"):
        return state
    try:
        conn = sqlite3.connect('sample_data/sample.db')
        cursor = conn.cursor()
        cursor.execute(state["sql_query"])
        results = cursor.fetchall()
        description = cursor.description  # This gives us column names
        conn.close()
        return {
            "raw_results": results,
            "cursor_description": description  # Save column names in state
        }
    except Exception as e:
        return {"error": f"SQL Execution Error: {e}"}

# Node: Generate Chart
from visualizer import generate_bar_chart

def generate_chart(state: AgentState):
    if state.get("error") or not state.get("raw_results"):
        return state
    try:
        # Try to generate a chart only if there are results
        headers = [desc[0] for desc in state.get("cursor_description", [])]
        data_for_chart = [headers] + state["raw_results"]
        chart_path = generate_bar_chart(data_for_chart)
        return {"chart_path": chart_path}
    except Exception as e:
        return {"chart_path": None}

# Build the graph
workflow = StateGraph(AgentState)

workflow.add_node("generate_sql", generate_sql)
workflow.add_node("execute_sql", execute_sql)
workflow.add_node("generate_chart", generate_chart)

workflow.set_entry_point("generate_sql")
workflow.add_edge("generate_sql", "execute_sql")
workflow.add_edge("execute_sql", "generate_chart")
workflow.add_edge("generate_chart", END)

app = workflow.compile()