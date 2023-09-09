import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

"""Data Collection and Processing"""

# loading the csv data as a Pandas DataFrame
gold_data = pd.read_csv('/content/gld_price_data.csv')

gold_data.head(5)

gold_data.tail(5)

# num of rows and columns
gold_data.shape

# get basic information about the data
gold_data.info()

# check if there are empty columns
gold_data.isnull().sum()

# get the statistical measure of the data
gold_data.describe()

"""Correlation:"""

correlation = gold_data.corr()

# constructing a heatmap to understand the correlation
plt.figure(figsize = (8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

# correlation value of GLD
print(correlation['GLD'])

# check distribution of the GLD price
sns.displot(gold_data['GLD'], color='green')

"""Splitting the Features and Target"""

X = gold_data.drop(['Date', 'GLD'], axis=1) # make a copy of gold_data, then drop Date and GLD and assign to X
Y = gold_data['GLD'] # assign column GLD to Y

print(X)

print(Y)

"""Splitting into Test Data and Train Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2) # test_size means take 20% of the data and use it for testing. The other 80% will be used for training.

"""Model Training:
Random Forest Regressor
"""

regressor = RandomForestRegressor(n_estimators=100)

# train the model
regressor.fit(X_train, Y_train)

"""Model Evaluation"""

# prediction on Test Data
test_data_prediction = regressor.predict(X_test)
print(test_data_prediction)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

"""Compare the Actual Values and the Predictied Values in a Graph"""

Y_test = list(Y_test)

plt.plot(Y_test, color='blue',  label = 'Actual Value')
plt.plot(test_data_prediction, color='green',  label = 'Predicted Value')
plt.title('Actual Price Vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD price')
plt.legend()
plt.show()
