from plotly.offline import plot

subject = ['Moe', 'Larry', 'Curly',
           'Moe', 'Larry', 'Curly',
           'Moe', 'Larry', 'Curly',
           'Moe', 'Larry', 'Curly']

score = [1, 6, 2, 8, 2, 9,
         4, 5, 1, 5, 2, 8]
aggs = ["count","sum","avg","median","mode",
        "rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)


data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
  xaxis = dict(title = 'Subject'),
  yaxis = dict(title = 'Score', range = [0,22]),
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

plot({'data': data,'layout': layout}, validate=False)