a = list(map(int, input("").split(" ")))
sum = 0
a_new = []
for i, x in enumerate(a):
    if int(x) < 0 and int(x) % 7 == 0:
        sum += x
        i += 1
        a_new.append(x)
print("Сумма отрицательных элементов, кратных 7 :", sum)
print("Новый список:", a_new)
