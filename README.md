# 🧠 Mini-SQL Analyst

An AI-powered SQL analyst that converts natural language queries into SQL and visualizes results.

This project demonstrates how to build a smart agent using **LangChain**, **LangGraph**, and **OpenAI**, which understands English questions, translates them into SQL, runs them on a local SQLite database, and returns both raw data and charts.

---

## 🧩 Features

- ✅ Natural Language → SQL query conversion
- ✅ Execution on a local SQLite database
- ✅ Result visualization (bar charts)
- ✅ Streamlit-based web interface
- ✅ Modular code structure (`agent.py`, `db_utils.py`, `visualizer.py`)

---

## 🔧 Technologies Used

- [LangChain](https://python.langchain.com/) – For LLM integration
- [LangGraph](https://github.com/langchain-ai/langgraph) – For building the agent workflow
- [OpenAI](https://platform.openai.com/docs/models) – As the LLM backend
- [SQLite3](https://www.sqlite.org/index.html) – Lightweight local database
- [Streamlit](https://streamlit.io) – For the web UI
- [Pandas & Matplotlib](https://pandas.pydata.org/ & https://matplotlib.org/ ) – For data manipulation and charting

---

## 📦 Installation

Make sure you have Python 3.9+ installed.

1. Clone the repo:
   ```bash
   git clone https://github.com/EloiRamos/mini-sql-analyst.git
   cd mini-sql-analyst
   ```
