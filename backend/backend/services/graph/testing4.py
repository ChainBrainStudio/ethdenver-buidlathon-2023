import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from datetime import datetime

# load the data
data = {
    "timestamp": ["1677884747", "1677882095", "1677799043"],
    "blockNumber": ["16751120", "16750902", "16744077"],
    "againstWeightedVotes": ["0", "0", "0"],
    "abstainWeightedVotes": ["0", "0", "0"],
    "forWeightedVotes": ["614962668257407086130180", "353001604654166506809891", "168885005508323062872471"]
}

df = pd.DataFrame(data)

# convert columns to appropriate types
df["timestamp"] = df["timestamp"].apply(lambda x: datetime.fromtimestamp(int(x)))
df["blockNumber"] = df["blockNumber"].astype(int)
df["againstWeightedVotes"] = df["againstWeightedVotes"].astype(int)
df["abstainWeightedVotes"] = df["abstainWeightedVotes"].astype(int)
df["forWeightedVotes"] = df["forWeightedVotes"].astype(float)

# create a ColumnDataSource
source = ColumnDataSource(df)

# create a figure object
p = figure(x_axis_type="datetime", sizing_mode="stretch_width")

# add a line glyph
p.line(x="timestamp", y="forWeightedVotes", source=source)

# display the chart
show(p)
