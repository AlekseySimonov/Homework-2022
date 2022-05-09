from itertools import permutations

with open('input.txt') as home0:
    home = home0.read().split('\n')

happiness = dict()
loc = set()

for i in home:
    name1,_,opinion,qp,_,_,_,_,_,_,name2 = i.split(' ')
    name2 = name2[0:-1]

    if opinion == 'lose':
        happiness[(name1,name2)] = -int(qp)
    else:
        happiness[(name1, name2)] = int(qp)

    loc.add(name1)

for you in loc:
    happiness[(you,'me')] = 0
    happiness[('me',you)] = 0

loc.add('me')

best = 0

for raw in permutations(loc):
    sum_happiness = 0

    sum_happiness += happiness[(raw[0], raw[-1])]
    sum_happiness += happiness[(raw[-1], raw[0])]

    for start, end in zip(raw[:-1], raw[1:]):
        sum_happiness += happiness[(start, end)]
        sum_happiness += happiness[(end, start)]

    best = max(best, sum_happiness)

output = open('output2.txt', 'w')
output.write(str(best))

output.close()
home0.close()