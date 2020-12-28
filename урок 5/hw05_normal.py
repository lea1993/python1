# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from hw05_easy import list_dir, rmdir, mkdir
import os
def change_dir(folden):
    try:
        os.chdir(folden)
        print('перешел в папку')
    except FileNotFoundError:
        print('нет папки')
do = {
    1: change_dir,
    2: list_dir,
    3: rmdir,
    4: mkdir
}

while True:
    choice = input('выбрать действие:\n'
                   '1. перейти в папку\n'
                   '2. содержимое папки\n'
                   '3. удалить папку\n'
                   '4. создать папку\n'
                   '5. выход\n\n')
    try:
        if len(choice.split()) == 2:
            choice, folder_name = choice.split()
            choice = int(choice)
            if do.get(choice): #метод для работы с ключами если он есть возв3знач1если нет none
                do.get(choice)(folder_name)
        else:
            choice = int(choice)
            if choice == 5:
                break
            elif do.get(choice):
                print(do.get(choice)())
    except ValueError:
        print('не верные данные')
    except TypeError:
        print('нет имени файла')

