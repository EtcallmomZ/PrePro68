"""Longest Stick"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())

    max_val = max(a, b, c, d, e, f, g)
    for i in range(max_val, 0, -1):
        space = (i - 1) * " "
        print(space + "*")
main()
