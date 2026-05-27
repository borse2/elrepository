import webbrowser

#Sources

#PS1
#Description: Image of the PS1
#Website Name: Playstation
#URL: https://www.playstation.com/en-us/playstation-history/1994-ps-one/
#Author Name: Unknown
#Date: Unknown
#Article Title: 30 Years of play
#-------------------------------------
#PS2
#Description: Image of the PS2
#Website Name: Playstation
#URL: https://www.playstation.com/en-us/playstation-history/2000-ps2/
#Author Name: Unknown
#Date: Unknown
#------------------------------------
#PS3
#Description: Image of the PS3
#Website Name: Playstation
#URL: https://www.playstation.com/en-us/playstation-history/2006-ps3/
#Author Name: Unknown
#Date: Unknown
#Article Title: 30 Years of play
#------------------------------------
#PS4
#Description: Image of the PS4
#Website Name: Playstation
#URL: https://www.playstation.com/en-us/playstation-history/2013-ps4/
#Author Name: Unknown
#Date: Unknown
#Article Title: 30 Years of play
#-------------------------------------
#PS5
#Description: Image of the PS5
#Website Name: Playstation
#URL: https://www.playstation.com/en-us/playstation-history/2020-ps5/
#Author Name: Unknown
#Date: Unknown
#Article Title: 30 Years of play

playstations=["https://tinyurl.com/2r62d2dt", #PS1
              "https://tinyurl.com/mtp35yr5", #PS2
              "https://tinyurl.com/49s2me6z", #PS3
              "https://tinyurl.com/5brhjxe3", #PS4
              "https://tinyurl.com/46wuux6n", #PS5
              ]
#MAIN CODE
age=input("Are you 18? Yes or No")
if age=="Yes":
    tech=input("TV or Computer or Telephone?")
    if tech=="TV":
        print("Because you are over 18 AND prefer the TV, I think you are a great fit for the PS1")
        webbrowser.open(playstations[0])
    elif tech=="Computer":
        print("Because you are over 18 AND prefer the Computer, I think you are a great fit for the PS2")
        webbrowser.open(playstations[1])
    elif tech=="Telephone":
        print("Because you are over 18 AND prefer the Telephone, I think you are a great fit for the PS3")
        webbrowser.open(playstations[2])
else:
    leisure=input("Indoor or Outdoor?")
    if leisure=="Indoor":
        print("Because you are under 18 AND prefer Indoor activities, I think you are a great fit for the PS4")
        webbrowser.open(playstations[3])
    elif leisure=="Outdoor":
        print("Because you are under 18 AND prefer Outdoor activities, I think you are a great fit for the PS5")
        webbrowser.open(playstations[4])
