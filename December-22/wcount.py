import sys
import operator
def words(fname,string):
    with open('filename.txt', 'w') as file:
        dict={}
    str1=" "
    for word in string.split():
                if word in dict:
                    dict[word]=dict[word]+1
                else:
                    dict[word]=1
    dict = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    str1=str(dict)
    file.write(str1)
    file.close()
    return dict
def printw(fname,string):
    dict=storewords(fname,string)
    for k in range(0,len(dict)):
        print (dict[k][0], dict[k][1])
    with open('filename.txt', 'r') as file:
        print("In File:")
        for word in file:
            print(word)
def main():
     string=input("Enter the String:")
     fname=input("Enter filename:")
     print_words(filename,string)
main()
