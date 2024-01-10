import numpy as np
import datetime
import plotly.graph_objs as go
from plotly.offline import plot

trace = go.Heatmap(z = [[1, 20, 30, 50, 1],
                       [20, 1, 60, 80, 30],
                       [30, 60, 1, -10, 20]],
                  x = ['Moday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday'],
                  y = ['Morning', 'Sfternoon', 'Evening'])
data = [trace]
plot(data)