"""Essay 300 Words"""
def main():
    """main"""
    essay = input()
    if len(essay) >= 300:
        print("Essay is 300 characters or more.")
    else:
        print("Please write more.")
main()
