from datetime import *
year, month, day = map(int, input().split("-"))
dt = date(year, month, day)
delta = timedelta(days = int(input()))
print((dt + delta).strftime("%Y-%m-%d"))