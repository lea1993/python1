# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
  nums = list(range(n,m))
  for i in nums:
    F = int(((((1 + 5 ** 0.5) / 2) ** i) - (((1 - 5 ** 0.5) / 2) ** i)) / (5 ** 0.5))
    i += 1
    print(F)
print(fibonacci(4,7))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
  num = len(origin_list)
  for i in range(num-1):
    for j in range(num-1-i-1):
      if origin_list[j] > origin_list[j+1]:
        origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]
      if origin_list[-1] < origin_list[-2]:
        origin_list[-1] += origin_list[-2]
        origin_list[-2] = origin_list[-1] - origin_list[-2]
        origin_list[-1] = origin_list[-1] - origin_list[-2]
 
  print(origin_list)
 
origin_list = [2, 5, 3, 7, 3, 9, 1]
print(sort_to_max(origin_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filt_2(a):
  for i in a:
    if i%2 == 0:
      a.remove(i)
    else:
      continue
    print(a)
a = [2, 5, 7, 3, 9, 1]
print(filt_2(a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a = list(map(int, input('Введите значение точки А: ').split(',')))
b = list(map(int, input('Введите значение точки B: ').split(',')))
c = list(map(int, input('Введите значение точки C: ').split(',')))
d = list(map(int, input('Введите значение точки D: ').split(',')))
def int(a, b, c, d):
  a_b = (((b[0] - a[0]) ** 0.5) + ((b[1] - a[1]) ** 0.5)) ** 0.5
  d_c = (((d[0] - c[0]) ** 0.5) + ((d[1] - c[1]) ** 0.5)) ** 0.5
  b_c = (((c[0] - b[0]) ** 0.5) + ((c[1] - b[1]) ** 0.5)) ** 0.5
  a_d = (((d[0] - a[0]) ** 0.5) + ((d[1] - a[1]) ** 0.5)) ** 0.5
  if a_b == d_c and b_c == a_d:
    print('точки являются вершинами паралеллограмма')
  else:
    print('точки не являются вершинами параллелограмма')
print(int(a, b, c, d))