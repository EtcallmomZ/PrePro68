"""logical"""
def main():
    """something"""
    p = input()
    q = input()
    if p == "True":
        p = 1
    else:
        p = 0
    if q == "True":
        q = 1
    else:
        q = 0
    p = bool(p)
    q = bool(q)
    print(f"p: {p} q: {q}")
    print(f"p ∨ q: {p or q}")
    print(f"p ∧ q: {p and q}")
    print(f"p → q: {(not p)or q }")
    print(f"p ↔ q: {p == q}")
main()
