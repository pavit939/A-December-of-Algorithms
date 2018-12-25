print("Enter your choice:")
print("1-With Tolerence \n2-Without Tolerence")
i = int(input())
def IsApproximatelyEqual1(x,y):
    a = round(x,2)
    b = round(y,2)
    if(a == b):
        return 1
def IsApproximatelyEqual2(x,y,tol):
    sub = abs(round(x - y,2))
    if(sub == tol):
        return 1
    print(sub)
def switch(i):
    if(i == 1):
        x = float(input("Enter number 1:"))
        y = float(input("Enter number 2:"))
        tol = float(input("Tolerance Level:"))
        
        if(IsApproximatelyEqual2(x,y,tol) == 1):
            print("True")
        else:
            print("False")
    if(i == 2):
        x = float(input("Enter number 1:"))
        y = float(input("Enter number 2:"))
        if(IsApproximatelyEqual1(x,y) == 1):
            print("True")
        else:
            print("False")
    if(i!=1 and i!=2):
        print("Enter a valid input!!")
        
switch(i)
