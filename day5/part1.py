input = open('input.txt','r')
total = 0

def CountVowels(string):
   vowels = ['a','e','i','o','u']
   total = 0
   for s in string:
      if s in vowels:
         total += 1
   return total

def Doubles(string):
    double = 0
    for x, y in zip(string[0:], string[1:]):
        if x == y:
            double += 1
    return double

def Contain(string):
    contain = 0
    for pattern in ['ab', 'cd', 'pq', 'xy']:
        if pattern in string:
            contain += 1
    return contain
i = 0
while i <= 1000:
    string = input.readline()
    vowels = CountVowels(string)
    doubles = Doubles(string)
    contain = Contain(string)
    if vowels >= 3 and doubles >= 1 and contain == 0:
        total += 1
    i += 1

output = open('output1.txt', 'w')
output.write(str(total))

output.close()
input.close()