s_1 = 'aaa'
s_2 = 'bbb'

i_1 = 1
i_2 = 2
i_3 = 3
i_4 = 4

f_1 = 3.5
f_2 = 4.1
f_3 = 7.9

print(i_1 < i_4)
print(i_2 < i_4)
print(i_1 > i_2)
print(i_1 <= i_3)
print(i_1 != i_4)
print(i_2 <= i_3)
print(i_4 <= i_2)
print(i_3 == i_4)
print(i_3 == i_1)
print(i_1 <= i_2)
print(i_3 > i_2)
print(i_4 >= i_2)
print(i_1 > i_3)
print(i_4 == i_4)

print(f_1 < f_3)
print(f_1 > f_2)
print(f_1 <= f_1)
print(f_2 == f_1)
print(f_2 >= f_3)
print(f_2 < f_2)
print(f_3 >= f_1)
print(f_3 < f_2)
print(f_3 == f_3)

# and or not

result = i_1 >= 0 and i_4 < 10
print('result_1 =', result)
result = i_2 <60 or i_1 > 10
print('result_2 =', result)
result = i_2 <60 and i_1 > 10
print('result_3 =', result)
result = not i_4 < 3
print('result_4 =', result)
result = i_3 > 9 and i_1 < 10
print('result_5 =', result)
result = i_2 == 4 or i_4 < 9
print('result_6 =', result)
result = not i_2 == 2
print('result_7 =', result)
result = i_1 >= 0 and not i_4 < 10
print('result_8 =', result)
result = i_4 <= 4 or i_3 < 100
print('result_9 =', result)
result = i_3 > 4 or i_3 < 100
print('result_10 =', result)

number = input()
if int(number) < 30:
    print('Вы ввели число ' + number + ', которое меньше ' + '30')
if int(number) > 30:
    print('Вы ввели число ' + number + ', которое больше ' + '30')
if int(number) == 30:
    print('Вы ввели число ' + number + ', которое равно ' + '30')

number = input()
import random
if int(number) < random.randint(1, 100):
    print('Вы ввели число ' + number + ', которое меньше ' + str(random.randint(1, 100)))
if int(number) > random.randint(1, 100):
    print('Вы ввели число ' + number + ', которое больше ' + str(random.randint(1, 100)))
if int(number) == random.randint(1, 100):
    print('Вы ввели число ' + number + ', которое равно ' + str(random.randint(1, 100)))

number = input()
import random
a = random.randint(1, 100)
if int(number) < random.randint(1, 100):
    print('Вы ввели число ' + number + ', которое меньше ' + str(a))
if int(number) > random.randint(1, 100):
    print('Вы ввели число ' + number + ', которое больше ' + str(a))
if int(number) == random.randint(1, 100):
    print('Вы ввели число ' + number + ', которое равно ' + str(a))

number = input()
import random
a_1 = random.randint(1, 100)
import random
a_2 = random.randint(1, 100)
if int(number) < a_1 and int(number) > a_2:
    print('Вы ввели число ' + number + ', которое меньше ' + str(a_1) + ' и больше ' + str(a_2))
if int(number) < a_1 and int(number) < a_2:
    print('Вы ввели число ' + number + ', которое меньше ' + str(a_1) + ' и меньше ' + str(a_2))
if int(number) < a_1 and int(number) == a_2:
    print('Вы ввели число ' + number + ', которое меньше ' + str(a_1) + ' и равно ' + str(a_2))
if int(number) > a_1 and int(number) < a_2:
    print('Вы ввели число ' + number + ', которое больше ' + str(a_1) + ' и меньше ' + str(a_2))
if int(number) > a_1 and int(number) > a_2:
    print('Вы ввели число ' + number + ', которое больше ' + str(a_1) + ' и больше ' + str(a_2))
if int(number) > a_1 and int(number) == a_2:
    print('Вы ввели число ' + number + ', которое больше ' + str(a_1) + ' и равно ' + str(a_2))
if int(number) == a_1 and int(number) < a_2:
    print('Вы ввели число ' + number + ', которое равно ' + str(a_1) + ' и меньше ' + str(a_2))
if int(number) == a_1 and int(number) > a_2:
    print('Вы ввели число ' + number + ', которое равно ' + str(a_1) + ' и больше ' + str(a_2))
if int(number) == a_1 and int(number) == a_2:
    print('Вы ввели число ' + number + ', которое равно ' + str(a_1) + ' и равно ' + str(a_2))