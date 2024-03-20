# HW2_P1: Nested Decisions: The Adventure Game 🏰

# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")


# Task 2: Setting the Scene
'''
Based on the corrected code from Task 1, expand the game. If the user 
chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", 
and provide outcomes for each decision.
'''

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You have unlocked secret passage!")


# Task 3: Default Path
'''
If the user makes an invalid choice at any point, use the pass statement for now. 
Later, you can enhance this to provide feedback or a different branch of the story.
'''

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You have unlocked secret passage!")
    else:
        pass
else:
    pass
