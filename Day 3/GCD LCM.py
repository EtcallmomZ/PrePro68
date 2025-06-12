"""GCD LCM"""
import math
def find_lcm(n1,n2):
    """find_lcm find_gcd"""
    print(math.lcm(n1, n2))

def find_gcd(n1,n2):
    """find_lcm find_gcd"""
    print(math.gcd(n1, n2))

def main():
    """main"""
    x = input()
    if x in ("lcm" , "gcd"):
        n1 = int(input())
        n2 = int(input())
        if x == "lcm":
            find_lcm(n1,n2)
        else:
            find_gcd(n1,n2)
    else:
        print("Invalid input. Please enter 'gcd' or 'lcm'.")

main()
