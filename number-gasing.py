import random

while True:
    number = random.randint(1, 10)
    count = 0

    while True:
        try:
            user = int(input("Enter a number between 1 and 10:\n"))

            if user < 1 or user > 10:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        count += 1

        if number == user:
            print("Correct prediction!")
            print(f"Your attempts: {count}")
            break

        elif number > user:
            print(f"Your guess is too small: {user}")

        else:
            print(f"Your guess is too big: {user}")

    action = input("Do you want to play again? (yes/no): ").lower().strip()

    if action == "yes":
        continue
    elif action == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Game over!")
        break