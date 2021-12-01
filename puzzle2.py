data = []
increases = 0

with open("example.txt","r") as f:
    for i in f.readlines():
                data.append(int(i.rstrip("\n")))

window_size = 3
i = 0
avg = []
while i < len(data) - window_size + 1:
    curr = data[i : i + window_size]
    curr_avg = sum(curr)/window_size
    avg.append(curr_avg)
    i += 1

for a in range(len(avg)):
    if a == 0:
        continue
    if data[i] > data[i-1]:
        increases += 1

print(increases)
