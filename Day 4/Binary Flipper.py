"""binary"""
Text = input()
T = " "
for i in Text:
    if i == "0":
        T = T + "1"
    else:
        T = T + "0"
print(T.strip())
