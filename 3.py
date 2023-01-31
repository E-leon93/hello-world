# coding=utf-8

print('----字符串----')

for i in 'hello':
    print(i)

print('----整数----')

n=[1,2,3,4,5]

for i in n:
    print(i)
else:
    print('ending')

for item in range(10):
    if item == 10:
        break
    print(item)
else:
    print('over')