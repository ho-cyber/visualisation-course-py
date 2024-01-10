from plotly.offline import plot


subject = ['Moe', 'Larry', 'Curly',
           'Moe', 'Larry', 'Curly',
           'Moe', 'Larry', 'Curly',
           'Moe', 'Larry', 'Curly']

score = [1, 6, 2, 8, 2, 9,
         4, 5, 1, 5, 2, 8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', 
        enabled = True),
    ]
  )]
)]


plot({'data': data}, validate=False)