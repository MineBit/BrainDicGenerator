#!/usr/bin/env python
 
import string
from os import system
 
    # Создание переменных;
ABC = ''
goflag = False
Alphs = {'1':string.ascii_uppercase, '2':string.ascii_lowercase, '3':string.digits, '4':string.punctuation}
 
    # Приветствие; выбор составляющих алфавита;
while goflag == False:
    print('| BRUTELIST CREATOR V0.2')
    print('| Выберите наборы символов: ')
    print('| 1) EN (Прописные)')
    print('| 2) en (Строчные)')
    print('| 3) Цифры')
    print('| 4) Пунктуационные знаки')
    IDs = input('| Введите подряд номера выбранных наборов: ')
    system('cls')
    goflag = True
    for n in IDs:   # Проверка на правильность ввода;
        if not(n in Alphs):
            print('Ошибка!')
            input()
            system('cls')
            goflag = False
        
    # Создание алфавита;
for n in IDs:
    ABC = ABC+Alphs[n]
 
    # Создание диапазона;
print('| BRUTELIST CREATOR V0.1')
min_symb = int(input('| Введите минимальное количество символов в пароле: '))
max_symb = int(input('| Введите максимальное количество символов в пароле: '))
system('cls')
 
    # Создание имён файлов и количества паролей в каждом файле;
print('| BRUTELIST CREATOR V0.1')
f_name = input('| Назовите словарь с полученными паролями: ')
pass_amount = int(input('| Введите количество паролей в каждой части словаря: '))
system('cls')
 
    # Функция вывода пароля;
def passout(st):
    cpass = ''
    for i in st:
        cpass = cpass + ABC[i]
    f.write(cpass+'\n')
    print('| \/ |   '+cpass)
 
    # Создание "БрутЛиста";
cpassout = ''
p_num = 0
f_num = 0
f = open((f_name+str(f_num)+'.txt'), 'w')
for curlength in range(min_symb,max_symb+1):  # Перебор длин паролей в заданном диапазоне;
    password = []   # Обнуление пароля;
    for i in range(curlength):
        password.append(0)
        if p_num == pass_amount:    # Запись в новый файл при необходимости.
            f.close()
            f_num += 1
            f = open((f_name+str(f_num)+'.txt'), 'w')
            p_num = 0
    passout(password)
    p_num += 1
    contr = [len(ABC)-1 for x in password] # Создание контольного значения;
    while password != contr:   # Пока не закончатся комбинации;
        password[len(password)-1] += 1  # Прибавление единицы в конец списка;
        if len(ABC) in password:  # Переход единицы на следующий уровень;
            j = len(password)-1
            while len(ABC) in password:
                password[j] = 0
                password[j-1] += 1
                j += -1
        if p_num == pass_amount:    # Запись в новый файл при необходимости.
            f.close()
            f_num += 1
            f = open((f_name+str(f_num)+'.txt'), 'w')
            p_num = 0
        passout(password)
        p_num += 1
f.close()
print('| Пароли сохранены в '+f_name+'0 - '+str(f_num)+'.txt')
print('| Успехов!')
input('| Нажмите ENTER, чтобы закрыть программу.')