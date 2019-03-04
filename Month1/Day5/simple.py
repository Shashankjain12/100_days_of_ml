#! usr/bin/python
"""
    Author:Shashank Jain
    github:Shashankjain12
"""

# Step 1. Involves Getting the datasets

# Step 2. Importing the Important Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
# Step 3. Importing our Dataset
#I will be using dummy dataset for these purposes thanks to https://machinelearningmastery.com/standard-machine-learning-datasets/

dataset=pd.read_excel("data.xls")

# Step 4. Separating the data into dependant and independant variables

X=dataset.iloc[:, 0].values

y=dataset.iloc[:, 1].values

#Step 5. Removing the missing data if any 
# As this have no missing data so skipping this part
""" 
    imputer=Imputer(missing_values='NAN',strategy='mean',axis=0)
    missing values-->values which are not there
    strategy-->how to remove those missing values
    axis--> how to put that data row wise or column wise
    imputer.fit(X[:,:-1])
    X[:,:-1]=imputer.transform(X[:,:-1])
"""
# Step 6. Categorical Data-Label Encoding
"""
    labelencoder is for values that are not numeric as our data is fully numeric
    so leaving this part.
    labelencoder_X=LabelEncoder()
    X[:,0]=labelencoder_X.fit_transform(X[:,0])
    But problem of dummy encoding is arised so removing that too.
    onehotencoder=OneHotEncoder(categorical_features=[0])//specidies which value
    to encode
    X=onehotencoder.fit_transform(X).toarray()
    labelencoder_y=LabelEncoder()
    y=labelencoder.fit_transform(y)
"""
# Step 7. Splitting the data into training and test set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
X_train=X_train.reshape(1,-1)
y_train=y_train.reshape(1,-1)

# Step 8. Feature Scaling
""" 
    To make values of X and Y on the same scale to avoid dependancy on one 
    feature more than other

sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
"""
regressor=LinearRegression()

regressor.fit(X_train,y_train)
#y_pred=regressor.predict(X_test)

plt.scatter(X_train,y_train,color="red")

plt.plot(X_train[0],regressor.predict(X_train)[0],color="red")

plt.title("X vs Y")

plt.show()

plt.scatter(X_test,y_test,color="red")

plt.plot(X_train[0],regressor.predict(X_train)[0])

plt.title("Xtest vs Ytest")

plt.show()