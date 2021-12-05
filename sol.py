import re
f = open("input","r")
arr = [[0 for i in range(1000)] for j in range(1000)]
for i in f:
    i.strip("\n")
    x1,y1,x2,y2 = map(int, re.findall(r'\d+', i))
    if(x1 == x2 or y1 == y2):
        if(y1==y2):
            if x1<x2:
                while x1<=x2:
                    arr[y1][x1] += 1
                    x1 += 1
            else:
                while x2<=x1:
                    arr[y1][x2] += 1
                    x2 +=1
        else:
            if y2>y1:
                while y1 <= y2:
                    arr[y1][x1] += 1
                    y1 = y1 + 1
            else:
                while y2 <= y1:
                    arr[y2][x1] =  arr[y2][x1]+1
                    y2 = y2 + 1
    
                    
count = 0
for i in range(1000):
    print(arr[i])
    for j in range(1000):
        if arr[i][j] >= 2:
            count += 1
print(arr)
print(count)

