# -*- coding: utf-8 -*-
"""wine quality prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14AqRmNGzgSZe8xDXgBd5harMpzhWnzD7

Import Library
"""

import pandas as pd
import numpy as np

"""import data"""

df = pd.read_csv('https://raw.githubusercontent.com/YBIFoundation/Dataset/main/WhiteWineQuality.csv',sep=';')

"""Describe data"""

df.head()

df.info()

df.describe()

df.columns

df.shape

"""Data visualization"""

df['quality'].value_counts()

df.groupby('quality').mean()

"""Define Target Variable (y) and Feature Variables (X)"""

y=df['quality']

y.shape

y

x=df[['alcohol','density','chlorides','fixed acidity','pH','residual sugar','sulphates','volatile acidity','citric acid','free sulfur dioxide','total sulfur dioxide']]

x=df.drop(['quality'],axis=1)

x.shape

x

"""Model evaluation"""

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()

x=ss.fit_transform(x)

x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,stratify=y,random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.svm import SVC
svc=SVC()

svc.fit(x_train,y_train)

y_pred=svc.predict(x_test)
y_pred.shape

y_pred

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

y=df['quality'].apply(lambda y_value:1 if y_value>=6 else 0)

y.value_counts()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,stratify=y,random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.svm import SVC
svc=SVC()
svc.fit(x_train,y_train)

y_pred=svc.predict(x_test)

y_pred.shape

y_pred

"""prediction"""

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

df_new=df.sample(1)

df_new

df_new.shape

x_new=df_new.drop(['quality'],axis=1)

x_new=ss.fit_transform(x_new)

y_pred_new=svc.predict(x_new)

y_pred_new