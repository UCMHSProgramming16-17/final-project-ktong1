# import needed modules

import numpy as np
import pandas as pd
import csv
from bokeh.plotting import figure, output_file, save
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxGroup

output_file("checkbox_group.html")

checkbox_group = CheckboxGroup(
        labels = ["Renewable Energy", "Nuclear Energy", "Natural Gas Energy"], active = [0, 1])

save (widgetbox(checkbox_group))