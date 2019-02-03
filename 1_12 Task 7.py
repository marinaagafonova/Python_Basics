Счастливый билет или нет.

number = int(input());
if (number//1e5 + (number//1e4)%10 + (number//1e3)%10) == (number%10 + (number%100)//10 + (number%1000)//100):
    print("Счастливый");
else:
    print("Обычный");
