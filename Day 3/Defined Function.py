"""Defined Function"""
def main():
    """main"""
    text = ""
    text = wrapping(text)
    looping(text)
    welcome()

def welcome():
    """welcome"""
    print("Welcome To AIT03, DSBA09, IT23")

def looping(text):
    """looping"""
    print(f"<{text}_> 0")
    print(f"<{text}_> 1")
    print(f"<{text}_> 2")
    print(f"<{text}_> 3")

def wrapping(text):
    """wrapping"""
    text = input()
    return text

main()
