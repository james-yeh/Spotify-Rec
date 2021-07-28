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
# import pickle, json
import pandas as pd
import numpy as np
import requests
import json


def predict(name):
    
    example = df_clean.loc[df_clean['name'] == name].head(1)

    recommendation = model.predict(example)[0]

    return recommendation



column1 = dbc.Col(
    [
        dcc.Markdown('## Song Recommendation', className='mb-5'),
        # Creates a Goal input and pass the value
        dcc.Markdown('#### Type the name of a song to receive recommendations for similar songs'),
        dcc.Input(
            id = "name",
            type='text',
            autocomplete='on',
#            list = list(df['name']),
            className='mb-5', size=540
            ),
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


