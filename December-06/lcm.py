x = int(input("Enter 1:"))
y = int(input("Enter 2:"))
product = (x * y)
n = 1000
a = [ ]
b = [ ]

for i in range(1,n):
    if x % i == 0:
        a.append(i)
for j in range(1,n):
    if y % j == 0:
        b.append(j)
if(set(a) and set(b)):
    cmn = (set(a) & set(b))
    gcd = (max(cmn))
    
lcm = product // gcd    

print(lcm)
