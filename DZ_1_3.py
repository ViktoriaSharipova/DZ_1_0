q = 0
q_max = 15
q_min = 10
while (True):
    a = int(input("Введите число"))
    if a == 7:
        print("Пока")
        break
    elif a > q_max:
        q_max = a
    q = q + a

print('Сумма введенных чисел равна ', q)
print("Максиммальное из введенных чисел это - ", q_max)
