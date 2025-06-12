"""Wildlife"""
def main():
    """main"""
    turtle = int(input())
    ribbit = int(input())
    tiger = int(input())
    deer = int(input())
    check_min = min(turtle, ribbit, tiger, deer)
    print(f"The slowest animal has a speed of: {check_min} km/h")
main()
