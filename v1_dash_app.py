import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import sqlite3
import datetime

# functions
def parse_row(row):
    '''
    Parse a results row from SQL query to the log database.
    '''
    dt, tk = row

    # format date
    frmt_dt = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')

    # pull number from ticker
    frmt_tk = float(tk.split(' ')[1].strip())

    return frmt_dt, frmt_tk

def get_data():
    '''
    Query the database and return lists of the data to plot.
    '''
    # set up database connection
    DB_NAME = "db.sqlite"
    conn = sqlite3.connect(DB_NAME)

    # get data from the db
    cur = conn.cursor()
    cur.execute('SELECT * FROM logs ORDER BY time ASC')
    res = cur.fetchall()

    # parse the results of the query
    _dt_data = []
    _tk_data = []

    for row in res:
        p_row = parse_row(row)
        _dt_data.append(p_row[0])
        _tk_data.append(p_row[1])

    return _dt_data, _tk_data



# create the dash app
app = dash.Dash()
server = app.server

# dash app layout
app.layout = html.Div(children = [
    dcc.Graph(id='test-graph',
    ),

    dcc.Interval(id='graph-refresh-interval',
     interval=5 * 1000,
     n_intervals=0,
     max_intervals=-1
     )
])


# dash dynamic functions
@app.callback(
    Output('test-graph', 'figure'),
    [Input('graph-refresh-interval', 'n_intervals')]
)
def update_test_graph(n):
    dt_data, tk_data = get_data()
    # put the data into a plotly graph object
    plot_data = [go.Scatter(x=dt_data, y=tk_data)]
    graph_data = {'data': plot_data}
    return graph_data


# run the dash app
app.run_server(debug=True)
