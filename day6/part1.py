input = open('input.txt', 'r')
home = input.read().split("\n")

grid = [[0] * 1000 for i in range(1000)]

for line in home:
    lamps = line.split(' ')
    start = [int(x) for x in lamps[-3].split(',')]
    end = [int(x) for x in lamps[-1].split(',')]
    dool = ' '.join(lamps[0:-3])

    for y in range(start[0], end[0]+1):
        x1, x2 = start[1], end[1]+1

        if dool == 'turn off':
            for i in range(x1, x2):
                grid[y][i] = 0

        elif dool == 'turn on':
            for i in range(x1, x2):
                grid[y][i] = 1

        elif dool == 'toggle':
            for i in range(x1, x2):
                if grid[y][i] == 1:
                    grid[y][i] = 0
                else:
                    grid[y][i] = 1
count = 0

for y in grid:
    count += y.count(1)

output = open('output1.txt', 'w')
output.write(str(count))

output.close()
input.close()
