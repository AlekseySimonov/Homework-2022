import json

with open("input.txt") as input:
    data = json.loads(input.read())


def sum_(data):

    result = 0

    if isinstance(data, int):
        result += data
    elif isinstance(data, list):
        for j in data:
            result += sum_(j)
    elif isinstance(data, str):
        pass
    elif isinstance(data, dict):
        for j in data:
            if data[j] == 'red':
               return 0
            result += sum_(data[j])
    return result


result = sum_(data)

output = open('output2.txt', 'w')
output.write(str(result))

output.close()
input.close()