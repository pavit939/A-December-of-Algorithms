def hash(str):
    l = []
    for i in str:
        l.append(ord(i))
    a = sum(l)
    print(a / len(str))
str = input("Enter a string:")
hash(str)
