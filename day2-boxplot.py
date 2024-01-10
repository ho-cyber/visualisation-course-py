import string
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go

N = 100
y_vals = {}
for letter in list(string.ascii_uppercase):
     y_vals[letter] = np.random.randn(N)+ (3*np.random.randn())
        
df = pd.DataFrame(y_vals)
df.head()

data = []

for col in df.columns:
    data.append(  go.Box( y=df[col], 
                         name=col, 
                         showlegend=False ) )

data.append( go.Scatter( x = df.columns, 
                        y = df.mean(), 
                        mode='lines', 
                        name='mean' ) )

plot(data)
