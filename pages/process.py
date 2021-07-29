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
            Spotify categorizes each song by rating different features numerically.  These ratings 
            represent different characteristics of the song.  Features include but are not limited to: 
            energy, key, loudness, valence, danceability.

            #### Our Predictions
            Our app uses a dataset from Kaggle containing information gathered from Spotify's API.  
            Using a nearest neighbor model, our app is able to make a recommendation by finding the 
            next best song based on euclidean distance from whatever inputted song.  


            """
        ),
        dcc.Markdown(""" 
        

        
        """
        ),



    ],
)

layout = dbc.Row([column1])