def vowels(l1):
    listone=len(l1)
    flag=0
    for i in range(listone - 1):
        listtwo=len(l1[i])
        for l in range(listtwo - 1):
            if l1[i][l] in 'aeiou' and l1[i][l+1] in 'aeiou' and l1[i+1][l] in 'aeiou' and l1[i+1][l+1] in 'aeiou':
                print(i,'==',l)
                flag=1
    if(flag==0):
        print("Unavailable")
str=input("String:")
vowels(str.split())
