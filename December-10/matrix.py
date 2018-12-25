n = int (input("Enter number of rows and columns:"))
arr = [ ]

import numpy as np
for i in range(n):
        for j in range(n):
                b = int (input("Enter the element:"))
                arr.append(b)
                
p=np.array(arr).reshape(n,n)
print(p)
d = np.linalg.det(p)
print(d)
