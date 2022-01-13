import csv
from collections import Counter

with open("E:/WHITEHAT JR/python/C-104/Database.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
# print(file_data)
file_data.pop(0)
# print(file_data)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))
n = len(new_data)
def mean():
    total = 0
    for x in new_data:
        total += x

    mean = total/n
    print("Mean is " + str(mean))
def median():
    new_data.sort()
    # print(new_data)
    if n%2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[(n//2)-1])
        median = (median1+median2)/2
    else: 
        median = new_data[n//2]

    print("Median is " + str(median))

def mode():
        
    #Calculating Mode
    data = Counter(new_data)
    
    mode_data_for_range = {
                            "110-115": 0,
                            "115-120": 0,
                            "120-125": 0
                        }
    for weight, occurence in data.items():
        if 110 < float(weight) < 115:
            mode_data_for_range["110-115"] += occurence
        elif 115 < float(weight) < 120:
            mode_data_for_range["115-120"] += occurence
        elif 120 < float(weight) < 125:
            mode_data_for_range["120-125"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is {mode:2f}")

a = float(input("Enter\n1 for mean\n2 for median\n3 for mode"))
if a == 1:
    mean()
elif a == 2:
    median()
elif a == 3:
    mode()
else:
    print("invalid input")