import matplotlib.pyplot as plt
import json
import pandas as pd 
import numpy as np
# from AutoClean import AutoClean
from autoviz.AutoViz_Class import AutoViz_Class
import datetime as dt


from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# data = json.load(open('sampledata.json'))
# df = pd.DataFrame(data['data']['voteDailySnapshots'])
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from datetime import datetime



data = json.load(open('sampledata.json'))
df = pd.DataFrame(data['data']['voteDailySnapshots'])
# Loop through each column in the DataFrame
for col in df.columns:
    # Convert values to integers if possible
    if df[col].dtype == 'object' and df[col].str.isnumeric().all():
        try:
            df[col] = df[col].astype(np.int64)
        except:
            df[col] = df[col].astype(float)

    # Convert values to datetime objects if possible
    elif df[col].dtype == 'object':
        print('in elif')
        try:
            print('in try')
            df[col] = dt.datetime.utcfromtimestamp(int(df[col])).strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
        except ValueError:
            pass
AV = AutoViz_Class()
# AV.AutoViz(filename = 'data_to_csv_test.csv', sep = ",")
# sep = ","
dft = AV.AutoViz(
    filename = '/Users/marissaposner/ethdenver-buidlathon-2023/backend/backend/services/graph/data_to_csv_test.csv',
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=0,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
    save_plot_dir=None
)