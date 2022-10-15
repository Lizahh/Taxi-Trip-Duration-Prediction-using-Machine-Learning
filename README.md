# Taxi-Trip-Duration-Prediction-using-Machine-Learning

<h3> The aim of this project is to predict the total ride duration of taxi trips in New York City.  </h3> 
<p> Almost all of us have used an Ola or Uber at some point or another to get a ride. Ride-hailing services link local drivers and passengers utilising their personal automobiles through online-enabled platforms. They are often a convenient means of door-to-door transportation. Typically, they are less expensive than utilising authorised taxicabs.
Predicting the duration of a driver's cab occupancy is crucial for optimising the effectiveness of taxi dispatching systems for such services. A dispatcher would be better equipped to choose which driver to assign to each pickup request if they knew roughly when a taxi driver would finish their current trip. </p> 

# Install

### 1) Clone the repository:

          git clone https://github.com/Lizahh/Taxi-Trip-Duration-Prediction-using-Machine-Learning
          
### 2) Istall the requirements:

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 

          
          
### 3) Download the Dataset:
          https://github.com/Lizahh/Taxi-Trip-Duration-Prediction-using-Machine-Learning/releases/tag/%23dataset
      
# Description

The project code is provided in the `Taxi trip duration prediction.ipynb` notebook file. You will also be required to use the included `nyc_taxi_trip_duration.csv` dataset file to complete your work which you can find in the release section of the repository. You can download the `taxi_trip_duration_prediction.py` file to play with the code as much you feel. Note that the code included in `Taxi trip duration prediction.ipynb` is meant to be used out-of-the-box and not intended for students to manipulate. If you are interested in how the results are achieved in the notebook, please feel free to explore this Python file.

# Run

In a terminal or command window, navigate to the top-level project directory `Taxi-Trip-Duration-Prediction-using-Machine-Learning/` (that contains this README) and run one of the following commands:

```bash
ipython notebook Taxi trip duration prediction.ipynb
```  
or
```bash
jupyter notebook Taxi trip duration prediction.ipynb
```
or open with Jupyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

# Data

The modified NYC Taxi Trip Duration dataset consists of 729323 data points, with each datapoint having 11 features. This dataset is a modified version of the Taxi Trip Duration dataset found on the [Kaggle](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data).

### **Features**

1. `id` : a unique identifier for each trip. This is a nominal data column.

2. `vendor_id` : a code indicating the provider associated with the trip record.This is a nominal data column.

3. `pickup_datetime` : the date and the time when the ride started.

4. `dropoff_datetime` : the date and time when the ride ended

5. `passenger_count` : the number of passengers in the vehicle (driver entered value)

6. `pickup_longitude` : date and time when the meter was engaged

7. `pickup_latitude` : date and time when the meter was disengaged

8. `dropoff_longitude` : the longitude where the meter was disengaged

9. `dropoff_latitude` : the latitude where the meter was disengaged

10. `store_and_fwd_flag` : This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server (Y=store and forward; N=not a store and forward trip).This column is categorical

### **Target Variable**

11. `trip_duration`: (target) duration of the trip in seconds

# You might be interested:

* [PyQt5 Crash Course](https://github.com/Lizahh/PyQt5-Crash-Course-with-codes)
* [OPAC (Online Public Access Catalog) Library Management Project with Pure Python](https://github.com/Lizahh/Simplest-Library-Management-System-using-Python-Only)
* [CRUD Operations with MongoDB](https://github.com/Lizahh/CRUD-operations-with-MongoDB)
