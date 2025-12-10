def separator():
    print("-" * 30)

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower().strip()
if playing != "yes":
    quit(1)
print("Okay! Let`s play :)")

questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply"),
    ("What does SSD stand for? ", "solid state drive"),
    ("What does HTML stand for? ", "hypertext markup language"),
    ("What does API stand for? ", "application programming interface"),
]

while playing == "yes":
    score = 0
    for question, answer in questions:
        separator()
        response = input(question).lower().strip()
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    separator()
    print(f"You got {score} questions correct!")
    print(f"You got {(score / len(questions)) * 100:.1f}%.")
    separator()

    playing = input("Do you want to play again? ").lower().strip()
separator()
print("\n")
print("Thanks for the game!")