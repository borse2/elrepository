import pandas as pd
data=pd.read_csv('data.csv')
print(data)
level=data['Level'].tolist()
time=data['Time'].tolist()
summary=data['Summary'].tolist()
feedback=data['Feedback'].tolist()
rating=data['Rating'].tolist()

bad=[]
great=[]
interesting=[]
def problems(review):
    for i in range(len(rating)):
        if review>=rating[i]:
            bad.append([i])
    print(bad)
    bad.clear()

def positive(review,seconds):
    for i in range(len(rating)):
        if rating[i]>=review and seconds<=time[i]:
            great.append([i])
    print(great)
    great.clear()

def suprise(word):
    for i in range(len(feedback)):
        if word in feedback[i]:
            interesting.append([i])
    print(interesting)
    interesting.clear()

problems(2)
print(data.loc[[14,34,77]])
positive(4,650)
print(data.loc[[79]])
suprise("secret")
print(data.loc[[66]])
