"""One last move"""
def fire_dragon():
    """fire_dragon"""
    print(f"You used {action}!")
    print("You win! The Demon Lord has been defeated!")

def thunder_blade():
    """thunder_blade"""
    print(f"You used {action}!")
    print("You dealt 250 damage... Not enough. The Demon Lord counterattacks!")

def shadow_fang_slash():
    """shadow_fang_slash"""
    print(f"You used {action}!")
    print("You win! The Demon Lord has been defeated!")

def main():
    """main"""
    print("The Demon Lord is almost defeated!")
    print("You only have enough mana for one final move.")
    if action == "Fire Dragon":
        fire_dragon()
    elif action == "Thunder Blade":
        thunder_blade()
    elif action == "Shadow Fang Slash":
        shadow_fang_slash()
    else:
        print("You hesitated too long... The Demon Lord strikes back!")
        print("You dealt 0 damage... Not enough. The Demon Lord counterattacks!")
action = input()
main()
