"""
countdown calculator
"""

from datetime import datetime

date_start = input("Enter starting date (year-month-day): ")
date_end = input("Enter end date (year-month-day): ")

d1_list = date_start.split("-")
d2_list = date_end.split("-")

time_one = datetime(int(d1_list[0]), int(d1_list[1]), int(d1_list[2]))
time_two = datetime(int(d2_list[0]), int(d2_list[1]), int(d2_list[2]))

time_three = time_one - time_two

print(time_three)
