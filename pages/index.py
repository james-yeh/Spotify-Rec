# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Do you need a song recommendation?
           

            Are you tired of listening the same songs and want to try something new?
            If you need some help on finding new songs to listen to, then let machine
            learning solve your problem. By using Spotify's data on each song we are
            able to predict similar songs based on many features of the songs, including
            popularity, loudness and danceability. So take a moment to expland the songs
            you listen to and find a new song you may like.

            """
        ),
        dcc.Link(dbc.Button('Recommend A Song', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
#        html.Img(src='assets/music_track.png', className='img-fluid')

    ]
)

layout = dbc.Row([column1, column2])