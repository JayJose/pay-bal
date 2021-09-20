import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.DARKLY]
dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash_app.server

dash_app.layout = dbc.Container(
    children=[
        dbc.Row([
            html.H2('UAB Payroll Explorer')
        ]),
    ]
)

if __name__ == '__main__':
    dash_app.run_server(debug=True)