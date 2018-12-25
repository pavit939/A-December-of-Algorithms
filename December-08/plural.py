import inflect
p = inflect.engine()
def plural (s,n):
    if(n == 1 and(p.singular_noun(s) == 0)):
        print(s)
    elif(n!=1):
        print(p.plural(s))
    else:
        print(p.plural(s))
s = input("Enter the string:")
n = int(input(f"Enter the number of {s}:"))
plural(s,n)
