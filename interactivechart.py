# import needed modules

import numpy as np
import pandas as pd
import csv
from bokeh.charts import Scatter, output_file, save
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxGroup

output_file("widgets.html")

# make widget
checkbox_group = CheckboxGroup(
        labels = ["Renewable Energy", "Nuclear Energy", "Natural Gas Energy"], active = [0, 1])

# save
save (widgetbox(checkbox_group))


