"""
# Notes for `datetime` Library with Alias `dt`

This file contains explanations and code examples for working with the `datetime` library in Python.

## 1. Working with Dates
   - Use `dt.date` for creating and manipulating date objects.
   - Get today's date with `dt.date.today()`.
   - Access components using `.year`, `.month`, `.day`.

## 2. Working with Times
   - Use `dt.time` for creating and manipulating time objects.
   - Access components using `.hour`, `.minute`, `.second`.

## 3. Working with Date and Time
   - Use `dt.datetime` for date and time combined.
   - Get the current date and time using `dt.datetime.now()`.

## 4. Formatting and Parsing
   - Format a datetime object to a string using `.strftime()`.
   - Parse a string into a datetime object using `dt.datetime.strptime()`.

## 5. Time Delta Operations
   - Use `timedelta` for arithmetic operations.
   - Add or subtract days, hours, or minutes from dates/times.
"""

# Importing the datetime module with alias
import datetime as dt
from datetime import timedelta as td

# 1. WORKING WITH DATES
# Getting today's date
current_date = dt.date.today()
print(f"Today's date is: {current_date}")

# Creating a custom date
custom_date = dt.date(2024, 1, 15)
print(f"Custom date: {custom_date}")

# Extracting components of a date
print(f"Year: {current_date.year}, Month: {current_date.month}, Day: {current_date.day}")

# 2. WORKING WITH TIMES
# Creating a custom time
custom_time = dt.time(10, 45, 30)
print(f"Custom time: {custom_time}")

# Extracting components of a time
print(f"Hour: {custom_time.hour}, Minute: {custom_time.minute}, Second: {custom_time.second}")

# 3. WORKING WITH DATE AND TIME
# Getting the current date and time
current_datetime = dt.datetime.now()
print(f"Current datetime: {current_datetime}")

# Creating a custom datetime
custom_datetime = dt.datetime(2024, 12, 22, 14, 30, 0)
print(f"Custom datetime: {custom_datetime}")

# 4. FORMATTING AND PARSING
# Formatting the current datetime as a string
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print(f"Formatted datetime: {formatted_datetime}")

# Parsing a string into a datetime object
date_str = "22-12-2024 14:30:00"
parsed_datetime = dt.datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print(f"Parsed datetime: {parsed_datetime}")

# 5. TIME DELTA OPERATIONS
# Adding 10 days to the current date
future_date = current_date + td(days=10)
print(f"Future date: {future_date}")

# Subtracting 5 hours from the current datetime
past_time = current_datetime - td(hours=5)
print(f"Past datetime: {past_time}")

# Calculating the difference between two dates
difference = future_date - current_date
print(f"Difference: {difference.days} days")