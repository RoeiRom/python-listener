from datetime import datetime

import pandas as pd
import numpy as np

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

results = [
    {
        "date": datetime(2021, 6, 16, hour=18, minute=0),
        "value": 100
    },
    {
        "date": datetime(2021, 6, 16, hour=18, minute=0, second=5),
        "value": 200
    },
    {
        "date": datetime(2021, 6, 16, hour=18, minute=0, second=10),
        "value": 150
    }
]

mapped_array = [[value.get("date"), value.get("value")] for value in results]

dataFrame = pd.DataFrame(mapped_array, columns=["date", "value"])
sorted_data_frame = dataFrame.sort_values("date", ascending=True)

test = np.array([timestamp(dateSample) for dateSample in sorted_data_frame["date"].to_list()])
diffs = [0]
for diffs_index in range(1, len(test)):
    diffs.append(test[diffs_index] - test[0])
sorted_data_frame['date'] = diffs
sorted_data_frame.rename(columns={'date': 'x', 'value': 'y'}, inplace=True)
x_diffs = np.diff(sorted_data_frame['x'].to_numpy())
y_diffs = np.diff(sorted_data_frame['y'].to_numpy())
inclines = []
for index in range(len(x_diffs)):
    inclines.append(y_diffs[index] / x_diffs[index])

print(inclines)
