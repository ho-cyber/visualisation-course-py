from plotly.offline import plot

subject = ['Math', 'Sci', 'Eng',
           'Math', 'Sci', 'Eng',
           'Math', 'Sci', 'Eng',
           'Math', 'Sci', 'Eng']

score = [1, 6, 2, 8, 2, 9,
         4, 5, 1, 5, 2, 8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'filter',
    target = 'y',
    operation = '>',
    value = 4
  )]
)]

layout = dict(
    title = 'Scores > 4'
)

plot({'data': data, 'layout': layout}, validate=False)