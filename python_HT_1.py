param_1 = 'test'
param_2 = 5
param_3 = 3.05
param_4 = bytes(4)
param_5 = ['one', 'two', 'three']
param_6 = ('ios', 'android')
param_7 = {'opel', 'audi', 'bmw'}
param_8 = frozenset(['ooo', 'aaa', 'zzz'])
param_9 = {
  "car": "Bmw",
  "model": "X3",
  "year": 2018
}
print('param_1 =', param_1, type(param_1))
print('param_2 =', param_2, type(param_2))
print('param_3 =', param_3, type(param_3))
print('param_4 =', param_4, type(param_4))
print('param_5 =', param_5, type(param_5))
print('param_6 =', param_6, type(param_6))
print('param_7 =', param_7, type(param_7))
print('param_8 =', param_8, type(param_8))
print('param_9 =', param_9, type(param_9))

a_1 = 'my'
a_2 = 'name'
a_3 = a_1 + a_2
print(a_3)

b_1 = 7
b_2 = 5
b_3 = b_1 + b_2
print(b_3)

b_1 = 7
b_2 = 5
b_4 = b_1 * b_2
print(b_4)

b_1 = 7
b_2 = 5
b_5 = b_1 // b_2
print(b_5)

b_1 = 7
b_2 = 5
b_6 = b_1 % b_2
print(b_6)

b_7 = (7 + 12) ** 3 + 7 * 4 - 44 / 2**4
print(b_7)
