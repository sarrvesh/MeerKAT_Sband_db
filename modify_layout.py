import dash_html_components as html
import dash_bootstrap_components as dbc

header = html.Div(children=[
            html.H1('MeerKAT S-band survey: modify pointing information')
         ], style={'padding':'10px 10px'})

point_name = dbc.FormGroup([
                dbc.Label('Pointing name', width=1),
                dbc.Col(
                    dbc.Input(type='text', 
                                  id='pointname', 
                                  value=''),
                    width=1
                ),
                dbc.Col(
                    dbc.Button('Get info', id='query', color='dark'),
                    width=1
                )
            ], row=True)

coord = dbc.FormGroup([
                dbc.Label('Coordinates (J2000)', width=1),
                dbc.Col(
                    dbc.Input(type='text', id='coord', value=''),
                    width=1
                )
            ], row=True)

calib = dbc.FormGroup([
                dbc.Label('Calibrator name', width=1),
                dbc.Col(
                    dbc.Input(type='text', id='calib', value=''),
                    width=1
                )
            ], row=True)

obs_date = dbc.FormGroup([
                dbc.Label('Observational date', width=1),
                dbc.Col(
                    dbc.Input(type='text', id='obs_date', value=''),
                    width=1
                )
            ], row=True)

status = dbc.FormGroup([
                dbc.Label('Status', width=1),
                dbc.Col(
                    dbc.Input(type='text', id='status', value=''),
                    width=1
                )
            ], row=True)

submit = dbc.FormGroup([
                dbc.Label('', width=1),
                dbc.Col(
                    dbc.Button('Update pointing', id='update', color='dark'),
                    width=1
                )
            ], row=True)

form = html.Div([
            point_name,
            coord,
            calib,
            obs_date,
            status,
            submit
       ], style={'padding':'10px 10px'})

layout = html.Div([
            dbc.Row(dbc.Col(header)),
            form
            #dbc.Row(dbc.Col(data_table, width=5), justify="center")
         ])
