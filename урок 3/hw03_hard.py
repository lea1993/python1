# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
norm_hors = 185
f = open('data_hours_of.txt', 'r', encoding='UTF-8')
nam = f.read()
nam_all = nam.split()
l_cont = []
n = 1
for ind, i in enumerate(nam_all):
    if ind == n:
        l_cont.append(i)
        n += 2
l_cont = list(map(int, l_cont))
norm_mon = 10000
new_mon = []
for i in l_cont:
    coff = round(i / 185, 2)
    new_mon.append(coff * norm_mon)
    new_mon = list(map(str, new_mon))
c = 0
n = 1
for ind, i in enumerate(nam_all):
    for j in new_mon:
        if ind == n:
            nam_all.remove(i)
            nam_all.insert(ind, new_mon[c])
            n += 2
            c += 1
nam_all = ', '.join(nam_all)
with open('workers.txt', 'w', encoding='UTF-8') as d:
    d.write(nam_all + '\n')
f.close
     

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

#list_all = list(map(chr, range(ord('А'), ord('Я') +1)))
#f = open('data_fruits.txt', 'r', encoding='UTF-8')
#nam = f.read()
#nam_all = nam.split()
#print(nam_all)
#for i in nam_all:
#    for j in list_all:
#        list_j = []
#        if i[0] == j:
#            list_j.append(i)
#       # list_i[0] = []
#    print(list_j)
#f.close
     