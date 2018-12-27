str = input("Enter a string:")
def lexico(s):
    x = sorted(s)
    n = len(x) - 1
    while True:
        yield ''.join(x)
        for i in range(n-1, -1, -1):
            if x[i] < x[i + 1]:
                break
        else:
            return
        v = x[i]
        for j in range(n, i, -1):
            if v < x[j]:
                break
        x[i], x[j] = x[j], x[i]
        x[i+1:] = x[i+1:][::-1]
for s in lexico(str):
    print(s)
