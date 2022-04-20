from collections import defaultdict
from itertools import permutations

input1 = open('input.txt', 'r')

location = set()
graph = defaultdict(dict)
for line in input1:
    src, _, dst, _, dist = line.split()
    location.add(src)
    location.add(dst)
    graph[src][dst] = int(dist)
    graph[dst][src] = int(dist)

distance = []
for perm in permutations(location):
    distance.append(sum(map(lambda i, j: graph[i][j], perm[:-1], perm[1:])))

output = open('output2.txt', 'w')
output.write(str(max(distance)))

output.close()
input1.close()
