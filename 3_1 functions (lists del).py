'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, 
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
'''

def modify_list(l):
    # put your python code here
    lastIndex = len(l) -1;
    while (lastIndex != -1):
        if (l[lastIndex]%2==1):
            del l[lastIndex]
        else:
            l[lastIndex] = l[lastIndex]//2
        lastIndex -=1;
