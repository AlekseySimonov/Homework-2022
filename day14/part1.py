input = open('input.txt', 'r')
result = []
while True:
    string = input.readline().split()
    if not string:
        break
    name = string[0]
    speed = string[3]
    time = string[6]
    rest = string[-2]
    total, rest = divmod(2503, int(rest) + int(time))
    distance = int(speed) * int(time) * total
    if rest > int(time):
        distance += int(speed) * int(time)
    else:
        distance += int(speed) * rest
    result.append(distance)

output = open('output1.txt', 'w')
output.write(str(max(result)))

output.close()
input.close()