# 5 4 3 1 2 3 4 5 3 2 2 1 6 6 2 2 1 1 2 6
# Задание 1.
import matplotlib.pyplot as plt
list = [] 

while len(list) < 20: 
    try:
        inp = int(input())
        list.append(inp)
    except:
        print("Только целые числа")


o = int()
a1 = sum(True for i in list if i == 1)
b2 = sum(True for i in list if i == 2)
c3 = sum(True for i in list if i == 3)
d4 = sum(True for i in list if i == 4)
e5 = sum(True for i in list if i == 5)
f6 = sum(True for i in list if i == 6)


print(list)
print('ВАРИАЦИОННЫЙ РЯД')
print(a1, ' - 1')
print(b2, ' - 2')
print(c3, ' - 3')
print(d4, ' - 4')
print(e5, ' - 5')
print(f6, ' - 6')


x = ('0', '1', '2', '3', '4', '5', '6')
y = (o, a1, b2, c3, d4, e5, f6)

# гистограмма частот
fig, axes = plt.subplots()
axes.bar(x, y)
plt.xlabel('Варианты')
plt.ylabel('Частота')
plt.show()

# Полигон частот
plt.axis([0, 7, 0, 7])
plt.xlabel('Варианты')
plt.ylabel('Частота')
plt.plot(x, y)
plt.show()


l_s = sorted(list)
summa_chastot = a1 + b2 + c3 + d4 + e5 + f6
sr_qv = ((1 ** 2) * a1 + (2 ** 2) * b2 + (3 ** 2) * c3 + (4 ** 2) * d4 + (5 ** 2) * e5 + (6 ** 2) * f6)/summa_chastot
v_srednya = (1 * a1 + 2 * b2 + 3 * c3 + 4 * d4 + 5 * e5 + 6 * f6)/summa_chastot
v_dispersia = (sr_qv - (v_srednya ** 2)) * summa_chastot / (summa_chastot - 1)
st_otcl = v_dispersia ** 0.5
one_proc = st_otcl / 100
kf_v = (st_otcl / v_srednya * 100)
print('Сумма частот - ', summa_chastot)
print('Выборочная средняя - ', v_srednya)

if (a1 > b2) and (a1 > c3) and (a1 > d4) and (a1 > e5) and (a1 > f6):
    print('Мода = 1')
if (b2 > a1) and (b2 > c3) and (b2 > d4) and (b2 > e5) and (b2 > f6):
    print('Мода = 2')
if (c3 > b2) and (c3 > a1 ) and (c3 > d4) and (c3 > e5) and (c3 > f6):
    print('Мода = 3')
if (d4 > b2) and (d4 > c3) and (d4 > a1) and (d4 > e5) and (d4 > f6):
    print('Мода = 4')
if (e5 > b2) and (e5 > c3) and (e5 > d4) and (e5 > a1) and (e5 > f6):
    print('Мода = 5')
if (f6 > b2) and (f6 > c3) and (f6 > d4) and (f6 > e5) and (f6 > a1):
    print('Мода = 6')

print('Средняя квадратов - ', sr_qv)
print('Выборочная дисперсия (Dв) - ', v_dispersia)
print('Среднее отклонение -  ', st_otcl)
print('Коэффициент вариации - ', kf_v)
print('Медиана - ', (l_s[9] + l_s[10])/2)


# Задание 2.
x1 = v_srednya - st_otcl
x2 = v_srednya + st_otcl
print(x1, '<', 3.5, '<', x2)

