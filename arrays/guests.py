#Boris Adokou
#Creating a program that manipulates a guest list
guests = [
"Alice", "Bob", "Charlie", "David", "Eve",
"Frank", "Grace", "Heidi", "Ivan", "Judy",
"Kevin", "Liam", "Mallory", "Nia", "Oscar",
"Peggy", "Quinn", "Riley", "Sybil", "Trent",
"Uma", "Victor", "Walter", "Xander", "Yara",
"Zane", "Amari", "Blake", "Casey", "Dakota"
]
plus1=input("Who is your +1 ")
guests.append(plus1)
print(guests)
#--------------------------------------------------------
vip=input("Welcome, valued guest! What is your name?: ")
guests.insert(0, vip)
print(guests)
#--------------------------------------------
guests[1]="Harvey"
print(guests)
#---------------------------------------
print(len(guests))
