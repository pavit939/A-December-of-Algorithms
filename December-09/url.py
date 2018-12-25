def https(s):
    if(s[0:8]=="https://"):
        return '1'
    else:
        return '0'
def url(s):
    if (".com" in s or ".net" in s or ".org" in s or ".in" in s):
        return "1"
    else :
        return '0'
s = input("Enter the string to check if it is an URL")
c = https(s)
if c =='1':
    u = url(s)
    if u =='1':
        print(f"{s} is an URL")
    else:
        print(f"{s} is not an URL")
else:
    print(f"{s} is not an URL")
