from langchain_core.prompts import PromptTemplate

NL_TO_SQL_PROMPT = PromptTemplate.from_template(
    """You are a helpful assistant acting as an SQL expert.
Given the following natural language query, generate a valid SQL query.
Only return the SQL query without any explanation.

Database Schema:
{schema}

Natural Language Query:
"{query}"

Generated SQL Query:
"""
)