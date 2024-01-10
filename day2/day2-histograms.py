import pandas as pd
import numpy as np
import plotly.plotly as py
import colorlover as cl
from plotly.offline import plot
import plotly.graph_objs as go

scl = cl.scales['9']['seq']['Blues']
colorscale = [ [ float(i)/float(len(scl)-1), 
                scl[i] ] for i in range(len(scl)) ]
colorscale


N = 500
mean, cov = [0, 2], [(1, .5), (.5, 1)]
x, y = np.random.multivariate_normal(mean, cov, size=50).T
df = pd.DataFrame({'x': x, 'y': y})
df.head()

data = [
    go.Histogram2dContour(
        x=df['x'],
        y=df['y'],
        colorscale=colorscale
    )
]

axis_template = dict(
    ticks='',
    showgrid=False,
    zeroline=False,
    showline=True,
    mirror=True,
    linewidth=2,
    linecolor='#444',
)

layout=go.Layout(xaxis=axis_template,
                 yaxis=axis_template,
                 width=700,
                 height=750,
                 autosize=False,
                 hovermode='closest',
                 title='2d Histogram in Pandas')

fig = go.Figure(data=data, layout=layout)

plot(fig)