"""blabla"""
x = input()
y = x.lower()
for i in y:
    if i.isalpha():
        print(f"{ord(i)-96},",end=" ")
    else:
        print(f"{i},",end=" ")
print(x)
