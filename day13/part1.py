from collections import defaultdict
from itertools import permutations

table = defaultdict(dict)
with open('input.txt') as input:
    for line in input:
        name1,_,gainloss,points,_,_,_,_,_,_,name2 = line.split()
        name2 = name2[:-1]
        if gainloss == 'lose':
            points = -int(points)
        else:
            points = int(points)
        table[name1][name2] = points

def get_total_happiness(a):
    a = [a[-1]] + a + [a[0]]
    return sum(table[p2][p1]+table[p2][p3] for p1,p2,p3 in zip(a, a[1:], a[2:]))

output = open('output1.txt', 'w')
output.write(str(max(get_total_happiness(list(x)) for x in permutations(table.keys()))))

output.close()
input.close()


