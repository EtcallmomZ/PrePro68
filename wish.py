"""aung wish"""
def main():
    """wish"""
    thing = ""
    x = int(input())
    if x >= 1000000:
        thing += "BYD SEAL"
    elif x >= 100000:
        thing += "Capybara"
    elif x >= 50000:
        thing += "Huawei Matebook X Pro (Harmony OS Next)"
    elif x >= 35000:
        thing += "Nvidia Geforce RTX5070Ti"
    elif x >= 30000:
        thing += "Xiaomi 15 Pro"
    elif x >= 25000:
        thing += "Luxury meal"
    elif x >= 1:
        thing += "Gold Coin or Huawei Watch"
    elif not x:
        print("P'Aung is unemployed, so he plans to apply for the Taiwan Government " \
        "Scholarship (MOE) to pursue a Master's degree instead.")
    else:
        print("Invalid Input")
    if x >= 1:
        print(f"For a salary of {x:,} Baht, P'Aung will buy a {thing}.")
main()
