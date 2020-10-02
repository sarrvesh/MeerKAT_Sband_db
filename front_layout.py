import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

###############################################################################
# Define the page header
###############################################################################
header = dbc.Row([
            html.H1('Welcome to the MeerKAT S-band survey website')
         ])

###############################################################################
# Define the individual cards
###############################################################################
card_style = {'height':'9rem'}
pub_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Publications"),
                    html.P("List of relevant publications")
                ]),
           ], color='secondary', style=card_style)

desc_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Description"),
                    html.P("Check out the technical aspects of the survey")
                ])
           ], color='secondary', style=card_style)

overview_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Survey status"),
                    html.P("Check out the current status of the survey")
                ])
           ], color='secondary', style=card_style)

modify_card = dbc.Card([
                #dbc.CardImg(src="", top=True),
                dbc.CardBody([
                    html.H2("Modify db"),
                    html.P("Modify details about individual pointings")
                ])
           ], color='secondary', style=card_style)

###############################################################################
# Define an empty row
###############################################################################
empty_space = dbc.Row([dbc.Label(' ')], style={'height':'5rem'})

###############################################################################
# Define a row of cards
###############################################################################
card_link_style = {'width':'18rem', 'color':'black'}
cards_row_1 = dbc.CardDeck([
                  dcc.Link(pub_card,      href="#",          style=card_link_style), 
                  dcc.Link(desc_card,     href="#",          style=card_link_style),
                  dcc.Link(overview_card, href="/overview/", style=card_link_style),
                  dcc.Link(modify_card,   href="/modify/",   style=card_link_style)
              ])

###############################################################################
# Define the page layout
###############################################################################
layout = html.Div(children=[
            dbc.Row([header], justify='center'),
            empty_space,
            dbc.Row([cards_row_1], justify='center')
            ], style={'padding':'10px 50px'})
