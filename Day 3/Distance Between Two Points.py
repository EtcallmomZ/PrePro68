"""Distance Between Two Points"""
def main():
    """main"""
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
    print(f"{d:.3f}")
main()
