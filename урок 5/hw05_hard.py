# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

print('sys.argv = ', sys.argv)

def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('pink - тест')

    print('cp <file_name> - копия указанного файла')
    print('rm <file_name> - удаляет указанный файл (попросить подтверждение)')
    print('cd <file_name> - меняет текущую директорию на указанную')
    print('ls - полный путь в текущую директорию')
def make_dir():
    if not dir_name:
        print('2 параметр - имя директории')
        return
    try:
        os.mkdir(dir_name)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже создана'.format(dir_name))

def ping():
    print('pong')

def cp(filename):
    with open(filename, 'rb', encoding='UTF-8') as f:
        with open('copy_' + filename, 'wb', encoding='UTF-8') as s:
            s.write(f.read())

def rm(filename):
    res = input('вы уверены? y/n')
    if res == 'y':
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('файл не найден')

def ls():
    print(os.getcwd())

def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('нет директории')

do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': cp,
    'rm': rm,
    'cd': cd,
    'ls': ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        if key == 'cd' or key == 'cp' or key == 'rm':
            do[key](dir_name)
        else:
            do[key]()
    else:
        print('неверный ключ')
        print('укажите ключ help дла получения справки')
