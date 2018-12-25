n = int(input("Enter a no:")) 
a = 0
b = 1

print("The fibonacci series is:")

for i in range (n):
    print(a)
    c = a + b
    a = b
    b = c