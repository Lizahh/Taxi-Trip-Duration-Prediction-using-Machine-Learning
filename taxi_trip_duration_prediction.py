# -*- coding: utf-8 -*-
"""
Project - Taxi trip duration prediction.ipynb

"""
# importing required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# reading the data
data = pd.read_csv('nyc_taxi_trip_duration.csv')

# first five rows of the data
data.head()

# columns in the dataset
data.columns

"""## Description of the variables


<b>id</b> : a unique identifier for each trip. This is a <b>nominal</b> data column.

<b>vendor_id</b> :  a code indicating the provider associated with the trip record.This is a <b>nominal</b> data column.

<b>pickup_datetime</b> : the date and the time when the ride started.

<b>dropoff_datetime</b> : the date and time when the ride ended

<b>passenger_count</b> : the number of passengers in the vehicle (driver entered value)

<b>pickup_longitude</b> : date and time when the meter was engaged

<b>pickup_latitude</b> : date and time when the meter was disengaged

<b>dropoff_longitude</b> : the longitude where the meter was disengaged

<b>dropoff_latitude</b> : the latitude where the meter was disengaged

<b>store_and_fwd_flag</b> : This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server (Y=store and forward; N=not a store and forward trip).This column is categorical

<b>trip_duration</b> :  (target) duration of the trip in seconds
"""

# shape of the data
data.shape

# statistics of the numerical features in the data
data.describe()

# overview of type of variables
data.dtypes

# checking the missing values in the dataset
data.isnull().sum()

# looking at the longest trips
print('Longest 5 trip duration: \n {} '.format(data['trip_duration'].nlargest(5)))
print('\nThe the number of rows with 0 as their trip duration values is {}'.format(len(data[data['trip_duration']==1 ])))

# There is 1 record with extremely large value of 1939736 and 13 with 0 seconds each. We can drop these rows.

# dropping the outliers
data=data[data.trip_duration!=data.trip_duration.max()]
data=data[data.trip_duration!=data.trip_duration.min()]

# converting the date time variables to datatime format
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])
data['dropoff_datetime'] = pd.to_datetime(data['dropoff_datetime'])

# creating datetime features
data['pickup_day']=data['pickup_datetime'].dt.day_name()
data['dropoff_day']=data['dropoff_datetime'].dt.day_name()
data['pickup_month']=data['pickup_datetime'].dt.month
data['dropoff_month']=data['dropoff_datetime'].dt.month

# columns of the data
data.columns

# dropping the variables which might not be helpful to predict the trip duration
data = data.drop(['id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude',
       'dropoff_longitude', 'dropoff_latitude'], axis=1)

# converting the categorical variables to numerical variables
data = pd.get_dummies(data)

# separating dependent and independent variables
X = data.drop(['trip_duration'], 1)
y = data['trip_duration']

# creating a training and validation set
x_train, x_valid, y_train, y_valid = train_test_split(X, y, test_size = 0.25, random_state=10)

"""## Linear Regression Model"""

# creating the model
lreg = LinearRegression()

# training the model
lreg.fit(x_train, y_train)

# rmse on training set
pred_train = lreg.predict(x_train)
rmse_train = np.sqrt(mean_squared_error(y_train, pred_train))
rmse_train

# rmse on validation set
pred_val = lreg.predict(x_valid)
rmse = np.sqrt(mean_squared_error(y_valid, pred_val))
rmse