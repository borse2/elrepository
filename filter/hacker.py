import pandas as pd
data=pd.read_csv('hacker.csv')
print(data)
log=data['IP_Address'].tolist()
protocol=data['Protocol'].tolist()
size=data['Data_KB'].tolist()
time=data['Time'].tolist()
description=data['Description'].tolist()
thief=[]
bad_logs=[]
filter=[]
def compromise(word):
    for i in range(len(log)):
        if word in description[i]:
            bad_logs.append([i])
    print(bad_logs)
    bad_logs.clear()
def stolen(large):
    for i in range(len(log)):
        if large in description[i]:
            thief.append([i])
    print(thief)
    thief.clear()
def force(word):
    for i in range(len(log)):
        if word in description[i]:
            filter.append([i])
    print(filter)
    filter.clear()

compromise('Failed')
print(data.loc[[193,194,195]])
print(data.loc[[196,197,198]])
stolen("Bulk")
print(data.loc[[199]])
force("Required")
print(data.loc[[204,205,207,210,214,218,221,222,224,231,235,267]])



