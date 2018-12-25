x = input("Enter the number")
y = int(x)
l = "left"
r = "right"
m = "middle"

def tower(n,l,m,r):
    if n ==1:
        print(l,"=>",r)
    else:
        t(n-1,l,r,m)
        print(l,"=>",r)
        t(n-1,m,l,r)
tower(y,l,m,r)

