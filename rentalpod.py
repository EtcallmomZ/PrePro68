"""Rental Pod"""
def main():
    """input"""
    x = input()
    y = input()
    z = input()
    result = ""
    if x == "Yes":
        x = True
    else:
        result += "No ability information." + "\n"
        x = False
    if y == "Yes":
        y = True
    else:
        result += "Owner's confirmation is required." + "\n"
        y = False
    if z == "Yes":
        z = True
    else:
        result += "The owner's ability must be alive." + "\n"
        z = False

    if (x and y and z) is True:
        print("Ability successfully added to Rental Pod.")
    else:
        print(result,end = "")
        print("Unsuccessful to add Ability.")
main()
