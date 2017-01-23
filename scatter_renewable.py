# import modules
from bokeh.charts import Scatter, output_file, save
import numpy as np
import pandas as pd
import csv

# get data into dataframe
df = pd.read_csv('energydata.csv')

# sort by year/month
df.sort_values(by = 'Year/Month')

print(df)

# plot graph
plot_1 = Scatter(df, x = 'Year/Month', y = 'Renewable Energy (kJ)', title = "Renewable Energy by Month and Year",
            xlabel = "Year-Month", ylabel = "Energy Produced (kJ)")

# output file
output_file("energychart_scatter_renewable.html")

# save
save(plot_1)