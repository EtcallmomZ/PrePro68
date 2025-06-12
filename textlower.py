'TextLower'

x = input()

if (x.isalpha()) is False :
    print("The text contains non-alphabetic characters")
else :
    print(f"Result: {x.casefold()}")
    