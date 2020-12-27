# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
  tempary_num = 10 ** (ndigits + 2)
  num_pl = number % 1 # остаток
  number = number + 0.5 / (10 **  ndigits )
  num_int = int(number)
  oun_wr = int(number * (10 ** ndigits))
  rec = oun_wr / (10 **ndigits)
  print(rec)
 
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    num_1 = []
    num_2 = map(int, str(number))
    for i in num_2:
        num_1.append(i)
        if sum(num_1[:3]) == sum(num_1[3:]):
            print('lucky ')
        else:
            print('unlucky')


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))



