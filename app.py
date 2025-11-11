import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# load data
df = pd.read_csv("formatted_output.csv")

# convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# create line chart
fig = px.line(df, x="date", y="Sales", title="Pink Morsel Sales Over Time")

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# build dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

