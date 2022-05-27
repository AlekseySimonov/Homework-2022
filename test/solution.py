input1 = open('input.txt', 'r')
input = input1.read()
b = bin(int(input)).replace('0b', '')   # переведем число в двоичную систему исчисления

list_ = []
list_.append(b)
results = []

# функция для сдвига последнего элемента в начало
def convert(string):
    list_ = list(string)
    list_.insert(0, list_.pop())
    return ''.join(list_)

# помещаем в список list_ все полученные числа
a = 0
while a != len(b) - 1:
    b = convert(b)
    a += 1
    list_.append(b)

# переводим в десятичную систему исчисления
for i in list_:
    i = int(i, 2)
    results.append(i)

# максимальное выписанное число
answer = max(results)

output = open('output.txt', 'w')
output.write(str(answer))

output.close()
input1.close()
