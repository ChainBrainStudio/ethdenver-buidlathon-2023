
PROMPT="""You are an AI that helps write python code to visualize data. In the coming prompts I'll feed you questions that you need to turn into Python code to create Responsive charts using the Bokeh visualization library. Show only code and do not use sentences. 

Convert all values that can be integers to integers or floats if the number is too big to convert to an integer. Convert Unix timestamps to DateTime objects using the datetime.datetime.fromtimestamp function and make sure it is the exact time down to the seconds. 

Given this, please write Python code to visualize 3 different Responsive charts in Bokeh for this data:


{
    "data": {
      "proposals": [
        {
          "id": "86"
        }
      ],
      "voteDailySnapshots": [
        {
          "timestamp": "1677884747",
          "blockNumber": "16751120",
          "againstWeightedVotes": "0",
          "abstainWeightedVotes": "0",
          "forWeightedVotes": "614962668257407086130180"
        },
        {
          "timestamp": "1677882095",
          "blockNumber": "16750902",
          "againstWeightedVotes": "0",
          "abstainWeightedVotes": "0",
          "forWeightedVotes": "353001604654166506809891"
        },
        {
          "timestamp": "1677799043",
          "blockNumber": "16744077",
          "againstWeightedVotes": "0",
          "abstainWeightedVotes": "0",
          "forWeightedVotes": "168885005508323062872471"
        }]}}"""


import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Convert Unix timestamps to DateTime objects
df = pd.DataFrame(data["data"]["voteDailySnapshots"])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# Convert values to integers or floats
df["blockNumber"] = pd.to_numeric(df["blockNumber"], downcast="integer")
df["againstWeightedVotes"] = pd.to_numeric(df["againstWeightedVotes"], downcast="float")
df["abstainWeightedVotes"] = pd.to_numeric(df["abstainWeightedVotes"], downcast="float")
df["forWeightedVotes"] = pd.to_numeric(df["forWeightedVotes"], downcast="float")

# Create ColumnDataSource
source = ColumnDataSource(df)

# Create chart 1: Line chart of forWeightedVotes over time
p1 = figure(title="For Weighted Votes Over Time",
            x_axis_label="Timestamp",
            y_axis_label="For Weighted Votes",
            x_axis_type="datetime",
            sizing_mode="stretch_both")
p1.line(x="timestamp", y="forWeightedVotes", source=source)

# Create chart 2: Bar chart of blockNumber vs forWeightedVotes
p2 = figure(title="For Weighted Votes vs Block Number",
            x_axis_label="Block Number",
            y_axis_label="For Weighted Votes",
            sizing_mode="stretch_both")
p2.vbar(x="blockNumber", top="forWeightedVotes", source=source, width=0.9)

# Create chart 3: Stacked bar chart of all vote types
p3 = figure(title="Vote Types Over Time",
            x_axis_label="Timestamp",
            y_axis_label="Weighted Votes",
            x_axis_type="datetime",
            sizing_mode="stretch_both")
p3.vbar_stack(["forWeightedVotes", "againstWeightedVotes", "abstainWeightedVotes"],
              x="timestamp", source=source, width=0.9)

# Show charts
show(p1)
show(p2)
show(p3)
