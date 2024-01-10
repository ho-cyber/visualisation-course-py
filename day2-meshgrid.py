import chart_studio
import plotly.graph_objs as go
import numpy as np
from plotly.offline import plot
import plotly.figure_factory as FF

x = np.linspace(0, 10, 250)
y = np.sin(x)

trace = go.Scatter(x=x, y=y,
                  mode='markers')
data=[trace]
plot(data)

x = np.arange(0, 100)
y = np.arange(0, 200, 2)
trace = go.Scatter(x=x, y=y,
                  mode = 'markers')
data = [trace]
plot(data)

x = np.arange(-10, 10, 0.4)
y = np.arange(-10, 10, 0.4)
XX, YY = np.meshgrid(x, y)
ZZ = np.sin(XX**2 + YY**2) / (XX**2 + YY**2)

lines = []
line_marker = dict(color='#0066FF', width=2)
for i, j, k in zip(XX, YY, ZZ):
    lines.append(go.Scatter3d(x=i, y=j, z=k, 
                              mode='lines', 
                              line=line_marker))

layout = go.Layout(
    title='Wireframe with Meshgrid',
    showlegend=False
)

fig = go.Figure(data=lines, layout=layout)
plot(fig)

shape = (4, 6)
zeros_array = np.empty(shape)

colorscale = [[0, 'rgb(49, 52, 92)'],
             [1, 'rgb(49, 52, 92)']]

font_colors = ['rgb(255, 255, 255)']

table = FF.create_table(zeros_array,
                       colorscale,
                       font_colors)

plot(table)