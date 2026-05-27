#Boris Adokou
#Program that manipulates students scores
scores = [
88, 42, 95, 70, 63, 82, 55, 91, 74, 85,
38, 77, 90, 61, 89, 72, 59, 98, 45, 81,
67, 73, 88, 52, 94, 79, 100, 68, 83, 71
]
print(min(scores))
print(max(scores))
#-----------------------------------
average=sum(scores)/len(scores)
print(average)
#-----------------------------------
scores.sort()
print(scores[0:3])
#------------------------------------
for i in range(len(scores)):
    scores[i]+=5
print(scores)
