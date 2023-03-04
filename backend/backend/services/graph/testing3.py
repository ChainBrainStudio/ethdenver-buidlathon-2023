from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import datetime

# Define data
data = {
    "timestamp": ["1677884747", "1677882095", "1677799043"],
    "blockNumber": ["16751120", "16750902", "16744077"],
    "againstWeightedVotes": ["0", "0", "0"],
    "abstainWeightedVotes": ["0", "0", "0"],
    "forWeightedVotes": ["614962668257407086130180", "353001604654166506809891", "168885005508323062872471"]
}

# Convert data types
data["timestamp"] = [datetime.datetime.fromtimestamp(int(x)) for x in data["timestamp"]]
data["blockNumber"] = [int(x) for x in data["blockNumber"]]
data["againstWeightedVotes"] = [float(x) for x in data["againstWeightedVotes"]]
data["abstainWeightedVotes"] = [float(x) for x in data["abstainWeightedVotes"]]
data["forWeightedVotes"] = [float(x) for x in data["forWeightedVotes"]]

# Create ColumnDataSource
source = ColumnDataSource(data=data)

# Create figure
fig = figure(x_axis_type='datetime', sizing_mode='scale_width', title="Vote Daily Snapshots")

# Add lines
fig.line(x='timestamp', y='forWeightedVotes', source=source, legend_label="For Weighted Votes", line_width=2, line_color="green")
fig.line(x='timestamp', y='againstWeightedVotes', source=source, legend_label="Against Weighted Votes", line_width=2, line_color="red")
fig.line(x='timestamp', y='abstainWeightedVotes', source=source, legend_label="Abstain Weighted Votes", line_width=2, line_color="blue")

# Format plot
fig.xaxis.axis_label = "Timestamp"
fig.yaxis.axis_label = "Weighted Votes"
fig.legend.location = "top_left"

# Show plot
show(column(fig))
