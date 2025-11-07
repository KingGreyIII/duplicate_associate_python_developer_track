# #Importing necessary packages
# from datetime import datetime as dt
# from datetime import timedelta
# from dateutil import tz
# import pandas as pd
#
# # part 1 building format_date function
# # defining Variables
# time_value_1 = dt(2024,5, 12,3,4,8).timestamp()
# time_value_2 = dt.today() # the dt.date.now() and dt.date.today() isn't working but removing the date, it works -> dt.today() and dt.now() work
# test_timestamp = dt.fromtimestamp(time_value_1) #how do I create a timestamp manual after importing the datetime package , to solve the issue, i created a timestamp but i need to return it back to datetime object, that where the dt.fromtimestamp() comes in
# # print(time_value_2)
# test_datetime_format = "%d-%m-%Y"
#
# # Building format_date function
# def format_date(timestamp, datetime_format):
#     print(type(dt.strftime(timestamp, datetime_format))) # or
#     return timestamp.strftime(datetime_format)
#
# # calling function for testing
# # format_date(test_timestamp,test_datetime_format)
# """
# So in this section above, i created the functio smoothly without any hassle, but an issue arouse when i wanted to test the function, i need a way to parse a datatime object that was a timestamp not an int or float , else an error would arise
# so everything above it a little test run by me, normally i should clean up, but i decided to leave my rough as ref to see it the thought train can help me recap when i review after some time
# """
# # part 2 building calculate_landing_time()
# # defining variable
# test_rocket_launch_dt = dt(2023, 2, 15)
# test_travel_duration = timedelta(days= 20)
#
# # the function section
# def calculate_landing_time(rocket_launch_dt,travel_duration):
#     landing_date = (rocket_launch_dt + travel_duration).date()
#     return landing_date.strftime(test_datetime_format)
#
# # Testing section
# calculate_landing_time(test_rocket_launch_dt,test_travel_duration)
#
# # Part 3
# # defining variable
# test_expected_delivery_dt = dt(2026, 2, 15)
# test_current_dt = dt.today()
# print(test_current_dt.date())
#
# # the function section
# def days_until_delivery(expected_delivery_dt,current_dt):
#     estimated_day = (expected_delivery_dt - current_dt).days
#     print(type(estimated_day))
#
# # Testing section
# days_until_delivery(test_expected_delivery_dt,test_current_dt)
# """At the end, there was no timezone aspect, but wil relearn it later this month"""

# datacamp own exact replica
from datetime import datetime as dt
from datetime import timedelta, date

date_timeformat = "%d-%m-%Y"

# def format_date(timestamp, datetime_format):
#     print(dt.fromtimestamp(timestamp).strftime(datetime_format))
#     return dt.fromtimestamp(timestamp).strftime(datetime_format)
# # format_date(1514665153, "%d-%m-%Y")
#
# def calculate_landing_time(rocket_launch_dt,travel_duration):
#     landing = rocket_launch_dt + timedelta(days = travel_duration)
#
#     print(landing.date().strftime(date_timeformat))
# calculate_landing_time(dt(2023, 2, 15), 20)

def days_until_delivery(expected_delivery_dt, current_dt):
    print((expected_delivery_dt - current_dt).days)
    return (expected_delivery_dt - current_dt).days
days_until_delivery(dt(2023, 2, 15), dt(2023, 2, 5))