f = open("input", "r")
binaryArr = f.read().splitlines()
oxygensArr = binaryArr
nBinaryDigits = len(binaryArr[0])
for index in range(nBinaryDigits): 
    cnt = sum(1 if oxy[index]=='1' else -1 for oxy in oxygensArr)
    oxygensArr = list(filter(lambda binary: binary[index]=='1' if cnt>=0 else binary[index]=='0', oxygensArr))
    if len(oxygensArr)==1:
        break  
co2Arr = binaryArr
for index in range(nBinaryDigits):
    cnt = sum(1 if co2[index]=='1' else -1 for co2 in co2Arr)
    co2Arr = list(filter(lambda binary: binary[index]=='0' if cnt>=0 else binary[index]=='1', co2Arr))
    if len(co2Arr)==1:
        break
oxygenVal = int(oxygensArr[0], 2)
co2Val = int(co2Arr[0], 2)
print(oxygenVal*co2Val)
