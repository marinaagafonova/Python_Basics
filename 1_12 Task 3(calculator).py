Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, 
после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

a = float(input());
b = float(input());
oper = input();
if oper =="+":
    print(a+b);
if oper == "-":
    print(a-b);
if oper == "*":
    print(a*b);
if oper == "pow":
    print(a**b);
if oper == "/" or oper=="div" or oper=="mod":
    if b==0:
        print("Деление на 0!");
    else:
        if oper == "/":
            print(a/b);
        if oper == "div":
            print(a//b);
        if oper == "mod":
            print(a%b);