Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. 
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].

Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. 
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

a1 = int(input());
a2 = int(input());
b1 = int(input());
b2 = int(input());
for i in range (b1,b2+1):
    print('\t'+str(i),end='');
print(end='\n');
for i in range (a1,a2+1):
    print(str(i)+'\t',end='');
    for j in range (b1,b2+1):
        print(str(i*j),end='\t');
    print(end='\n');
