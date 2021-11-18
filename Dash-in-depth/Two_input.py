import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

airline_data = pd.read_csv('airline_data.csv',
                           encoding = "ISO-8859-1",
                           dtype = {"Div1Airport":str,
                                    "Div1TailNum":str,
                                    "Div2Airport":str,
                                    "Div2TailNum":str})
app = dash.Dash()
app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                        style={'textAlign':'center',
                                               'color':'red',
                                               'font-size':40}),
                                html.Div(['Year: ',dcc.Input(id='input-yr',
                                                              value='2010',
                                                              type='number',
                                                              style={'height':'50px',
                                                                     'font-size':35})]),
                                html.Div(["State Abbreviation: ", dcc.Input(id='input-ab',
                                                                            value='AL',
                                                                            type='text',
                                                                            style={'height':'50px',
                                                                                   'font-size':40})]),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='bar-plot')),])
@app.callback(Output(component_id = 'bar-plot', component_property='figure'),
              [Input(component_id='input-yr', component_property='value'),
              Input(component_id='input-ab', component_property='value')])
def get_graph(entered_year,entered_state):
    df = airline_data[(airline_data['Year']==int(entered_year)) &
                      (airline_data['OriginState']==entered_state)]
    g1 = df.groupby(['Reporting_Airline'])['Flights'].sum().nlargest(10).reset_index()
    fig1 = px.bar(g1, x='Reporting_Airline',y='Flights', title='Top 10 airline carrier in year ' + str(entered_year) + ' in terms of number of flights')
    fig1.update_layout()
    return fig1

if __name__=='__main__':
    app.run_server(port=8002, host='127.0.0.1',debug=True)
