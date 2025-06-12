'Palindrome'

text = input()
x = text.lower()
NEW = x[::-1]


if x == NEW :
    print("Yes")
else:
    print("No")
