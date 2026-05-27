##purpose of this program is to help users find a dog that fits their needs"

#Initializing
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
import webbrowser
import pandas as pd
data=pd.read_csv("dogs.csv")
id=data["id"].tolist()
name=data["Name"].tolist()
breed=data["Breed Group"].tolist()
reason=data["BredFor"].tolist()
minlife=data["Minimum Life Span"].tolist()
maxlife=data["Maximum Life Span"].tolist()
minweight=data["Minimum Weight"].tolist()
maxweight=data["Maximum Weight"].tolist()
temperament=data["Temperament"].tolist()
image=data["Image"].tolist()
filter=[]



#Functions
#-------------------------------------------------------------------
def dogs(size):
    if size == "Tiny":
            for i in range(len(breed)):
                if 0<=minweight[i] and maxweight[i]<=10:
                    filter.append(name[i])
    elif size == "Small":
            for i in range(len(breed)):
                if 11<=minweight[i] and maxweight[i]<=25:
                    filter.append(name[i])
    elif size == "Medium":
            for i in range(len(breed)):
                if 26<=minweight[i] and maxweight[i]<=60:
                    filter.append(name[i])
    elif size == "Large":
            for i in range(len(breed)):
                if 61<=minweight[i]:
                    filter.append(name[i])
    print(filter)
    filter.clear()
#-------------------------------------------------------------------
def dogs2(dog_breed):
    for i in range(len(breed)):
        if dog_breed==breed[i]:
            filter.append(temperament[i])
            webbrowser.open(image[i])
    if dog_breed not in breed[i]:
        print("Invalid input")
#-------------------------------------------------------------------
def dogs3(purpose):
    for i in range(len(breed)):
        if purpose==reason[i]:
            filter.append(name[i])
    if purpose not in reason[i]:
        print("Invalid input")
    print(filter)
#-------------------------------------------------------------------
def menu():
    print("Welcome to the Dog Finder!")
    print("1. Find dogs by size")
    print("2. Find dogs by breed")
    print("3. Find dogs by purpose")


while True:
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        size = input("Enter the size (Tiny, Small, Medium, Large): ")
        dogs(size)
    elif choice == "2":
        breed = input("Enter the breed: ")
        dogs2(breed)
    elif choice == "3":
        purpose = input("Enter the purpose: ")
        dogs3(purpose)
    else:
        print("Invalid choice. Please try again.")

#Main
menu()
