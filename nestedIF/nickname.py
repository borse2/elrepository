#Generate a code that determines what a character is based on a set of user inputs
print("Welcome to choose your superhero! DONT ADD SPACES BEFORE ASNWERING THE INPUT, please")
franchise=input("Do you prefer DC or Marvel? ")
if franchise=="Marvel":
    teamwork=input("Do you prefer to lead others or be by yourself 💔🐺 ")
    if teamwork=="lead others" and franchise=="Marvel":
        technology=input("Last question: do you prefer to be tech free or surround yourself in tech? ")
        if technology=="tech free" and franchise=="Marvel" and teamwork=="lead others":
            print("You're Captain America crodie")
        elif technology=="surround yourself in tech" and franchise=="Marvel" and teamwork=="lead others":
            print("You're Iron Man foo")
    elif teamwork=="be by yourself" and franchise=="Marvel":
        maturity=input("Would you describe yourself and childish or mature? ")
        if teamwork=="be by yourself" and franchise=="Marvel" and maturity=="mature":
            print("Pretty sure you're Wolverine")
        elif teamwork=="be by yourself" and franchise=="Marvel" and maturity=="childish":
            print("AYYYYY, you're Spider-Man")
elif franchise=="DC":
    characteristic=input("Are you more hopeful or more determined? ")
    if characteristic=="hopeful" and franchise=="DC":
        time=input("Do you prefer the dark or light? ")
        if characteristic=="hopeful" and franchise=="DC" and time=="light":
            print("My symbol of hope. You are Superman")
        elif characteristic=="hopeful" and franchise=="DC" and time=="dark":
            print("You are vengeance! You are Batman")
    elif characteristic=="determined" and franchise=="DC":
        creativity=input("Last question: Are you more creative or not creative? ")
        if characteristic=="determined" and franchise=="DC" and creativity=="creative":
            print("I bestow upon you Green Lantern")
        elif characteristic=="determined" and franchise=="DC" and creativity=="not creative":
            print("You are Wonder Woman. idk I ran out of ideas")

