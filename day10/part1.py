with open("input.txt") as string:
    a = string.read()
b = 0
while b <= 39:
    number = a[0]
    len_ = 1
    result = ''
    for i in (a +'X')[1:]:
        if number == i:
            len_ += 1
        else:
            result += str(len_)+str(number)
            number = i
            len_ = 1
    a = result

    b += 1

output = open('output1.txt', 'w')
output.write(str(len(a)))

output.close()
string.close()








