import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
def get_date(product_id):
  data= pd.read_csv('/content/drive/MyDrive/Artificial Inteligent/pluto.csv')
  model_data=data[data['id']==product_id]
  y= model_data['supply'].values
  x= model_data['over'].values.reshape(-1, 1)

  model1 = LinearRegression()
  model1.fit(x, y)
  predictions1 = model1.predict([[1]])

  model2= GaussianNB() 
  model2.fit(x,y)
  predictions2 = model2.predict([[1]])

  model3= DecisionTreeClassifier()
  model3.fit(x,y)
  predictions3 = model3.predict([[1]])

  model2= RandomForestClassifier() 
  model2.fit(x,y)
  predictions4 = model2.predict([[1]])
  
  model2= ExtraTreesClassifier(n_estimators=100) 
  model2.fit(x,y)
  predictions5 = model2.predict([[1]])
  
  model2= LogisticRegression() 
  model2.fit(x,y)
  predictions6 = model2.predict([[1]])
  

  
  average=(predictions1+predictions2+predictions3+predictions4+predictions5+predictions6)/6.0
  retSTR='Linear Regression: '+predictions1 + ' GaussianNB: '+predictions2 +' Decision Tree: '+predictions3 +' Random Forrest: '+predictions4 + ' Extra Trees: '+predictions5 + ' Logistic Regression: '+predictions6 + 'Average: '+average 
  return average
