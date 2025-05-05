print("Welcome to Treasure Island.Your mission is to find the treasure")
choice = input("left or right? l for left and r for right")
if choice == "l":
    ask = input("swim or wait")
    if ask == "wait":
        door = input("which door?")
        if door == "yellow":
            print("you win!")
        elif door == "red":
            print("Burned by fire.Game Over")
        elif door == "blue":
            print("Eaten by beasts.Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over")
else:
    print("Fall into a hole.Game Over")



