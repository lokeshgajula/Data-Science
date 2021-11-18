import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

airline_data = pd.read_csv('airline_data.csv',
                           encoding="ISO-8859-1",
                           dtype={'Div1Airport':str,'Div1TailNum':str,
                                  'Div2Airport':str,'Div2TailNum':str})
app = dash.Dash(__name__)
app.layout = html.Div(children = [html.H1("Interactive Line Plot",
                                          style={'textAlign':'center',
                                                 'color':'red',
                                                 'font-size':40}),
                                  html.Div(["input year", dcc.Input(id="input-yr",
                                                                    value=2010,
                                                                    type='number',
                                                                    style={'height':'50px',
                                                                           'font-size':35}),],
                                           style={'font-size':40}),
                                  html.Br(),
                                  html.Br(),
                                  html.Div(dcc.Graph(id='scatter-plot')),])
@app.callback(Output(component_id = 'scatter-plot', component_property='figure'),
              Input(component_id='input-yr',component_property='value'))
def get_graph(entered_year):
    df = airline_data[airline_data['Year']==int(entered_year)]
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    fig = go.Figure(data = go.Scatter(x=line_data['Month'],y=line_data['ArrDelay'],mode='lines',marker=dict(color='green')))
    fig.update_layout(title="Month vs Avg Flight Delay Time", xaxis_title="Monthe", yaxis_title="AvgDelay")
    return fig
if __name__=='__main__':
    app.run_server()
    
