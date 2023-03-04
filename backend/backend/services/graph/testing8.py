PROMPT ="""
You are an AI that helps write python code to visualize data. In the coming prompts I'll feed you questions that you need to turn into Python code to create Responsive charts using the Bokeh visualization library. Import all models from Bokeh. 

Convert all values that can be integers to integers or floats if the number is too big to convert to an integer. Convert Unix timestamps to DateTime objects using the datetime.datetime.fromtimestamp function and make sure it is the exact time down to the seconds. Write only code and do NOT use sentences.

Given this, please write Python code to visualize a colorful, Responsive chart in Bokeh for the defined data object below:"""
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
import datetime

# Define data object
data = {
    "data": {
      "proposals": [        {          "id": "86"        }      ],
      "voteDailySnapshots": [        {          "timestamp": "1677884747",          "blockNumber": "16751120",          "againstWeightedVotes": "0",          "abstainWeightedVotes": "0",          "forWeightedVotes": "614962668257407086130180"        },        {          "timestamp": "1677882095",          "blockNumber": "16750902",          "againstWeightedVotes": "0",          "abstainWeightedVotes": "0",          "forWeightedVotes": "353001604654166506809891"        },        {          "timestamp": "1677799043",          "blockNumber": "16744077",          "againstWeightedVotes": "0",          "abstainWeightedVotes": "0",          "forWeightedVotes": "168885005508323062872471"        }]
    }
}

# Convert Unix timestamps to datetime.datetime objects
for snapshot in data["data"]["voteDailySnapshots"]:
    snapshot["timestamp"] = datetime.datetime.fromtimestamp(int(snapshot["timestamp"]))

# Convert integer-like strings to integers or floats
for snapshot in data["data"]["voteDailySnapshots"]:
    snapshot["blockNumber"] = int(float(snapshot["blockNumber"]))
    snapshot["againstWeightedVotes"] = int(float(snapshot["againstWeightedVotes"]))
    snapshot["abstainWeightedVotes"] = int(float(snapshot["abstainWeightedVotes"]))
    snapshot["forWeightedVotes"] = float(snapshot["forWeightedVotes"])

# Create ColumnDataSource object
source = ColumnDataSource(data=data["data"]["voteDailySnapshots"])

# Create figure object
p = figure(x_axis_type='datetime', width=800, height=400, title='Vote Weighted by Time')

# Add glyphs to figure object
p.line(x='timestamp', y='forWeightedVotes', line_width=2, line_color=Spectral3[0], legend_label='For', source=source)
p.line(x='timestamp', y='againstWeightedVotes', line_width=2, line_color=Spectral3[1], legend_label='Against', source=source)
p.line(x='timestamp', y='abstainWeightedVotes', line_width=2, line_color=Spectral3[2], legend_label='Abstain', source=source)

# Add legend to figure object
p.legend.location = "top_left"
p.legend.click_policy="hide"

# Show figure object
show(p)
