def string(main,sub):
    x=main.split(" ")
    for i in x:
        if sub in i:
            new= x.count(sub)
            return new
main = input("enter the main string:")
sub = input("enter the sub string :")
print("find",string(main,sub),"number of ",sub)
