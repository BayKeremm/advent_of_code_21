f = open("input", "r")
binarray = f.read().splitlines()
oxygensArr = binarray
binaryDigits = len(binarray[0])
for index in range(binaryDigits):
    cnt = sum(1 if oxy[index]=='1' else -1 for oxy in oxygensArr)
    oxygensArr = list(filter(lambda binary: binary[index]=='1' if cnt>=0 else binary[index]=='0', oxygensArr))
    print(oxygensArr)

