"""CheckBit"""
Bit = input()
B1 = Bit + " "
T1 = ""
for i in B1:
    if i.isspace():
        T2 = T1.strip()
        if T2[0] == T2[-1]:
            print(f"{T2[1:7]}",end=" ")
            T1 = ""
        else:
            T1 = ""
    else:
        T1 += i
