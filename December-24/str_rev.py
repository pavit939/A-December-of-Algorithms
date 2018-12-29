def strrev(string,str,len):
    if(len!=0):
        str = str + string[len]
        strrev(string,str,len-1)
    else:
        print("The reversed string is:{}".format(str))
def main():
    string = input("Enter string:")
    str =" "
    l1 = len(string)
    strrev(string,str,l1-1)
main()
