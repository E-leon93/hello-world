# coding=utf-8

#计算水仙花数，三位数，各位立方和等于三位数本身

item = 100

while item <= 999:
    k = item // 100
    h = (item // 10) % 10
    u = item % 10
    if (k**3 + h**3 + u**3) == item:
       print(item)
    item += 1
else:
    print('over')