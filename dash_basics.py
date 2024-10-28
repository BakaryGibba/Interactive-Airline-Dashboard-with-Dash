# Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read the airline data into pandas dataframe
airline_data = pd.read_csv('downloaded_airline_data.csv') #Needs to be completed 

#print(airline_data[['Flights', 'DistanceGroup']].head())
# Setting random state to be 42 so that we get same result
data = airline_data.sample(n=500, random_state=42)

data['Flights'] = data['Flights'].astype(int)

data_grouped = data.groupby('DistanceGroup')['Flights'].sum().reset_index()
# Pie Chart Creation

fig = px.pie(data_grouped, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div
# Add description about thegraph using html p (paragraph) component
# Finally, add graph component.

app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                        style={'textAlign': 'center',
                                               'color': '#503D36',
                                               'font-size': 40}),
                                html.P('Proportion of distance group (350 mile distance interval group) by flights',
                                      style={'textAlign':'center', 'color':'#F57241'}),
                                dcc.Graph(figure=fig),
                            ])
# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)