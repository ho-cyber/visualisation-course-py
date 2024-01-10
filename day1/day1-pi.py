from plotly.offline import plot
import plotly.graph_objs as go

labels = ['Oxygen','Hydrogen',
          'Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

trace = go.Pie(labels=labels, values=values)

plot([trace])

