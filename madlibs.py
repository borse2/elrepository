#Boris Adokou
#Simulation of the popular madlibs game where silly stories are generated using input from the player
import random
start = '\033[1m'
end = '\033[0m'
def madlibs():
    #Gather input
    global start
    global end
    print("Welcome to Madlibs. If you want a random input type 'random'")
    pet1=input("Enter a pet: ")
    pets=["Dog", "Cat", "Rabbit", "Fish", "Hamster", "Snake", "Spider", "Turtle", "Pig", "Horse"]
    if pet1=="random":
        pet1=random.choice(pets)
    monument1=input("Enter any monument: ")
    monuments=["Sears Tower", "Burj Khalifa", "Pyramids of Giza", "The Bean", "Statue of Liberty", "Eiffel Tower", "Empire State Building", "Great Wall of China", "Christ the Redeemer", "The Hollywood Sign"]
    if monument1=="random":
        monument1=random.choice(monuments)
    adjective1=input("Enter any adjective: ")
    adjectives=["abnormal", "bizzare", "quirky", "cringe", "strange", "spirited", "attentive", "monsterous", "nonchalant", "studious"]
    if adjective1=="random":
        adjective1=random.choice(adjectives)
    proper_name1=input("Enter any proper name: ")
    yearning=["Faye Webster", "Laufey", "Alicia Keys", "Summer Walker", "beabadoobee", "PinkPanthress", "Lana Del Ray", "Mitski", "Fiona Apple", "Pheobe Bridgers"]
    if proper_name1=="random":
        proper_name1=random.choice(yearning)
    proper_name2=input("Enter any proper name: ")
    manipulators=["Bryson Tiller", "Brent Faiyaz", "Daniel Caesar", "PartyNextDoor", "Giveon", "Kanye West", "Future", "Asap Rocky", "Drake", "Steve Lacy"]
    if proper_name2=="random":
        proper_name2=random.choice(manipulators)
    nationality=input("Enter any nationality: ")
    nationalities=["American", "Japanese", "Brazilian", "German", "Canadian", "French", "Mexican", "Indian", "Chinese", "Middle Eastern"]
    if nationality=="random":
        nationality=random.choice(nationalities)

    #Story
    print(f"""Dear Diary, today I caught my {start}{pet1.upper()}{end} chopping bare tings at {start}{monument1.upper()}{end}
Is you {start}{adjective1.upper()}{end}? You moving super ways so bagg. I should've listened to {start}{proper_name1.upper()}{end} and {start}{proper_name2.upper()}{end}
Wallahi this is the last time im dealing a {start}{nationality.upper()}{end} {start}{pet1.upper()}{end}
.""")

madlibs()
