Data=[1,84,82,35,37,6,14,15,55,71,59,99]
for i in range(1,len(Data)):
    if i == len(Data) - 1:
        if Data[i] > Data[i-1]:
            print(f"A peak was found at value {Data[i]}, index {i}")
    elif Data[i] > Data[i-1] and Data[i] > Data[i+1]:
        print(f"A peak was found at value {Data[i]}, index {i}")
