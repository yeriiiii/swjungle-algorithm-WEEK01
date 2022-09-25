#<14888 연산자 끼워넣기>

import sys
from itertools import permutations

#input 받기
N = int(sys.stdin.readline())

num_array = list(map(int, sys.stdin.readline().split())) # [A1, A2, ... AN]
num_of_operator = list(map(int, sys.stdin.readline().split())) # [ (+), (-), (x), (÷) ]

#helper funcition
def calculator(a, b, oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == 'x':
        return a*b 
    elif oper == '÷':
        if a<0 and b>0:
            return -((-a)//b)
        else: 
            return a//b


operator_array = []
per_set = set()
max_value = -1000000000
min_value = 1000000000

for i in range (num_of_operator[0]):
    operator_array.append('+')
for i in range (num_of_operator[1]):
    operator_array.append('-')
for i in range (num_of_operator[2]):
    operator_array.append('x')
for i in range (num_of_operator[3]):
    operator_array.append('÷')

# 조합 set 생성
for per in permutations(operator_array, N-1):
    per_set.add(per)


for per in per_set:
    ls = list(per) # [ + + x - ÷ ]
    value = num_array[0]

    #순열 값 계산
    for i in range (0, N-1):
        value = calculator(value,num_array[i+1],ls[i])

    #max, min value update
    if value > max_value: max_value = value
    if value < min_value: min_value = value

print(max_value)
print(min_value)

