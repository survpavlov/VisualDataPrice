import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from data import get_data_ticker

T = 0
L = []
N = []

app = dash.Dash(__name__)

opts = [{'label': 'ticker_' + f'{i:02}', 'value': i} for i in range(100)]

app.layout = html.Div(children = [
    dcc.Graph(
        id = 'price-graph',
        figure = {
            'layout': {
                'title': 'Data Price'
            }
        }
    ),
    
    dcc.Dropdown(
        id = 'ticker-dropdown',
        options = opts,
        value = 0,
        clearable = False,
        className = "dropdown",
    ),

    dcc.Interval(
        id = 'graph-update',
        interval = 1*1000,
        n_intervals = 0
    )
])

@app.callback(Output('price-graph', 'figure'),
              [Input('ticker-dropdown', 'value'),
               Input('graph-update', 'n_intervals')
              ]
)
def update_graph(value, n_intervals):
    global T, L, N
    if value != T:
      T = value
      L = []
      N = []
    m = get_data_ticker(T, len(N))
    L.extend(m)
    N.extend(range(len(N), len(N) + len(m)))
    fig = go.Figure(data = [go.Scatter(x = N, y = L)])
    return fig


if __name__ == "__main__":
    app.run_server(debug = True, host = '127.0.0.2')
