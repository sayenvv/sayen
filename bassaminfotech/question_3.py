def convert(string):
    if string.islower()==True:
        x=string.upper()
        return x
    else:
        x=string.lower()
        return x
string = input("enter the string:")
print(convert(string))