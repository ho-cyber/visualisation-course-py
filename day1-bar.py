from plotly.offline import plot
import plotly.graph_objs as go

data = [go.Bar(
            x=['giraffes', 
               'orangutans', 
               'monkeys'],
            y=[20, 14, 23]
    )]

plot(data)