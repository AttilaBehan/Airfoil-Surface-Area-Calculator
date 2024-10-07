import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

#Handling data from airfoil tool file
data=[]
setter=0
x=[]
y_upper=[]
y_lower=[]
with open(r"filename") as file:
    for i in file:
        if "upper" in i:
            setter=True
            continue
        if "lower" in i:
            setter=False
            continue
        initdata=i.replace('\n','').replace(',',' ').split()
        initdata=[i for i in initdata if i!='']
        print(i)
        if initdata!=['', ''] and initdata!=[''] and initdata!=[]:
            if setter==True:
                x.append(float(initdata[0]))
                y_upper.append(float(initdata[1]))
            if setter==False:
                y_lower.append(float(initdata[1]))
y_upper=np.array(y_upper)
y_lower=np.flip(np.array(y_lower))
num=-min(y_lower)
for i in range(len(y_lower)):
    y_lower[i]+=num
    y_upper[i]+=num

import pandas as pd
df=pd.DataFrame()
df["x"]=x
df["y_upper"]=y_upper
df["y_lower"]=y_lower
print(df)
area=np.trapezoid(-y_upper+y_lower,x)/(10**6)
print(area)

plt.plot(x, y_upper, label='Upper Surface')
plt.plot(x, y_lower, label='Lower Surface')
plt.fill_between(x, y_lower, y_upper, color='lightgray', alpha=0.5, label='Enclosed Area')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Airfoil Area = {area:.4f} m^2')
plt.legend()
plt.grid(True)
plt.show()
