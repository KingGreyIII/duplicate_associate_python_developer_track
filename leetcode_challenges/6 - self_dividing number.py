left = 1
right = 22
num_list = [values for values in range(left, right + 1) if int(str(values)[-1]) != 0]
acceptable = []
for values in num_list:
    for i in range(len(str(values))):
        print(values % int(str(values)[i]))
# print(num_list)
