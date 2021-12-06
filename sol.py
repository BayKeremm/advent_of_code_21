
f = open("input", "r")
data = list(map(int,f.read().split(',')))
j = 0

count = [data.count(i) for i in range(9)]
print(count)
print(count[1:])
print(count[:-1])
for i in range(256):
	zeros = count[0]
	count[:-1] = count[1:]
	count[6] += zeros
	count[8] = zeros
print(sum(count))
