# import needed modules
import numpy as np
import pandas as pd
import csv
from bokeh.charts import Scatter, output_file, save
from bokeh.layouts import gridplot
from bokeh.models.ranges import Range1d

# get into dataframe
df = pd.read_csv('energydata.csv')

# plot graph 1
plot_1 = Scatter(df, x = 'Year/Month', y = 'Renewable Energy (kJ)', color = 'green', title = "Renewable Energy by Month and Year",
            xlabel = "Year-Month", ylabel = "Energy Produced (kJ)")

# plot graph 2 with locked axes
plot_2 = Scatter(df, x_range = plot_1.x_range, x = 'Year/Month', y = 'Nuclear Energy (kJ)', color = 'black', title = "Nuclear Energy by Month and Year",
            xlabel = "Year-Month", ylabel = "Energy Produced (kJ)")
            
# plot graph 3
plot_3 = Scatter(df, x_range = plot_1.x_range, x = 'Year/Month', y = 'Natural Gas Energy (kJ)', color = 'red', title = "Natural Gas Energy by Month and Year",
            xlabel = "Year-Month", ylabel = "Energy Produced (kJ)")

# link plots
plot_final = gridplot([[plot_1, plot_2, plot_3]])

# output file
output_file("energychart.html")

# save
save(plot_final)
