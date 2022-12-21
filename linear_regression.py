import numpy as np
import pandas
from sklearn import linear_model
from sklearn. import train_test_spilt
from sklearn.datasets import load_boston
boston = load_boston()
df_x=pandas.DataFrame(boston.data,columns=boston.feature_names)
df_y=pandas.DataFrame(boston.target)
df_x.describe()
reg=linear_model.LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
reg.fit(x_train,y_train)
a=reg.predict(x_test)
a



