# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:05:15 2024

@author: SWRM
"""
from dash import Dash, dcc, html, Input, State, Output, callback
import dash_bootstrap_components as dbc
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=dbc.Container([
    dbc.Row([
        dbc.Col([html.H1("Select your Gender"),dcc.Dropdown(["male","female"],value="male",id="gender")],width=3),
        dbc.Col([html.H1("Select your race"),dcc.Dropdown(["group A","group B", "group C","group D","group E"],value="group A",id="race")],width=3),
        dbc.Col([html.H1("Parental level of education"),dcc.Dropdown(["associate's degree","bachelor's degree", "high school","master's degree","some college","some high school"],value="associate's degree",id="degree")],width=3),
        dbc.Col([html.H1("Select your lunch type"),dcc.Dropdown(["free/reduced","standard"],value="free/reduced",id="lunch")],width=3)
        ]),
    dbc.Row([
        dbc.Col([html.H1("Select your Test preparation technique"),dcc.Dropdown(["none","completed"],value="none",id="test_prep")],width=4),
        dbc.Col([html.H1("Type your writing score"),dcc.Input(placeholder="Please enter here",value="",id="writing")],width=4),
        dbc.Col([html.H1("Type your reading score"),dcc.Input(placeholder="Please enter here",value="",id="reading")],width=4)
        ]),
    dbc.Row(dbc.Col([html.Button('Submit', id='submit-val', n_clicks=0),
             html.Div(id='answer',children='The prediction for your math score is')]))
    
    ])

@callback(
    Output("answer","children"),
    Input("gender","value"),
    Input("race","value"),
    Input("degree","value"),
    Input("lunch","value"),
    Input("test_prep","value"),
    State("writing","value"),
    State("reading","value"),
    Input("submit-val","n_clicks"),
    prevent_initial_call=True
    )


def outputer(
        gender,
        race_ethnicity,
        parental_level_of_education,
        lunch,
        test_preparation_course,
        reading_score: int,
        writing_score: int,submit ):
    data=CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=int(reading_score),
        writing_score=int(writing_score))
    features=data.get_data_as_data_frame()
    predictions=PredictPipeline()
    prediction_values=predictions.predict(features)
    return 'The prediction for your math score is "{}"'.format(
        prediction_values
    )


if __name__=="__main__":
    app.run(debug=True)      