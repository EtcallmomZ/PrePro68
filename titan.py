"""titan"""
def main():
    """what"""
    x = int(input())
    y = int(input())
    z = input()
    if z != "Yes" :
        print("Training Corps")
    elif (y >= 7 ) or (x >= 80 and y > 5):
        print("Scout Regiment")
    elif (x >= 90 and y > 1 ) or (x >= 80 and y > 1):
        print("Military Police Regiment")
    elif z == "Yes":
        print("Garrison Regiment")
    else:
        print("Training Corps")

main()
