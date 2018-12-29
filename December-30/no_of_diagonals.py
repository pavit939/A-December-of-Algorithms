def no_of_diagonals(n):
    v = n*(n-3)/2
    print("Number of diagonals is {} ".format(v))
    
def main():
    n = int(input("Enter the number of vertex:"))
    no_of_diagonals(n)
main()
