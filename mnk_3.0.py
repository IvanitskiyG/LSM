import os
import mnk_core_3_0 as core
os.system('color 0a')
core.st()
import matplotlib.pyplot as plt
os.system('cls')
os.system('title Метод наименьших квадратов 3.0')
defaultcfg = '''TITLE=Исходные данные и приближение
X=t, с
Y=ln(h/h0)
MODE=2'''
desc = {'TITLE': 'Название графика',
        'X':     'Название оси X\t',
        'Y':     'Название оси Y\t',
        'MODE':  'Режим работы\t'}
state = 'main'
while True:
    if state == 'exit':
        break
    if state == 'main':
        print('Метод наименьших квадратов v3.0')
        print('©IGS Software, 2023\n')
        print('1.Настройки\n2.Работа с данными\n3.Выход')
        r = core.select(['1', '2', '3'])
        if r == '1':
            state = 'setup'
        elif r == '2':
            state = 'work'
        elif r == '3':
            state = 'exit'
        os.system('cls')
        continue
    if state == 'setup':
        print('1.Название графика\n2.Название оси X\n3.Название оси Y\n4.Режим работы\n5.Сброс настроек\n6.Вывод настроек\n7.Главное меню')
        r = core.select(['1', '2', '3', '4', '5', '6', '7'])
        if r == '7':
            state = 'main'
            os.system('cls')
            continue
        if r == '5':
            f = open('cfg.txt', 'w')
            print(defaultcfg, file=f, end='')
            f.close()
            os.system('cls')
            continue
        f = open('cfg.txt', 'r')
        d = {}
        for line in f.readlines():
            a, b = line.split('=')
            b = b.strip()
            d[a] = b
        f.close()
        if r == '6':
            for k in d.keys():
                print(desc[k], d[k], sep='\t')
            print('Нажмите ENTER для продолжения')
            input()
            os.system('cls')
            continue
        if r == '1':
            print('Введите название графика, нельзя использовать знак "="')
            d['TITLE'] = input()
        elif r == '2':
            print('Введите название оси X, нельзя использовать знак "="')
            d['X'] = input()
        elif r == '3':
            print('Введите название оси Y, нельзя использовать знак "="')
            d['Y'] = input()
        elif r == '4':
            print('Выберите, к какой функции приближать данные.\n1. y = kx\n2. y = kx + b')
            d['MODE'] = core.select(['1', '2'])
        f = open('cfg.txt', 'w')
        for k in d.keys():
            s = k + '=' + d[k]
            print(s, file=f)
        f.close()
        os.system('cls')
        continue
    elif state == 'work':
        print('1.Ручной ввод\n2.Ввод из файла\n3.Главное меню')
        r = core.select(['1', '2', '3'])
        if r == '3':
            state = 'main'
            os.system('cls')
            continue
        elif r == '1':
            lx, ly = core.get_input_man()
        elif r == '2':
            lx, ly = core.get_input_f()
        f = open('cfg.txt')
        d = {}
        for line in f.readlines():
            a, b = line.strip().split('=')
            d[a] = b
        f.close()
        if d['MODE'] == '1':
            k = core.mnk_1(lx, ly)
            b = 0
            print('y = kx')
            print('k =', k)
        elif d['MODE'] == '2':
            k, b = core.mnk_2(lx, ly)
            print('y = kx + b')
            print('k =', k)
            print('b =', b)
        print('Построение графика...\n')        
        ty = [k * x + b for x in lx]
        plt.title(d['TITLE'])
        plt.xlabel(d['X'])
        plt.ylabel(d['Y'])
        plt.grid()
        plt.scatter(lx, ly)
        plt.plot(lx, ty, '-')
        plt.show()
        print('Нажмите ENTER для продолжения')
        input()
        os.system('cls')
        continue
