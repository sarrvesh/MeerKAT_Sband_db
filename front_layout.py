import dash_html_components as html
import dash_bootstrap_components as dbc

header = dbc.Row([
            html.H1('Welcome to the MeerKAT S-band survey website')
            ], justify='center'
         )

pub_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Publications"),
                    html.P("List of relevant publications"),
                    html.P("Link")
                ]),
           ], color='secondary')

desc_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Description"),
                    html.P("Check out the technical aspects of the survey"),
                    html.P("Link")
                ])
           ], color='secondary')

overview_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Survey status"),
                    html.P("Check out the current status of the survey"),
                    html.P("Link")
                ])
           ], color='secondary')

modify_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Modify db"),
                    html.P("Modify details about individual pointings"),
                    html.P("Link")
                ])
           ], color='secondary')

empty_space = dbc.Row([dbc.Label(' ')], style={'height':'5rem'})

cards_row_1 = dbc.CardDeck([
                  pub_card, desc_card, overview_card, modify_card
              ], style={"width":"60%"})

layout = html.Div(children=[
            dbc.Row([header], justify='center'),
            empty_space,
            dbc.Row([cards_row_1], justify='center')
            ], style={'padding':'10px 50px'})
