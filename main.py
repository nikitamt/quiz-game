#Quiz Game

def separator():
    print("-" * 30)

QUESTIONS = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply"),
    ("What does SSD stand for? ", "solid state drive"),
    ("What does HTML stand for? ", "hypertext markup language"),
    ("What does API stand for? ", "application programming interface"),
]

def play_round() -> None:
    score = 0
    for question, answer in QUESTIONS:
        separator()
        response = input(question).lower().strip()
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {answer}.")

    separator()
    print(f"You got {score} questions correct!")
    print(f"You got {(score / len(QUESTIONS)) * 100:.1f}%.")
    separator()

    return

def main() -> None:
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ").lower().strip()
    if playing not in ("yes", "y"):
        print("Okay, maybe next time!")
        return
    print("Okay! Let`s play :)")

    while True:
        play_round()

        playing = input("Do you want to play again? ").lower().strip()
        if playing not in ("yes", "y"):
            break

    print("\n")
    print("Thanks for the game!")

if __name__ == "__main__":
    main()