def pascal(n):
    l1 = []
    for line in range(0,n):
        for i in range(0,line + 1):
            l1.append(coeffbi(line,i))
    a = len(l1)
    a = a-n
    while(a < len(l1)):
        j = 0
        for i in range(n-1,-1,-1):
            print(l1[a],"x^",i,"y^",j)
            a = a + 1
            j = j + 1
def coeffbi(n,k):
    result = 1
    if (k > n - k):
        k = n - k
    for i in range(0,k):
        result = result * (n - i)
        result = result // (i + 1)
    return result
def main():
    n =int(input("Enter the number:"))
    pascal(n+1)
main()
