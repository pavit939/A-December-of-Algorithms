string = input("Enter the word:")
n = int(input("Enter the number:"))
arr =[]
for i in string:
    print(chr(ord(i)+n),end='')
