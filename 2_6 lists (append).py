'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента 
этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", 
то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''

numbers = [int(i) for i in raw_input().split()];
result = [];
output = "";
lastIndex = len(numbers)-1;
if len(numbers)>0:
    if len(numbers)==0:
        print(0);
    else:
        for i in range(len(numbers)):
            temp = 0;
            if len(numbers)>1:
                if i==0:
                    temp = numbers[i+1] + numbers[-1]
                    result.append(temp)                # adding new element to "numbers" list
                elif i>0 and i<lastIndex:
                    temp = numbers[i-1] + numbers[i+1]
                    result.append(temp)
                elif i==lastIndex:
                    temp = numbers[i-1] + numbers[0]
                    result.append(temp)
            else:
                result.append(numbers[0]) 
        for i in range(len(result)):
            output += str(result[i]) + ' ';
print(output);
