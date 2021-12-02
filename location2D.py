x = 0
y = 0
aim = 0
with open('input.txt') as f:
    for line in f:
        cmd = "".join([s for s in line if s.isalpha()])
        val = int("".join([n for n in line if n.isdigit()]))
        if cmd == "forward":
            x += val
            y = y + aim*val
        if cmd == "down":
            aim += val
        if cmd == "up":
            aim -= val
print(x*y)
print(aim)
print(x)
print(y)
