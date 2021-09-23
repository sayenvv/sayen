def search(a,p):
    if a[-1]>a[-2]:
        if p in a:
            x=a.index(p)
            return x
        else:
            a.append(p)
            a.sort()
            print(a)
            y=a.index(p)
            return y
    else:
        print("invalid array")
a=list(input("create an array:"))
p=input("enter the element to find:")
print(search(a,p))
