input = open('input.txt','r')
input_list = list(input)
direction = sum([list(i) for i in input_list], [])

Santa = list(direction)
Robo_Santa = list(direction)
del Santa[1::2], Robo_Santa[2::2], Robo_Santa[0]

def visited_houses(any_direction):
    x = 0
    y = 0
    N_S = []
    W_E = []

    for i in any_direction:
        if i == '<':
            y -= 1
            N_S.append(x)
            W_E.append(y)
        elif i == '>':
            y += 1
            N_S.append(x)
            W_E.append(y)
        elif i == '^':
            x += 1
            N_S.append(x)
            W_E.append(y)
        elif i == 'v':
            x -= 1
            N_S.append(x)
            W_E.append(y)
    return [' '.join(str(x)) for x in zip(N_S, W_E)]

result_Robo_Santa = visited_houses(Robo_Santa)
result_Santa = visited_houses(Santa)
result = len(set(result_Robo_Santa + result_Santa))

output = open('output2.txt', 'w')
output.write(str(result))

output.close()
input.close()