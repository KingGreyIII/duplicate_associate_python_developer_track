from datetime import datetime, date
import pandas as pd

onebike_datetimes = pd.read_csv(
    '../csv_files/capital-onebike.csv',
    parse_dates=["Start date", "End date"],
    date_format="%d-%m-%y %H:%M"   # modern replacement for date_parser
)

# print(onebike_datetimes.head(5))

# count = 10
# while count > 0:
#     for a in onebike_datetimes:
#         print(a["start"])
#         count-= 1


# Part 1
# Create dictionary to hold counts
trip_counts = {'AM': 0, 'PM': 0}

# Loop over each row
for _, trip in onebike_datetimes.iterrows():
    start_time = trip["Start date"]
    if start_time.hour < 12:
        trip_counts["AM"] += 1
    else:
        trip_counts["PM"] += 1

print(trip_counts)


