from sklearn.linear_model import LinearRegression

x=[[1],[2],[3],[4],[5],[6],[7],[8]]
y=[20000,25000,30000,35000,40000,45000,50000,55000]

model=LinearRegression()
model.fit(x,y)
prediction=model.predict([[5]])
print("predicted Salary :",prediction)
