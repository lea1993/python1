# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
def my_dir(path):
    try:
        os.mkdir(path)
        print('директория создана')
    except FileExistsError:
        print('директрия уже есть')

def del_dir(path):
    try:
        os.removedirs(path)
        print('директория удалена')
    except FileExistsError:
        print('директории нет')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def all_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    filename = sys.argv[0]
    with open(filename, 'r', encoding='UTF-8') as f:
        name, extnsion = filename.split('.') #это чтоб разделял имя и расширение
        with open(name + '_copy.' + extnsion, 'w', encoding='UTF-8') as s:
            s.write(f.read())

if __name__ == '__main__':
    dir_path = 'dir_()'
    [my_dir(dir_path.format(i)) for i in range(1,10)]
    [del_dir(dir_path.format(i)) for i in range(1,10)]

    all_dir()