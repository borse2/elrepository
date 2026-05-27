import pandas as pd
data=pd.read_csv('influencer.csv')
print(data)
month=data['Month'].tolist()
views=data['Views'].tolist()
dislikes=data['Dislikes'].tolist()
subscribers=data['Subscriber(+-)'].tolist()
revenue=data['Revenue'].tolist()

beginnings=[]
peak=[]
scandals=[]

def humble(number):
    for i in range(len(month)):
        if views[i] <= number:
            beginnings.append([i])
    print(beginnings)
    beginnings.clear()
def golden(growth):
    for i in range(len(month)):
        if subscribers[i] >= growth:
            peak.append([i])
    print(peak)
    peak.clear()
def scandal(disapproval):
    for i in range(len(month)):
        if revenue[i] <= disapproval:
            scandals.append([i])
    print(scandals)
    scandals.clear()
humble(2000)
print(data.loc[[0,1,2,3,4,5,6,7,8,9,10]])
golden(50000)
print(data.loc[[64,65,66,67,68,69,70,71,72]])
scandal(0)
print(data.loc[[98,107]])
