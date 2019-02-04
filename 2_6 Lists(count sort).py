'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

numbers = [int(i) for i in input().split()];
numbers.sort();
result = [];
char = "";
if (len(numbers)>1):
    for i in numbers:
        if(numbers.count(i)>1 and char!=str(i)):
            result.append(i)
            char = str(i);
    for i in range(len(result)):
        print(str(result[i])+' ',end='');
