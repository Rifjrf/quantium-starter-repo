import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# load data
df = pd.read_csv("formatted_output.csv")

# convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# build dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

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
        labelStyle={"display": "inline-block", "margin-right": "15px"}
    ),

    dcc.Graph(id="sales-graph")
])


@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    fig = px.line(filtered, x="date", y="Sales", title="Pink Morsel Sales Over Time")
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
