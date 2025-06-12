"""Candy Fair"""
import math
def main():
    """main"""
    x = int(input())
    y = int(input())
    if x < y:
        print("Each friend will get: 0 candies")
    else:
        amount = math.floor(x / y)
        print(f"Each friend will get: {amount} candies")
main()
