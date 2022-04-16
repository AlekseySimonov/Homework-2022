import hashlib

input1 = open('input.txt', 'r')
input = input1.read()

i = 1
while True:
    MD5 = hashlib.md5((input+str(i)).encode())
    if MD5.hexdigest().startswith('00000'):
        break
    i += 1

output = open('output1.txt', 'w')
output.write(str(i))

output.close()
input1.close()