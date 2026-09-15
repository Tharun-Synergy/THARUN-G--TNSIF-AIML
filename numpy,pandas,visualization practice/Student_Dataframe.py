import pandas as pd
data = {
    "Name": ["Abdul", "Bhagavath", "Jersush Raj", "Sanjeevi kumar", "Yogeshwaran", "Sriram", "Naveen", "Vishwa Kumar"],
    "Department": ["CSE", "AIDS", "CSE", "IT", "AIDS", "CSE", "IT", "AIDS"],
    "Marks": [85, 72, 91, 68, 78, 88, 74, 95],
    "Attendance": [90, 85, 95, 75, 82, 78, 88, 70]
}
df = pd.DataFrame(data)

print("Student DataFrame:","\n",df)
print("\nFirst 5 students:","\n",df.head(5))
print("\nAverage Marks:","\n",df["Marks"].mean())
print("\nStudents who scored more than 75:","\n",df[df["Marks"] > 75])
print("\nStudents whose attendance is below 80%:","\n",df[df["Attendance"] < 80])
print("\nStudents sorted based on marks:","\n",df.sort_values("Marks"))
