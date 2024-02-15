# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:21:30 2024

@author: Shubham Goswami
"""

import pandas as pd
### The columns in xlsx file are:
### RAINDATE	RAINTIME	      RAIN
### 24-03-15	15:15:00+05:30	0
### 24-03-15	15:30:00+05:30	0


# Load the Excel file
df = pd.read_excel("rain_15min.xlsx",sheet_name="trial")

# Convert RAINDATE and RAINTIME columns to datetime format
df['RAINDATE'] = pd.to_datetime(df['RAINDATE'] + ' ' + df['RAINTIME'].str.split('+').str[0], format='%d-%m-%y %H:%M:%S')

# df['RAINDATE1'] = pd.to_datetime(df['RAINDATE'] + ' ' + df['RAINTIME'].str.split('+').str[0])


# Extract date and time separately
df['DATE'] = df['RAINDATE'].dt.date
df['TIME'] = df['RAINDATE'].dt.time

# Filter the data to get only the records corresponding to 8:30:00 each morning
morning_rainfall = df[df['TIME'] == pd.to_datetime('08:30:00').time()]

# Assign these rainfall values to the previous date
morning_rainfall['DATE'] = morning_rainfall['DATE'] - pd.Timedelta(days=1)

morning_rainfall['YEAR'] = morning_rainfall['RAINDATE'].dt.year
morning_rainfall['MONTH'] = morning_rainfall['RAINDATE'].dt.month

monthly_rainfall = morning_rainfall.groupby(['YEAR', 'MONTH'])['RAIN'].sum().reset_index()
monthly_rainfall.to_excel("monthly_rainfall_data.xlsx", index=True, header=['Monthly Rainfall'])


monthly_rainfall.to_excel("monthly_rainfall_data.xlsx", index=True, header=['Monthly Rainfall'])

# Optionally, you can save the updated dataframe to a new Excel file
# df.to_excel("updated_rainfall_data.xlsx", index=False)
