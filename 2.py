import sys
print("Введите список:")
x = list(map(int, input().split(" ")))
a = int(input("Введите a: "))
b = int(input("Введите b: "))
x1 = []
x2 = x
x3 = []
k = 0
o = a
sum = 0

if a < 0 or b < 0:
    print("Введите положительные a/b", file=sys.stderr)
    exit(1)
if a > b:
    print("число a не должно быть больше числа b", file=sys.stderr)
    exit(1)

for l in x:
    x1.append(abs(float(l)))
m = max(x1)
print("Максимальное число по модулю:", m)

for i in x:
    if (k == 0) and (i > 0):
        k += 1
        sum = -i
    if (k > 0):
        sum += i
if sum == 0:
    print("В списке нет отрицательных чисел", file=sys.stderr)
else:
    print("Сумма элементов, после первого положительного числа: ", sum)

x2 = x[a:b + 1]
for c, g in enumerate(x):
    if a > c or b < c:
        x3.append(g)
x4 = x2 + x3
print("Новый список, где элементы от a до b идут первыми:")
print(x4)