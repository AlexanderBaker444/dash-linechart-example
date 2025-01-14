import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Stock Value in the Early 2000's"
mytitle = "Stock Value Over Time"
x_values = ['2003', '2005', '2007', '2009', '2011', '2013','20015','2017']
y1_values = [100, 80, 200, 140, 250, 300,150,180]
y2_values = [10, 20, 30, 40, 50, 60,70,80]
y3_values = [100, 100, 100, 100, 100, 100,100,100]
color1 = 'red'
color2 = 'blue'
color3 = 'yellow'
name1 = 'Stock 1'
name2 = 'Stock 2'
name3 = 'Stock 3'
tabtitle = 'Stocks and Bonds'
sourceurl = 'https://www.Stock-Value.com'
githublink = 'https://github.com/AlexanderBaker444/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
