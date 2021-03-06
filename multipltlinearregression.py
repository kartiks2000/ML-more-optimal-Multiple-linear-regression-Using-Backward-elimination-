# Multiple Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("50_Startups.csv")

x = dataset.iloc[:,:4].values
y = dataset.iloc[:,4].values


# Encoding categorical data and also implementing dummy vairiable

# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))



# Avoiding Dummy Vairiable Trap
# We know that there are dummy vairiable column at index 0,1,2 to avoid dummy trap we need to remove any one of the dummy vairiable column hence we are removing the column 0
# Although the linear regression liberary take care of the dummy trap so we dont need to this manually but we did it to remind our self about dummy variable trap 
x = x[:,1:]


# We dont need to take care of the feature scaling manually as the liberary is taking care of it automatically.


# Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)



# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)



# Predicting the Test set result
y_pred = regressor.predict(x_test)



# This model is trained using ALL-IN Method hence its not so accurate
# This model is not the most optimal we can make it more accurate by using the BACKWARD ELIMNATION METHOD


# ------------------------------- BACKWARD ELIMINATION --------------------------------------

# Building more optimal model using BACKWARD ELIMINATION

import statsmodels.api as sm
# Preparing for Backward elimination method
# PROBLEM-: Unlike the other liberaries the above liberary does not consider the constant b0 so we need to add column of ones(1's) in the start of array X
# Also known as adding of "Intercept"
x = np.append(arr = np.ones((50,1)).astype(int), values = x, axis = 1)


# Emplementing Backward elimination
# We need to create a new matrix of features which will be our optimal matrix of feature, at last it will only contain the optimal team of features(colums) that are statistically significant and other columns/features will be neglected 
# we need to specify the index of all indipendent variable/column in the dataset
#x_opt = x[:,[0,1,2,3,4,5]]
x_opt = np.array(x[:, [0, 1, 2, 3, 4, 5]], dtype=float)
# now we need to make a new regressor
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
# The next line processes the model and gives us information about our regression model, it also gives the p-values 
# Now we can compare the p-values and decide which variable has to be removed
print(regressor_OLS.summary())
# After comparing we can see that we need to remove column at 2nd Index


# We again need to update the regressor by removing column at index 2
x_opt = np.array(x[:, [0, 1, 3, 4, 5]], dtype=float)
# now we again need to make a new regressor
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
# The next line processes the model and gives us information about our regression model, it also gives the p-values 
# Now we can compare the p-values and decide which variable has to be removed
print(regressor_OLS.summary())

# We need to follow this until we get the optimal model

# We again need to update the regressor by removing column at index 1
x_opt = np.array(x[:, [0, 3, 4, 5]], dtype=float)
# now we again need to make a new regressor
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
# The next line processes the model and gives us information about our regression model, it also gives the p-values 
# Now we can compare the p-values and decide which variable has to be removed
print(regressor_OLS.summary())


# We again need to update the regressor by removing column at index 4
x_opt = np.array(x[:, [0, 3, 5]], dtype=float)
# now we again need to make a new regressor
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
# The next line processes the model and gives us information about our regression model, it also gives the p-values 
# Now we can compare the p-values and decide which variable has to be removed
print(regressor_OLS.summary())


# We again need to update the regressor by removing column at index 5
x_opt = np.array(x[:, [0, 3]], dtype=float)
# now we again need to make a new regressor
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
# The next line processes the model and gives us information about our regression model, it also gives the p-values 
# Now we can compare the p-values and decide which variable has to be removed
print(regressor_OLS.summary())

# This is our required optimal model.







