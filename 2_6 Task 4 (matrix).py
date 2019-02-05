'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, 
содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы 
на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

matrix = []
while True:
    temp = input()
    if temp == "end":
        break
    matrix.append([int(i) for i in temp.split()]) 
rows = len(matrix)
columns = len(matrix[0])
result = [[sum([matrix[i-1][j], matrix[(i+1)%rows][j], matrix[i][j-1], matrix[i][(j+1)%columns]]) for j in range(columns)] for i in range(rows)]
for i in range (rows):
    for j in range (columns):
        print(str(result[i][j]) + ' ', end = '')
    print()
