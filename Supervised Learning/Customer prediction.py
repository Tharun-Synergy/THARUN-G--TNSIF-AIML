import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.DataFrame({
    'Age': [20,22,25,28,30,32,35,38, 40, 45],
    'Income': [15000,18000,22000, 30000,35000,
               40000,45000,50000, 55000, 60000],
    'Purchased': [0,0,0,1,1,1,1,1,1,1]
})
X=df[['Age','Income']]
y=df['Purchased']
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=42)
logistic_model = Pipeline([('scaler',StandardScaler()),('classifier',LogisticRegression())])
logistic_model.fit(X_train, y_train)
logistic_pred=logistic_model.predict(X_test)
logistic_accuracy=accuracy_score(y_test, logistic_pred)
tree_model =DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
tree_pred=tree_model.predict(X_test)
tree_accuracy= accuracy_score(y_test, tree_pred)
new_customer = pd.DataFrame({
    'Age': [27],
    'Income': [28000]
})
logistic_new=logistic_model.predict(new_customer)
tree_new=tree_model.predict(new_customer)
print("Logistic Regression Accuracy:",f"{logistic_accuracy:.2%}")
print("Decision Tree Accuracy:",f"{tree_accuracy:.2%}")
print("\nNew Customer Prediction:")
print("Logistic Regression:",logistic_new[0])
print("Decision Tree:",tree_new[0])
