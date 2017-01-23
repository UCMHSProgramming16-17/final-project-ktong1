# import needed modules
from bokeh.charts import Bar, output_file, save
import numpy as np
import pandas as pd
import csv

# get data into dataframe
df = pd.read_csv('energydata.csv')

# plot graph
plot_1 = Bar(df, 'Year/Month', values = 'Renewable Energy (kJ)', title = 'Renewable Energy by Year', color = 'green')

# save
output_file('energychart_bar_renewable.html')
save (plot_1)
