# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## The Build Process

            #### Spotify Data
            Spotfy created a Convolutional Neural Network they run the songs on their through to
            represent the songs in numerical values. These values try to represent how much
            energy a song may have, how loud a song may be or even try to predict the danceability
            of a song.

            #### Our Predictions
            Our app uses a Kaggle dataset that gathered a large number of Spotify songs and their information.
            Specifically it focuses on the information Spotify provides on each song and uses a Nearest Neighbor 
            machine learning algorithm to make a song recommendation. 


            """
        ),
        dcc.Markdown(""" 
        

        
        """
        ),



    ],
)

layout = dbc.Row([column1])