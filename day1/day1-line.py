
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np


N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

plot(data, filename='basic-line')