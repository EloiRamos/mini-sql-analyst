if __name__ == "__main__":
    from agent import app

    while True:
        user_query = input("\nEnter your question (type 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        result = app.invoke({"user_query": user_query})
        
        if result.get("error"):
            print("❌ Error:", result["error"])
        else:
            print("✅ SQL Query:\n", result["sql_query"])
            print("📊 Results:", result["raw_results"])
            if result["chart_path"]:
                print(f"📈 Chart saved at: {result['chart_path']}")