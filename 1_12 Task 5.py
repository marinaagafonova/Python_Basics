'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль 
в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
'''

a = int(input());
b = int(input());
c = int(input());

if a>b:
    if a>c:
        if b>c:
            print (a, '\n', c, '\n', b);
        else: 
            print(a, '\n', b, '\n', c);
    else:
        print(c, '\n', b, '\n', a);
else:   
    if b>c:
        if a>c:
            print(b, '\n', c, '\n', a);
        else:
            print(b, '\n', a, '\n', c);
    else:
        print(c, '\n', a, '\n', b);
