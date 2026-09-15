import matplotlib.pyplot as plt
students = ["Abdul","Bhagavath","Jersush","Sanjeevi","Yogeshwaran",
            "Sriram", "Naveen", "Vishwa", "Arun", "Priya"]
marks = [85,72,91,38,78,88,55,32,67,95]
# Bar chart
plt.bar(students,marks)
plt.title("Student Python Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
# Performance categories
excellent = 0
good = 0
average = 0
needs_improvement = 0

for mark in marks:
    if mark >=80:
        excellent+= 1
    elif mark >=60:
        good +=1
    elif mark >= 40:
        average +=1
    else:
        needs_improvement +=1
# Pie chart
categories = ["Excellent","Good","Average","Needs Improvement"]
values = [excellent, good, average, needs_improvement]

plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.title("Student Performance Distribution")
plt.show()
