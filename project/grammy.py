
import pandas as pd
import random
data=pd.read_csv("dataset.csv")
rank=data["Rank"].tolist()
name=data["Artist"].tolist()
monthly=data["Monthly Streams on Spotify"].tolist()
total=data["Total Streams (Spotify)"].tolist()
win=data["Grammy's Won"].tolist()
nomination=data["Nominations"].tolist()
genre=data["Genre"].tolist()

def ask_question(prompt, correct_answer, all_answers):
    wrong = [a for a in all_answers if a != correct_answer]
    options = random.sample(wrong, 3)
    options.append(correct_answer)
    random.shuffle(options)
    letters = ["A", "B", "C", "D"]
    print(prompt)
    for letter, opt in zip(letters, options):
        print(f"{letter}. {opt}")
    answer = input("Enter A, B, C, or D: ").strip().upper()
    if answer in letters:
        selected = options[letters.index(answer)]
    else:
        selected = None

    return selected == correct_answer

print("Welcome to the Grammy Museum! What do you want to do?")


choice=input("Quiz or Learn: ").title()
def program(output):
    if output=="Quiz":
        score = 0
        artist = random.choice(name)
        idx = name.index(artist)
        print(f"You are being quizzed on {artist}!\n")
        if ask_question("Question 1: What is the genre of this artist?",
                        genre[idx], genre):
            score += 1
        else:
            print(f"Wrong! The correct answer is {genre[idx]}.\n")
        if ask_question("Question 2: What is their current monthly rank?",
                        rank[idx], rank):
            score += 1
        else:
            print(f"Wrong! The correct answer is {rank[idx]}.\n")
        win_str = [str(w) for w in win]
        if ask_question("Question 3: How many Grammys has this artist won?",
                        win_str[idx], win_str):
            score += 1
        else:
            print(f"Wrong! The correct answer is {win[idx]}.\n")
        print(f"You got {score}/3 correct")
        print("Would you like to play again? (Yes/No) ")
        again = input().title()

        if again == "Yes":
            program("Quiz")
        elif again == "No":
            print("Thanks for playing!")
        else:
            print("Invalid input. Returning to main menu.")



    elif output=="Learn":
        knowledge=int(input("Choose a random number out of 100: "))
        found = False
        for i in range(len(name)):
            if knowledge==rank[i]:
                found = True
                print(f"The artist you're learning about is {name[i]}!")
                print(f"""According to the data, {name[i]} is ranked {rank[i]} on Spotify's monthly listeners and {total[i]} total
streams on Spotify and counting.""")
                print(f"{name[i]} has won {win[i]} Grammy Awards and has been nominated {nomination[i]} times")
                print("Do you want to learn about another artist? (Yes/No) ")
                response = input().title()
                if response=="Yes":
                    program("Learn")
                elif response=="No":
                    print("Thank you for visiting the Grammy Museum!")
                else:
                    print("Invalid input. Returning to main menu.")
                    program(choice)
                break
        if not found:
            print("No artist has that rank. Try again.")
            program("Learn")


program(choice)
