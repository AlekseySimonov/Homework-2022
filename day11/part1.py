import re

with open("input.txt") as input:
    old_password = list(input.read())

def straight(password):
    return any(ord(password[i + 1]) == ord(password[i]) + 1 and ord(password[i + 2]) == ord(password[i]) + 2 for i in range(0, len(password)-2))

def double_letter(password):
    return bool(re.match(r'^.*(.)\1.*(.)\2.*$', "".join(password)))

def bad_letters(password):
    return not any(bad_letter in password for bad_letter in ['i', 'o', 'l'])

def check(password):
    return straight(password) and double_letter(password) and bad_letters(password)

def increase_password(password):
    password[-1] = 'a' if ord(password[-1]) + 1 > ord('z') else chr(ord(password[-1]) + 1)
    return password if password[-1] != 'a' else increase_password(password[:-1]) + ['a']

new_password = increase_password(old_password)
while not check(new_password):
    new_password = increase_password(new_password)

output = open('output1.txt', 'w')
output.write(''.join(new_password))

output.close()
input.close()