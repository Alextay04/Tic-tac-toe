matrix = [['_','_','_'],['_','_','_'],['_','_','_']]
print("НУМЕРАЦИЯ СТРОК И СТОЛБЦОВ НАЧИНАЕТСЯ С 1!!!")
print('ЧТОБЫ ЗАКОНЧИТЬ ИГРУ ВВЕДИТЕ "111"')

def start():
    for row in (matrix):
        print("")
        for col in(row):
            print(col,end=" ")
    print("")

first_name = str(input('Введите имя первого игрока '))
second_name = str(input('Введите имя второго игрока '))

#начало игры 
while True:
#первый ход
    symbol_X_row = int(input(first_name+ ", введите строку "))
    if symbol_X_row == 111:
        print("Игра закончена")
        break
    symbol_X_col = int(input(first_name+', введите столбец '))
    if symbol_X_col == 111:
        print("Ирга закончена")
        break
    matrix[symbol_X_row - 1][symbol_X_col - 1] = "X"
    start()
    if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X":
        print("Победил "+first_name+"!")
        break
    if matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X":
        print("Победил "+first_name+"!")
        break
    if matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X":
        print("Победил "+first_name+"!")
        break
    if matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X":
        print("Победил "+first_name+"!")
        break
    if matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
        print("Победил "+first_name+"!")
        break 
    if matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] =="X":
        print("Победил "+first_name+"!")
        break
    if matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X":
        print("Победил "+first_name+"!")
        break 
    if matrix[2][0] == "X" and matrix[1][1] == "X" and matrix[0][2] == "X": 
        print("Победил "+first_name+"!")
        break
    
#второй ход
    symbol_Y_row = int(input(second_name+', введите строку '))
    if symbol_Y_row == 111:
        print("Игра окончена")
        break 
    symbol_Y_col = int(input(second_name+', введите столбец '))
    if symbol_Y_col == 111:
        break
        print("Игра окончена") 
    matrix[symbol_Y_row - 1][symbol_Y_col - 1] = "O"
    start()
    if matrix[0][0] =="O" and matrix[0][1] =="O" and matrix[0][2] == "O":
        print("Победил " +second_name+"!")
        break
    if matrix[1][0] =="O" and matrix[1][1] =="O" and matrix[1][2] == "O":
        print("Победил " +second_name+"!")
        break
    if matrix[2][0] =="O" and matrix[2][1] =="O" and matrix[2][2] == "O":
        print("Победил " +second_name+ "!")
        break
    if matrix[0][0] =="O" and matrix[0][1] =="O" and matrix[0][2] == "O":
        print("Победил " +second_name+"!")
        break
    if matrix[0][1] =="O" and matrix[1][1] =="O" and matrix[2][1] == "O":
        print("Победил " +second_name+"!")
        break
    if matrix[0][2] =="O" and matrix[1][2] =="O" and matrix[2][2] == "O":
        print("Победил " +second_name+"!")
        break
    if matrix[0][0] =="O" and matrix[1][1] =="O" and matrix[2][2] == "O":
        print("Победил " +second_name+"!")
        break
    if matrix[2][0] =="O" and matrix[1][1] =="O" and matrix[0][2] == "O":
        print("Победил " +second_name+"!")
        break


    
    


