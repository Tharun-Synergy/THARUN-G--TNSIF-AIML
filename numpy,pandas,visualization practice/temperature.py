import numpy as np

temp_Arr=np.array([30,38,40,29,36,42,37])
print("\n","AVG temperature: ",np.mean(temp_Arr))
print("\n","Max temperature: ",np.max(temp_Arr))
print("\n","Min tempertaure: ",np.min(temp_Arr))
print("\n","Above 30 tempertaure:",temp_Arr[temp_Arr>30])
updated_Temperature=temp_Arr+2
print("\n","+2 temprature arr: ",updated_Temperature)
