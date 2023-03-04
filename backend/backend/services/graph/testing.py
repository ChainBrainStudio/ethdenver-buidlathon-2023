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

# create data frame
data = json.load(open('sampledata.json'))
df = pd.DataFrame(data['data']['voteDailySnapshots'])
print(df)
import pandas as pd
import datetime

def convert_int_columns(df):
    for col in df.iteritems():
        if df[col].dtype == 'object':
            continue
        try:
            df[col] = pd.to_numeric(df[col], downcast='integer')
        except ValueError:
            try:
                df[col] = pd.to_numeric(df[col], downcast='float')
            except ValueError:
                pass
    
    for col in df.columns:
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            df[col] = df[col].astype('Int64')
    
    for col in df.columns:
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            df[col] = df[col].astype(float)
            df[col] = df[col].astype(pd.Int64Dtype()).astype(float)

def convert_unix_timestamps(df):
    for col in df.columns:
        if df[col].dtype == 'int64':
            try:
                df[col] = pd.to_datetime(df[col], unit='s', utc=True)
            except ValueError:
                pass
df = convert_int_columns(df)
df = convert_unix_timestamps(df)


print(df.dtypes)

# # convert Unix timestamps to datetime
# df["timestamp"] = df["timestamp"].apply(lambda x: datetime.utcfromtimestamp(int(x)).strftime('%Y-%m-%d %H:%M:%S'))
# df['timestamp']=pd.to_datetime(df['timestamp'])
# print(df['timestamp'])

# # convert numeric columns to integers
# df["blockNumber"] = df["blockNumber"].astype(int)
# df["againstWeightedVotes"] = df["againstWeightedVotes"].astype(float)
# df["abstainWeightedVotes"] = df["abstainWeightedVotes"].astype(float)
# df["forWeightedVotes"] = df["forWeightedVotes"].astype(float)
    
# # create a new column with the total votes
# df["totalWeightedVotes"] = df["againstWeightedVotes"] + df["abstainWeightedVotes"] + df["forWeightedVotes"]
# print(df.dtypes)
# # create a column data source
# source = ColumnDataSource(df)

# # create a figure object
# p = figure(x_axis_type='datetime', title="Weighted Votes over Time")

# # create a line plot for "forWeightedVotes" column
# p.line(x="timestamp", y="forWeightedVotes", source=source, line_color="blue", legend_label="For")

# # create a line plot for "againstWeightedVotes" column
# p.line(x="timestamp", y="againstWeightedVotes", source=source, line_color="red", legend_label="Against")

# # create a line plot for "abstainWeightedVotes" column
# p.line(x="timestamp", y="abstainWeightedVotes", source=source, line_color="gray", legend_label="Abstain")

# # create a line plot for "totalWeightedVotes" column
# p.line(x="timestamp", y="totalWeightedVotes", source=source, line_color="green", legend_label="Total")

# # show the figure
# show(p)


# # First, let's extract the vote data from the input
# vote_data = {
#     "data": {
#         "proposals": [{"id": "86"}],
#         "voteDailySnapshots": [
#             {
#                 "timestamp": "1677884747",
#                 "blockNumber": "16751120",
#                 "againstWeightedVotes": "0",
#                 "abstainWeightedVotes": "0",
#                 "forWeightedVotes": "614962668257407086130180",
#             },
#             {
#                 "timestamp": "1677882095",
#                 "blockNumber": "16750902",
#                 "againstWeightedVotes": "0",
#                 "abstainWeightedVotes": "0",
#                 "forWeightedVotes": "353001604654166506809891",
#             },
#             {
#                 "timestamp": "1677799043",
#                 "blockNumber": "16744077",
#                 "againstWeightedVotes": "0",
#                 "abstainWeightedVotes": "0",
#                 "forWeightedVotes": "168885005508323062872471",
#             },
#         ],
#     }
# }

# # Create a figure object
# p = figure(title="Vote Daily Snapshots", x_axis_label="Timestamp", y_axis_label="For Weighted Votes")

# # Extract x and y values from vote data
# x_values = [int(vote["timestamp"]) for vote in vote_data["data"]["voteDailySnapshots"]]
# y_values = [int(vote["forWeightedVotes"]) for vote in vote_data["data"]["voteDailySnapshots"]]

# # Add a line to the figure
# p.line(x_values, y_values, line_width=2)

# # Show the figure
# show(p)



# data = json.load(open('sampledata.json'))
# df = pd.DataFrame(data['data']['voteDailySnapshots'])
# # Loop through each column in the DataFrame
# for col in df.columns:
#     # Convert values to integers if possible
#     if df[col].dtype == 'object' and df[col].str.isnumeric().all():
#         try:
#             df[col] = df[col].astype(np.int64)
#         except:
#             df[col] = df[col].astype(float)

#     # Convert values to datetime objects if possible
#     elif df[col].dtype == 'object':
#         print('in elif')
#         try:
#             print('in try')
#             df[col] = dt.datetime.utcfromtimestamp(int(df[col])).strftime(
#                             "%Y-%m-%d %H:%M:%S"
#                         )
#         except ValueError:
#             pass

# print(df.dtypes)

# # pipeline = AutoClean(df, mode = 'auto', extract_datetime='auto')
# # print('pipeline output', pipeline.output.dtypes)
# # print('pipeline', pipeline)

# df.to_csv('data_to_csv_test.csv', sep='\t')
# # print(df.dtypes)
# datapath = ''

# # print("data      ", data["data"]["voteDailySnapshots"])
# # print(pd.json_normalize(data['voteDailySnapshots']))

# AV = AutoViz_Class()
# AV.AutoViz(filename = 'data_to_csv_test.csv', sep = ",")
# sep = ","
# dft = AV.AutoViz(
#     filename = data["data"]["voteDailySnapshots"],
#     sep=",",
#     depVar="",
#     dfte=None,
#     header=0,
#     verbose=0,
#     lowess=False,
#     chart_format="svg",
#     max_rows_analyzed=150000,
#     max_cols_analyzed=30,
#     save_plot_dir=None
# )

# # Extract the data from the JSON data
# timestamps = [int(snapshot['timestamp']) for snapshot in data['data']['voteDailySnapshots']]
# for_votes = [int(snapshot['forWeightedVotes']) for snapshot in data['data']['voteDailySnapshots']]
# against_votes = [int(snapshot['againstWeightedVotes']) for snapshot in data['data']['voteDailySnapshots']]
# abstain_votes = [int(snapshot['abstainWeightedVotes']) for snapshot in data['data']['voteDailySnapshots']]

# # Plot the data
# plt.plot(timestamps, for_votes, label='forWeightedVotes')
# plt.plot(timestamps, against_votes, label='againstWeightedVotes')
# plt.plot(timestamps, abstain_votes, label='abstainWeightedVotes')
# plt.xlabel('Timestamp')
# plt.ylabel('Weighted Votes')
# plt.title('Weighted Votes Over Time')
# plt.legend()
# plt.show()

