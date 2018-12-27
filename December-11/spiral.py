def printsp(er,ec,a):
    sr = 0 
    sc = 0 
    while (sr < er and sc < ec):
        for i in range(sr,ec):
            print(a[sr][i],"-->",end=" ")
        sr = sr + 1
        for i in range(sr,er):
            print(a[i][ec - 1],"-->",end=" ")
        ec = ec - 1
        if (sc < er and sc < ec):
            for i in range(ec - 1,sc - 1,-1):
                print(a[er - 1][i],"-->",end=" ")
            er = er - 1
            for i in range(er - 1,sr - 1,-1):
                print(a[i][sc],"-->",end=" ")
            sc = sc + 1
def main():
    n = int(input("Enter the number of rows and columns in for a matrix:"))
    m = [[0] * n for i in range(n**n)]
    for i in range (n):
        for j in range(n):
            m[i][j]=int(input())
    printsp(n,n,m)
main()
