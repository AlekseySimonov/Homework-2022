input1 = open('input.txt', 'r')
input = input1.read().split('\n')

def check(input):
    if input not in dictionary:
        return int(input)

    if isinstance(dictionary[input], int): return dictionary[input]
    return main(input)

def main(input):

    parts = dictionary[input].split(' ')

    if len(parts) == 1:
        a = parts[0]
        if a in dictionary:
            dictionary[input] = check(a)
            return dictionary[input]
        else:
            return int(a)

    elif 'NOT' in parts:
        a = parts[1]
        dictionary[input] = ~check(a)
        return dictionary[input]

    elif "AND" in parts:
        a, b = parts[0], parts[2]
        dictionary[input] = check(a) & check(b)
        return dictionary[input]

    elif "XOR" in parts:
        a, b = parts[0], parts[2]
        dictionary[input] = check(a) ^ check(b)
        return dictionary[input]

    elif "OR" in parts:
        a, b = parts[0], parts[2]
        dictionary[input] = check(a) | check(b)
        return dictionary[input]

    elif "RSHIFT" in parts:
        a, b = parts[0], parts[2]
        dictionary[input] = check(a) >> check(b)
        return dictionary[input]

    elif 'LSHIFT' in parts:
        a, b = parts[0], parts[2]
        dictionary[input] = check(a) << check(b)
        return dictionary[input]

dictionary = {}

for k in input:

    string = k.split(' -> ')
    inp,res = string[0], string[1]
    dictionary[res]= inp

output = open('output1.txt', 'w')
output.write(str(main('a')))

output.close()
input1.close()