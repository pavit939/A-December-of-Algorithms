def cup_str(n):
    v = n * (n-1) / 2
    print("Number of strings required is:{}".format(v))
def main():
    n=int(input("Enter number of friends:"))
    cup_str(n)
main()
