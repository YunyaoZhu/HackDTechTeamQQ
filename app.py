# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('data/datasets_One_Year_of_FitBitChargeHR_Data.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Date'] = pd.to_datetime(df['Date'],format='%d-%m-%Y')
df['Day of month'] = pd.to_datetime(df['Date']).dt.day

df['Calories'] = df['Calories'].apply(lambda x: x*1000)
df[['Distance']] = df[['Distance']].apply(lambda x: x.astype(str).str.replace(",",".").astype(float) * 0.621371)
df['all_activity'] = df[['Minutes_of_intense_activity','Minutes_of_moderate_activity','Minutes_of_slow_activity']].sum(axis=1)
col_select = ['Calories','Minutes_of_intense_activity','Minutes_of_moderate_activity','Minutes_of_slow_activity','all_activity']
wide_df = df[col_select]

## Groupby the weekday and plot statistics by day of the week
df.index = df['Date']
by_weekday = pd.DataFrame()
by_weekday['Calories'] = df['Calories'].groupby(df.index.dayofweek).mean()
by_weekday['Week_day'] = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

df_Date = pd.read_csv('data/datasets_One_Year_of_FitBitChargeHR_Data.csv', index_col=0, parse_dates=True)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_options):
    dict_list = []
    for i in list_options:
        dict_list.append({'label': i, 'value': i})

    return dict_list

### Stack df  to make scatter plot of minutes vs date (activity as level)
df_bar = df_Date[['Minutes_sitting', 'Minutes_of_slow_activity', 'Minutes_of_moderate_activity',
             'Minutes_of_intense_activity']]

stacked = df_bar.stack().reset_index().rename(columns={
    'level_1': 'Activity',
    0: 'Minutes'
})


stacked['Activity'] = stacked['Activity'].str.replace('Minutes_of_', '')


barfig = px.scatter(stacked, x="Date", y = "Minutes", color="Activity",
                    title="Time spent on each activity type over time")
#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

linefig = px.line(df, x='Date', y='Calories', title="Calories consumed over time")


boxplot = px.box(df, x ="Day of month", y="Calories", title="Calories consumed by day of month")

linefig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

barfig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

boxplot.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

data = "The dataset comes from "
motivation="Collateral health impacts of covid-19"

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Your Personalized Health Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.H4(
        children="Descriptive, not Prescriptive Healthcare",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Don\'t let algorithms decide for you, '
                      'gain control over your lifestyle based on data we expose',
             style={
        'textAlign': 'center',
        'color': colors['text']
    }),





    # html.Label('Dropdown'),
    #     dcc.Dropdown(
    #         id  = "y_selector",
    #         options=[
    #         {'label': 'Distance', 'value': df[['Distance']]},
    #         {'label': 'Calories', 'value': df[['Calories']]},
    #         {'label': 'Steps', 'value': df[['Steps']]},
    #         {'label': 'floors', 'value': df[['floors']]},
    #         {'label': 'Minutes_sitting', 'value': df[['Minutes_sitting']]},
    #             {'label': 'Minutes_of_slow_activity', 'value': df[['Minutes_of_slow_activity']]},
    #             {'label': 'Minutes_of_moderate_activity', 'value': df[['Minutes_of_moderate_activity']]},
    #             {'label': 'Minutes_of_intense_activity', 'value': df[['Minutes_of_intense_activity']]},
    #             {'label': 'Calories_Activity', 'value': df[['Calories_Activity']]}
    #         ],
    #
    # ),

    dcc.Graph(id='timeseries',
            config={'displayModeBar': False},
            animate=True,
            figure=linefig),

    dcc.Graph(
        id='barplot',
        figure=barfig),

    dcc.Graph(
        id="boxplot",
        figure=boxplot),

    html.Div(children='The data used comes from https://www.kaggle.com/alketcecaj/one-year-of-fitbit-chargehr-data'
                      ,
             style={
            'textAlign': 'left',
            'color': colors['text']
    }),






])


# # Update Time Series
# @app.callback(Output('timeseries', 'figure'),
#               [Input('id of input component', 'value')])
#
#
# #px.line(df, x='Date', y='Calories')
# def update_graph(yaxis_column_name):
#     fig = px.line(x='Date',
#                   y=yaxis_column_name)


   # fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')



  #  return fig

if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(host='127.0.0.1', port=8050, debug=True)
