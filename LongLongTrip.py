'LongLongTrip'

x = input()
y = int(input())

C = x.find('C')
P = x.find("P")
r = abs(P - C)

if r <= y:
    print("Possible")
else :
    print("Impossible")
