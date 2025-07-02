import streamlit as st
from agent import app

st.title("🧠 Mini-SQL Analyst")
st.markdown("Ask a question about your database!")

user_query = st.text_input("Enter your question:")
if st.button("Run"):
    result = app.invoke({"user_query": user_query})
    
    if result.get("error"):
        st.error(result["error"])
    else:
        st.subheader("Generated SQL:")
        st.code(result["sql_query"], language="sql")
        
        st.subheader("Results:")
        st.write(result["raw_results"])

        if result["chart_path"]:
            st.image(result["chart_path"])