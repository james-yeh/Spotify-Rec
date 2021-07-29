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
            #### Our app uses nearest neighbor to predict a song recommendation 
            #### using a Kaggle dataset.  The app itself is build from plotly.
        

            """
        ),
        dcc.Markdown(""" 
        

        
        """
        ),



    ],
)

layout = dbc.Row([column1])