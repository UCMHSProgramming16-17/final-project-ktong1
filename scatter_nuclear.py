# import modules
from bokeh.charts import Scatter, output_file, save
import numpy as np
import pandas as pd
import csv

# get data into dataframe
df = pd.read_csv('energydata.csv')

# sort by year/month
df.sort_values(by = 'Year/Month')

# plot graph
plot_1 = Scatter(df, x = 'Year/Month', y = 'Nuclear Energy (kJ)', color = 'Year', title = "Nuclear Energy by Month and Year",
            xlabel = "Year-Month", ylabel = "Energy Produced (kJ)")

# output file
output_file("energychart_scatter_nuclear.html")

# save
save(plot_1)