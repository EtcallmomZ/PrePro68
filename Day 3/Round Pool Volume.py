"""Round Pool Volume"""
import math
def main():
    """main"""
    d = int(input())
    high = int(input())
    if d <= 0 or high <= 0:
        print("The values must be positive numbers only.")
    else:
        r = d / 2
        area1 = math.pi * (r ** 2)
        area2 = math.pi * (r ** 2) * high
        area3 = round(area2 * 1000)
        print(f"This circular pool has a surface area of {area1:,.2f} square meters.")
        print(f"It requires about {area2:,.2f} cubic meters of water.")
        print(f"Which is approximately {area3:,} liters.")
main()
