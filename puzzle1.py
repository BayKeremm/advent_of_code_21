_input_ = open("input" , "r")
content = _input_.read()
input_list = content.split("\n")
_input_.close()
count = 0
i = 0
for i in range(len(input_list)):
    if i == 0:
        continue
    if input_list[i]>input_list[i-1]:
        count += 1
    i = i + 1
print(count)
print(len(input_list))
