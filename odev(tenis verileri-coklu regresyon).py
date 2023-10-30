#veri önişleme
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler=pd.read_csv('tenis_veriler.csv')
print(veriler)

from sklearn import preprocessing
veriler2=veriler.apply(preprocessing.LabelEncoder().fit_transform)

c=veriler2.iloc[:,:1]

from sklearn import preprocessing
ohe=preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()
print(c)

havadurumu=pd.DataFrame(data=c,index=range(14),columns=['o','r','s'] )
sonveriler=pd.concat([havadurumu,veriler.iloc[:,1:3]],axis=1)
sonveriler=pd.concat([veriler2.iloc[:,-2:],sonveriler],axis=1)

#veri önişleme bitiş
#linear regression yöntemi

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(sonveriler.iloc[:,:-1],sonveriler.iloc[:,-1:],test_size=0.33,random_state=0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

import statsmodels.api as sm 

X = np.append(arr = np.ones((14,1)).astype(int), values=sonveriler.iloc[:,:-1], axis=1 )
X_l = sonveriler.iloc[:,[0,1,2,3,4,5]].values
r_ols = sm.OLS(endog = sonveriler.iloc[:,-1:], exog =X_l)
r = r_ols.fit()
print(r.summary())

sonveriler=sonveriler.iloc[:,1:]

import statsmodels.api as sm 

X = np.append(arr = np.ones((14,1)).astype(int), values=sonveriler.iloc[:,:-1], axis=1 )
X_l = sonveriler.iloc[:,[0,1,2,3,4]].values
r_ols = sm.OLS(endog = sonveriler.iloc[:,-1:], exog =X_l)
r = r_ols.fit()
print(r.summary())



x_train=x_train.iloc[:,1:]
x_test=x_test.iloc[:,1:]

regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)



