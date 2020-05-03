# *-* coding: utf-8 *-*

from Permutation import *
from StabilizerChain import *
from sys import stdout



def example_permutations():
    
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - -\n')
    
    print('Пример работы с перестановками\n')
    
    a = Permutation([3, 4, 1, 2, 6, 7, 5])
    print('a =', a)
    
    b = to_perm([1, 5, 4, 3, 2])
    print('b =', b)
    
    c = to_perm('(5 7 1 4 8)')
    print('c =', c)
    print()
    
    print('a * b =', a * b)
    print('b * a =', b * a)
    print()
    
    print('b * c =', b * c)
    print('c * b =', c * b)
    print()
    
    print('a ^ 0 =', a ** 0)
    print('a ^ 1 =', a ** 1)
    print('a ^ 3 =', a ** 3)
    print('a ^ 226 =', a ** 226)
    print('a ^ 123456789 =', a ** 123456789)
    print('a ^ -1 =', a ** -1)
    print('a ^ -2 =', a ** -2)
    print()
    
    print('ord(a) =', a.ord())
    print('ord(b) =', b.ord())
    print()
    
    print('a = b ?', a == b)
    print('c = (8 5 7 1 4) ?', c == to_perm('(8 5 7 1 4)'))
    
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - -\n')



def example_A_5():
    
    print('Пример работы с группой A_5\n')
    
    a = Permutation([2, 3, 1, 4, 5])
    b = Permutation([1, 3, 4, 2, 5])
    c = Permutation([1, 2, 4, 5, 3])
    
    print('Образующие A_5:')
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print()
    
    A_5 = StabilizerChain([a, b, c])
    
    print('|A_5| =', A_5.ord())
    print()
    
    print('Орбита 1: ', A_5.get_orbit(1))
    print('Орбита 2 в Stab_1:', A_5[1].tree.get_orbit())
    print('Образующие Stab_{1, 2}:', A_5.get_gen_set(2))
    print()
    
    print('Сильное порождающее множество для A_5:')
    print(A_5.get_strong_gen_set())
    print()
    
    sigma = Permutation([2, 1, 3, 4, 5])
    print('Сожержится ли', sigma, 'в A_5?', A_5.contains(sigma))
    print()
    
    sigma = Permutation([2, 1, 4, 3, 5])
    print('Содержится ли', sigma, 'в A_5?', A_5.contains(sigma))
    print()
    
    print('Разложение через Сильное порождающее множество:')
    print(sigma, '=', A_5.contains(sigma, need_decomp = True))
    
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - -\n')



def example_G():
    
    print('Пример работы с группой G = A_4 x S_3\n')
    
    a = to_perm('(1 2 3)')
    b = to_perm('(1 3 4)')
    c = to_perm('(5 6)')
    d = to_perm('(6 7)')
    
    print('Образующие G:')
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)
    print()
    
    G = StabilizerChain([a, b, c, d])
    
    print('|G| =', G.ord())
    print()
    
    print('Орбита 1:', G.get_orbit(1))
    print('Орбита 7:', G.get_orbit(7))
    print('Орбита 6 в Stab_5:', G[5].tree.get_orbit())
    print('Образующие Stab_1:', G.get_gen_set(1))
    print()
    
    print('Сильное порождающее множество для G:')
    print(G.get_strong_gen_set())
    print()
    
    sigma = to_perm('(1 2 3 4 5)')
    print('Сожержится ли', sigma, 'в G?', G.contains(sigma))
    print()
    
    sigma = to_perm('(3 1 4)')
    print('Содержится ли', sigma, 'в G?', G.contains(sigma))
    print()
    
    print('Разложение через Сильное порождающее множество:')
    print(sigma, '=', G.contains(sigma, need_decomp = True))
    
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - -\n')



def my_task():
    
    '''
    
    Условие задачи
    
    Цыганка гадает вам на картах. Она раскладывает 56 карт из младшей колоды таро на столе в семь рядов по 8 карт в каждом (сначала она заполняет верхний ряд слева направо, а потом переходит к следующему и т.д.). Потом она собирает карты обратно в колоду по столбцам (сверху оказывается карта в левом верхнем углу, снизу в правом нижнем). Собирая карты, цыганка может немного их перемешать, снимая верхнюю половину колоды и кладя её под низ.
    
    Цыганка хочет добиться воспроизводимости гадания (полезно для бизнеса).
    
    1). Какими способами она может тасовать карты так, чтобы сверху оставалась та же карта, которая была там до тасования?
    
    2). Может ли она при этом подложить под верхнюю карту любую другую заранее выбранную, и если да, то каким количеством способов?
    
    '''
    
    print('Тестовая задача\n')
    
    print('Перестановки, порождающие группу G: ') # как я понял из условия
    a = Permutation([1, 9, 17, 25, 33, 41, 49, 2, 10, 18, 26, 34, 42, 50, 3, 11, 19, 27, 35, 43, 51, 4, 12, 20, 28, 36, 44, 52, 5, 13, 21, 29, 37, 45, 53, 6, 14, 22, 30, 38, 46, 54, 7, 15, 23, 31, 39, 47, 55, 8, 16, 24, 32, 40, 48, 56])
    
    b = Permutation([29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
    
    print('a =', a) # (2 ... 8)(4 ... 22)(6 ... 36)(12 ... 23)
    print('b =', b) # (1 29)(2 30)(3 31)(4 32)...(27 55)(28 56)
    print()
    stdout.flush()
    
    
    # Строим полную цепочку стабилизаторов
    G = StabilizerChain([a, b])
    
    
    print('|G| =', G.ord()) # 20460710453732638271310403731456000000
    
    stab_1 = G.ord() // len(G[0].tree)
    print('|Stab_1| =', stab_1) # 365369829530939969130542923776000000
    print()
    
    print('Орбита второй карты в Stab_1 =', G[1].tree.get_orbit()) # {2, 3, 4, ..., 54, 55}
    # -> Для всех чисел, кроме {1, 56} ответ на 2-ой вопрос - Можно
    print()
    
    # Количество способов поместить 2-ую карту под 1-ую
    stab_12 = G.ord() // len(G[0].tree) // len(G[1].tree)
    print('|Stab_{1, 2}| =', stab_12) # 6766107954276666095010054144000000
    
    # Всего элементов, сохраняющих 1, но не сохраняющих 2
    print('|Stab_1| - |Stab_{1, 2}| =', stab_1 - stab_12) # 358603721576663303035532869632000000
    
    print('\n- - - - - - - - - - - - - - - - - - - - - - - - -\n')



if __name__ == '__main__':
    
    example_permutations()
    example_A_5()
    example_G()
    
    # Исполнение my_task() займёт ~ 15 минут
    # my_task()