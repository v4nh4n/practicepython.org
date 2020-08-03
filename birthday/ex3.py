import json
from bokeh.plotting import figure, show, output_file


with open("info.json","r+") as f:
    info = json.load(f)

output_file("plot.html")

scientists = []
for i in info:
    scientists.append(i)

birthday_months = []
for i in info:
    birthday_months.append(info[i][:2])

p = figure(x_range=scientists, plot_height=250, title="Scientists birthday months")
p.vbar(x=scientists, top=birthday_months, width=0.9)
p.y_range.start = 0
show(p)


