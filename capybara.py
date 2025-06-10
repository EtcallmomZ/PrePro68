"""secret"""
X = float(input())
Y = float(input())
Z = float(input())
B = int(input())
if 155 <= X <= 165:
    if 22 <= Y <= 24:
        if  34 <= Z <= 36:
            if not B % 2 :
                print("\"Yes, This is a capybara star.\"")
            else :
                print("\"No, This isn't a capybara star.\"")
        else :
            print("\"No, This isn't a capybara star.\"")
    else :
        print("\"No, This isn't a capybara star.\"")
else :
    print("\"No, This isn't a capybara star.\"")
