"""
Dashboard for vacation planning

Author: Erich Kinder

"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import weather_pull
from datetime import date

today = date.today()

app = Dash(__name__)

# Get the weather data from https://www.visualcrossing.com/ via an API call

weather_data = weather_pull.pull_weather_data('Calistoga', '11/29/2022', '12/02/2022')

temp_fig = px.line(weather_data, x='datetime', y=['tempmax', 'tempmin'])

app.layout = html.Div(children=[
    html.H1(children='Travel Dashboard for ' + 'Calistoga'),
    dcc.DatePickerRange(
        id='vacation-dates',
        min_date_allowed=today,
        initial_visible_month=today
    ),

    dcc.Graph(id='temp', figure=temp_fig)
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050")
