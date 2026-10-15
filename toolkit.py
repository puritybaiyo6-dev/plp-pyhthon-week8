
import random


# Tool 1: Calculate the result of two numbers.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"Your answer is: {result:g}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Manage a list of tasks that changes while the program runs.
def todo_list_manager():
    tasks = []

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Your task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number is not on the list.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 4.")


# Tool 3: Let the user guess a randomly selected number.
def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number from 1 to 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Correct! You guessed the number in "
                    f"{attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a whole number.")


# Main program: display the menu until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list_manager()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please enter a number from 1 to 4."
            )


if __name__ == "__main__":
    main()
