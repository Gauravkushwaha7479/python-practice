score = 0



while True:
    try:

        user = int(input("Enter the user choice\n"))

        Go_left = 1

        Go_right = 2
        Go_straight = 3
        Quit_game = 4
    except ValueError:
        print("Invalid input. please enter a valid number")
        continue


    if user == Go_left:
        print("you have chosen to go left and you have encontered a monster ")

        action = input("Do you want to fight or run away? (fight/run)\n").lower()

        if action == "fight":
            print("you have chosen to fight the monster and you have won the battle")
            score += 10

        elif action == "run":
            print("you have chosen to run away and you have escaped the monster:")
        else:
            print("Invalid choice. please choose a valid option:")

    elif user == Go_right:
        print("you have chosen to go right and you have win a treasure chest:")

        action = input("Do you want to open the treasere chest or leave it? (open/leave)\n").lower()

        if action == "open":
            print("you have chosen to opne the treasure chest and you have found a gold coin")
            score += 5

        elif action == "leave":
            print("you have chosen to leave the treasure chest and you have missed a gold coin")
        else:
            print("Invalid choice. please chooose a valid option:")

    elif user == Go_straight:
        print("you have chose to go straight and you have discovered a secret passage:")

        action = input("Do you want to enter the secret passage or leave it? (enter/leave)\n").lower()

        if action == "enter":
            print("you have chose to enter the secret passage and you have found a hidden room with a magic sword")
            score += 15

        elif action == "leave":
            print("you have chose to leave the secret passage and you have missed a magic sword")
        else:
            print("Invalid choice. please choose a valid option:")
            
    elif user == Quit_game:
        print("you have chosen to quit the game")
        break
    else:
        print("Invalid choice. Please choose a valid option:")

    print("your current score is:", score)
 
