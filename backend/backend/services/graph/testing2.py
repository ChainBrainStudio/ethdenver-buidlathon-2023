from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from datetime import datetime

# Data
timestamps = ["1677884747", "1677882095", "1677799043"]
block_numbers = ["16751120", "16750902", "16744077"]
for_weighted_votes = ["614962668257407086130180", "353001604654166506809891", "168885005508323062872471"]
for_weighted_votes = [int(x) for x in for_weighted_votes]

# Convert timestamps to datetime objects
timestamps = [datetime.fromtimestamp(int(x)) for x in timestamps]

# Create a column data source
source = ColumnDataSource(data=dict(timestamps=timestamps, block_numbers=block_numbers, for_weighted_votes=for_weighted_votes))

# Create a figure
p = figure(title="Vote Daily Snapshots", x_axis_label="Timestamp", y_axis_label="For Weighted Votes", x_axis_type='datetime')

# Add a line plot
p.line(x='timestamps', y='for_weighted_votes', line_width=2, source=source)

# Format the x-axis
p.xaxis.formatter = DatetimeTickFormatter(days="%m/%d %H:%M",
months="%m/%d %H:%M",
hours="%m/%d %H:%M",
minutes="%m/%d %H:%M")

# Show the plot
show(p)
