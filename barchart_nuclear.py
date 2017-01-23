# import needed modules
from bokeh.charts import Bar, output_file, save
import numpy as np
import pandas as pd
import csv

# get data into dataframe
df = pd.read_csv('energydata.csv')

# plot graph
plot_1 = Bar(df, 'Year/Month', values = 'Nuclear Energy (kJ)', title = 'Nuclear Energy by Month and Year', color = 'yellow')

# save
output_file('energychart_bar_nuclear.html')
save (plot_1)
