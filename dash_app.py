import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Step 1: Load the processed CSV
df = pd.read_csv("formatted_output.csv")

# Step 2: Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Step 3: Sort by date
df = df.sort_values("date")

# Step 4: Create line chart
fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "Sales": "Total Sales"}
)

# Step 5: Set up Dash app layout
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Step 6: Run Dash
if __name__ == "__main__":
    app.run(debug=True)
