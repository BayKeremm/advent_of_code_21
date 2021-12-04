import numpy as np
f = open("input", "r")
raw_data = f.read().split()
numbers = list(map(int,raw_data[0].split(",")))
cards = np.array(raw_data[1:],dtype="int64")
print(cards)
print(numbers)


def checkRows(sub_set):
    for i in range(0, len(cards), 5):
        print(cards[i:i+5])
        arr = []
        for j in range(5):
            arr.append(cards[i+j])
        curr_set = set(arr)
        print(arr)
        rc = set.intersection(sub_set,curr_set)
        print(rc)
        break


number_set = {}
number_set = set()
for i in numbers:
    number_set.add(i)

print(number_set)
checkRows(number_set)
    
