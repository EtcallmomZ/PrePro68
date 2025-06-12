"""Rebirth Realms"""
def magic_world():
    """magic_world"""
    print("You are reborn in a magical world. Magic flows through your veins!")
    print("Your new world is: Arcane Dominion")

def sci_fi_world():
    """sci_fi_world"""
    print("You awaken in a futuristic tech world, surrounded by spaceships and robots!")
    print("Your new world is: Neon Nexus")

def anime_game_world():
    """anime_game_world"""
    print("You become the protagonist of a cartoon or game, ready for your adventure!")
    print("Your new world is: Pixel Realm")

def wuxia_world():
    """wuxia_world"""
    print("You awaken in a world of martial arts, ancient clans, \
and hidden techniques. The path of the sword awaits you!")
    print("Your new world is: Jianghu Eternal")

def past_with_memory():
    """past_with_memory"""
    print("You return back in time with all your memories. Ready to change your fate!")
    print("You have returned to: Chrono Veil")

def main():
    """main"""
    world = input()
    if world == "1":
        magic_world()
    elif world == "2":
        sci_fi_world()
    elif world == "3":
        anime_game_world()
    elif world == "4":
        wuxia_world()
    elif world == "5":
        past_with_memory()
    else:
        print("You chose no path, and thus the currents of \
fate have carried you to eternal cleansing...")

main()
