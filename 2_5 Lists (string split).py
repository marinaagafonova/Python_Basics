#Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

numbers = [int(i) for i in raw_input().split(" ")];
result = 0;
for i in numbers:
    result += i;
print(result);
