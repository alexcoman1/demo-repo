answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
    answer = input("You reach a crossroads, would you like to go left or right?").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack.")
        if answer == "attack":
            print("That was not the greatest idea, you lost!")
        else:
            print("Good choice, you made it away safely.")

            answer = input("You see a car and a plane. Which would you like to take? (car/plane)")

            if answer == "plane":
                print("Unfortunately you do no know how to fly a plane.. game over")
            else:
                print("You won!")

    elif answer == "right":
        print("You walk aimlessly to the right and fall on a patch of ice. You injure your leg and cannot continue. Game over!")

    else:
        print("Invalid choice, you lost!")



else:
    print("That's too bad!")