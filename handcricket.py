import random

def play_innings(player_role, target=None):
    score = 0
    print(f"\nYou are {player_role}")

    while True:
        user = int(input("Enter your score (1-6): "))
        if user < 1 or user > 6:
            print("Enter a number between 1 and 6 only.")
            continue

        computer = random.randint(1, 6)
        print(f"Computer played: {computer}")

        if user == computer:
            print("Out!")
            break
        else:
            score += user
            print(f"Score: {score}")

        if target and score > target:
            break

    return score

def main():
    print("=== HAND CRICKET GAME ===")
    choice = input("Choose bat or bowl (bat/bowl): ").lower()

    if choice == "bat":
        player_score = play_innings("Batting")
        print(f"\nYour total score: {player_score}")

        print("\nComputer is batting...")
        computer_score = play_innings("Bowling", player_score)

    else:
        print("\nComputer is batting first...")
        computer_score = play_innings("Bowling")
        print(f"\nComputer total score: {computer_score}")

        player_score = play_innings("Batting", computer_score)

    print("\n=== RESULT ===")
    if player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("MATCH DRAWN!")

if __name__ == "__main__":
    main()