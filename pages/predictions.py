# Imports from 3rd party libraries
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_daq as daq
# Imports from this application
from app import app
import joblib
import pandas as pd
import numpy as np
import sklearn
import requests
import json

#from spotify_model_2.
# import csvs from github
url_us = "https://raw.githubusercontent.com/James-yeh/Spotify-Rec/main/US.csv"
url_tracks = "https://media.githubusercontent.com/media/James-yeh/Spotify-Rec/main/tracks.csv"
url_datao = "https://raw.githubusercontent.com/James-yeh/Spotify-Rec/main/data_o.csv"
url_dbgo = "https://raw.githubusercontent.com/James-yeh/Spotify-Rec/main/data_by_genres_o.csv"

df = pd.read_csv('data.csv')
nn = joblib.load('model.z')
enc = joblib.load('encoder.z')


def song_suggester(song_obj):
    distance, neighbors = nn.kneighbors(np.array([song_obj]))
    suggestions = []
    for i in neighbors[0][1:]:
        suggestions.append([df['name'].iloc[i],df['artists'].iloc[i]*21583])
    sug = pd.DataFrame(suggestions,columns = ['song','artist'])
    sug['artist'] = enc.inverse_transform(sug['artist'].to_numpy().astype(int))
    return sug
# returns a dataframe of 20 songs from song suggester from an exact name

def predict(name):
    song = 'song'
    try:
        song = df[df['name']==name]
        recommendation = song_suggester(song.drop(columns=['name']).iloc[0])['song'][0]
    except:
        recommendation = 'Invalid Song Name. Try Again'

#    return song
    return recommendation
# Just call song(song_name) to get a d




# Possible code to provide suggestions for song names / auto complete
# name_list = list(df['name'])
#         html.Datalist(id="name_list", children=[
#         html.Option(value=name) for name in name_list
#     ]),

column1 = dbc.Col(
    [
        dcc.Markdown('## Song Recommendation', className='mb-5'),
        # Creates a Goal input and pass the value
        dcc.Markdown('#### Type the name of a song to receive recommendations for similar songs'),
        dcc.Input(
            id = "name",
            type='text',
#            autoComplete='True',
#            list = 'name_list',
            className='mb-5',
            ),

        dbc.Button("Predict Kickstarter Success", id="example-button", color='primary',
                   className="mr-2"),
        html.Div(id='container-button-timestamp'),
        html.Span(id="example-output",
                  style={"vertical-align": "middle"}),

        
    ],
    md=6,
)

# Set call back to be applied with button press.
@app.callback(
    Output("prediction-content",
           "children"), [Input("example-button", 'n_clicks')],
    [
        State('name', 'value'),

    ]
)
# Function that passes values to predict function on button click
def on_button_click(n, name):
    '''
    on_button_click function passes information from the model on clicl
    '''
    if n is None:
        return "Please provide the name of a song"
    else:
        recommendation = predict(name)
        return '{}'.format(recommendation)

# Create another callback for gauge probability
@app.callback(
    Output("my-gauge",
           "value"), [Input("example-button", 'n_clicks')],
    [
        State('name', 'value'),
    ]
)
# Pass predict function to retrive y_pred_proba
def predict_button_click(n_clicks, name):
    '''
    on_button_click function passes information from the model on click
    '''
    recommendation = predict(name)
    if n_clicks == None:
        return 0
    else:
        return recommendation

# Using a blank column for spacing
column2 = dbc.Col(
    className='mb-40'
)

column3 = dbc.Col(
    [
        # Create a lable and pass prediction value
        html.H2('Song Recommendation', className='mb-4'),
        html.Div(id='prediction-content', className='lead'),
    ],
    className='mb-40',
    md=5
)
layout = dbc.Row([column1, column2, column3])


