from sklearn.tree import DecisionTreeClassifier
X = [[0,0],[0,1],[1,1],[1,0],[2,0],[2,1],[0,0],[1,1]]
y = [0, 1, 1, 0, 1, 1, 0, 1]
model = DecisionTreeClassifier()
model.fit(X, y)
prediction = model.predict([[0, 1]])
if prediction[0]== 1:
    print("Play: Yes")
else:
    print("Play: No")
