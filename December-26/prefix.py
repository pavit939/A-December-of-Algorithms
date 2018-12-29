n = input("Enter Strings:")
a = n.split()
pre_len = len(a[0])
for x in a[1 : ]:
    pre_len = min(pre_len, len(x))
    while not x.startswith(a[0][ : pre_len]):
        pre_len = pre_len - 1
pre = a[0][ : pre_len]
print("The prefix element is {}".format(pre))
