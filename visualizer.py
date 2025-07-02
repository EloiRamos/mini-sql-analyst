import os
import matplotlib.pyplot as plt
import pandas as pd

def generate_bar_chart(data, x_label="X", y_label="Y", title="Chart"):
    """Generates a bar chart from query result data."""
    try:
        if len(data) < 2:
            return None
        headers = data[0]
        df = pd.DataFrame(data[1:], columns=headers)
        if len(df.columns) < 2:
            return None
        plt.figure(figsize=(10, 5))
        df.plot(kind='bar', x=df.columns[0], y=df.columns[1], title=title)
        os.makedirs("output", exist_ok=True)
        chart_path = "output/chart.png"
        plt.savefig(chart_path)
        plt.close()
        return chart_path
    except Exception as e:
        print(f"Error generating chart: {e}")
        return None