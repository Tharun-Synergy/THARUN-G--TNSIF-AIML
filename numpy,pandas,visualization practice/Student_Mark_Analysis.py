import numpy as np
marks = np.array([[85, 78],[72, 80],
                  [90, 95],[68, 70],
                  [77, 85],[95, 92],
                  [81, 79],[74, 76],
                  [88, 90],[69, 72]])
total = np.sum(marks, axis=0)
average = np.mean(marks, axis=0)
highest = np.max(marks, axis=0)
lowest = np.min(marks, axis=0)

for i in range(2):
    print("\n", "subjects ",i+1)
    print("Total Marks:", total[i])
    print("Average Marks:", average[i])
    print("Highest Marks:", highest[i])
    print("Lowest Marks:", lowest[i])
    print("Marks greater than 75:", marks[marks[:, i] > 75, i])
