with open('input.txt', 'r') as INPUT:
    line = INPUT.readline()

for counter in range(50):
    array = [element for element in line]
    HMNumb = 1
    new_array = []
    try:
        for i in range(len(array)):
            if array[i] == array[i + 1]:
                HMNumb += 1
            else:
                new_array.append(str(HMNumb))
                new_array.append(array[i])
                HMNumb = 1
    except IndexError:
        None
        if array[-1] == array[-2]:
            new_array[-1][0] += 1
            line = ''.join(new_array)
        else:
            new_array.append(str(1))
            new_array.append(array[-1])
            line = ''.join(new_array)

output = open('output2.txt', 'w')
output.write(str(len(line)))

output.close()
INPUT.close()