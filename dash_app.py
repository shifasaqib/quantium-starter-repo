import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load cleaned data
df = pd.read_csv("formatted_output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Initialize app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

# Layout
app.layout = html.Div(className="main-container", children=[

    html.H1("Pink Morsel Sales Dashboard", className="title"),

    html.Div(className="radio-container", children=[
        html.Label("Filter by Region:", className="radio-label"),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            className="radio-items"
        ),
    ]),

    dcc.Graph(id="sales-line-chart")

])


# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    grouped_df = filtered_df.groupby("date")["Sales"].sum().reset_index()

    fig = px.line(
        grouped_df,
        x="date",
        y="Sales",
        title="Total Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f8f9fa",
        font=dict(size=14),
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)