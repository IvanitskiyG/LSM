#©IGS Software, 2023


s = '''
###  ###   ####      ####  ###  ##### ### # # #  ##  ####  #####
 #  #   # #         #     #   # #      #  # # # #  # #   # #   
 #  #      ###       ###  #   # ###    #  # # # #### ####  ###
 #  #   #     #         # #   # #      #  # # # #  # # #   #    
###  #### ####      ####   ###  #      #   # #  #  # #  ## #####
'''

def st():
    print(s)


def select(l):
    x = []
    while x not in l:
        x = input().lower()
    return x


def mnk_1(lx, ly):
    #y = kx
    n = len(lx)
    c = 0
    z = 0
    for i in range(n):
        c += lx[i] * ly[i]
        z += lx[i] ** 2
    k = c / z
    return k


def mnk_2(lx, ly):
    #y = kx + b
    n = len(lx)
    a = 0
    b = 0
    for i in range(n):
        a += lx[i] * ly[i]
        b += lx[i] ** 2
    k = (a * n - sum(lx) * sum(ly)) / (b * n - sum(lx) ** 2)
    b = (sum(ly) - k * sum(lx)) / n
    '''rc = 0; sy2 = 0; sx2 = 0
    for i in range(n):
        rc += lx[i] * ly[i]
        sx2 += lx[i] ** 2
        sy2 += ly[i] ** 2
    rc = rc * n - sum(lx) * sum(ly)
    rz = ((n * sx2 - sum(lx) ** 2) * (n * sy2 - sum(ly) ** 2)) ** 0.5'''
    return k, b


def get_input_man():
    print('Вводите x и y через пробел; пустая строка = конец данных')
    lx, ly = [], []
    s = input().strip().replace(',', '.')
    while s != '':
        if s.count(' ') != 1:
            print('Некорректные данные, повторите ввод')
            continue
        x, y = map(float, s.split())
        lx.append(x)
        ly.append(y)
        s = input().strip().replace(',', '.')
    return lx, ly


def get_input_f():
    print('Введите название файла')
    lx, ly = [], []
    while True:
        try:
            filename = input().strip()
            f = open(filename, 'r')
            break
        except FileNotFoundError:
            print('Такого файла не существует, повторите ввод')    
    for line in f.readlines():
        x, y = map(float, line.replace(',', '.').split())
        print(x, y)
        lx.append(x)
        ly.append(y)
    f.close()
    print('Введены данные из файла', filename)
    return lx, ly
