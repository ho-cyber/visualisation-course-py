from plotly.offline import plot
import plotly.graph_objs as go


data = [go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation = 'h'
)]

plot(data, filename='horizontal-bar')