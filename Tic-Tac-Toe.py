matrix = [['_','_','_'],['_','_','_'],['_','_','_']]
print("НУМЕРАЦИЯ СТРОК И СТОЛБЦОВ НАЧИНАЕТСЯ С 1!!!")
print('ЧТОБЫ ЗАКОНЧИТЬ ИГРУ ВВЕДИТЕ "111"')

def start():
    for row in (matrix):
        print("")
        for col in(row):
            print(col,end=" ")
    print("")

def first_move():
    symbol_X_row = int(input(first_name+ ", введите строку "))
    symbol_X_col = int(input(first_name+', введите столбец '))
    matrix[symbol_X_row - 1][symbol_X_col - 1] = "X"
    start()

def second_move():
    symbol_Y_row = int(input(second_name+', введите строку '))
    symbol_Y_col = int(input(second_name+', введите столбец '))
    matrix[symbol_Y_row - 1][symbol_Y_col - 1] = "0"
    start()

def win0():
    if matrix[0][0] and matrix[0][1] and matrix[0][2] == "0":
        print("Победил "+second_name)
    elif matrix[1][0] and matrix[1][1] and matrix[1][2] == "0":
        print("Победил "+second_name)
    elif matrix[2][0] and matrix[2][1] and matrix[2][2] == "0":
        print("Победил"+second_name)
    elif matrix[0][0] and matrix[0][1] and matrix[0][2] == "0":
        print("Победил "+cond_name)
    elif matrix[0][1] and matrix[1][1] and matrix[2][1] == "0":
        print("Победил "+second_name)
    elif matrix[0][2] and matrix[1][2] and matrix[2][2] =="0":
        print("Победил "+second_name)
    elif matrix[0][0] and matrix[1][1] and matrix[2][2] == "0":
        print("Победил "+second_name)
    elif matrix[2][0] and matrix[1][1] and matrix[0][2] == "0":
        print("Победил "+second_name) 

def winx():
    if matrix[0][0] and matrix[0][1] and matrix[0][2] == "x":
        print("Победил "+a)
    elif matrix[1][0] and matrix[1][1] and matrix[1][2] == "x":
        print("Победил "+a)
    elif matrix[2][0] and matrix[2][1] and matrix[2][2] == "x":
        print("Победил"+a)
    elif matrix[0][0] and matrix[1][0] and matrix[2][0]  == "x":
        print("Победил "+a)
    elif matrix[0][1] and matrix[1][1] and matrix[2][1] == "x":
        print("Победил "+a)
    elif matrix[0][2] and matrix[1][2] and matrix[2][2] =="x":
        print("Победил "+a)
    elif matrix[0][0] and matrix[1][1] and matrix[2][2] == "x":
        print("Победил "+a)
    elif matrix[2][0] and matrix[1][1] and matrix[0][2] == "x":
        print("Победил "+a)





first_name = str(input('Введите имя первого игрока '))
second_name = str(input('Введите имя второго игрока '))

active = True
while True:
    symbol_X_row = int(input(first_name+ ", введите строку "))
    symbol_X_col = int(input(first_name+', введите столбец '))
    matrix[symbol_X_row - 1][symbol_X_col - 1] = "X"
    start()
    if matrix[0][0] and matrix[0][1] and matrix[0][2] == "x":
        break
        print("Победил "+first_name+"!")
    elif matrix[1][0] and matrix[1][1] and matrix[1][2] == "x":
        active = False
        print("Победил "+first_name+"!")
    elif matrix[2][0] and matrix[2][1] and matrix[2][2] == "x":
        active = False
        print("Победил "+first_name+"!")
    elif matrix[0][0] and matrix[1][0] and matrix[2][0]  == "x":
        active = False
        print("Победил "+first_name+"!")
    elif matrix[0][1] and matrix[1][1] and matrix[2][1] == "x":
        active = False
        print("Победил "+first_name+"!")
    elif matrix[0][2] and matrix[1][2] and matrix[2][2] =="x":
        active = False
        print("Победил "+first_name+"!")
    elif matrix[0][0] and matrix[1][1] and matrix[2][2] == "x":
        active = False
        print("Победил "+first_name+"!")
    elif matrix[2][0] and matrix[1][1] and matrix[0][2] == "x": 
        active = False
        print("Победил "+first_name+"!")
    symbol_Y_row = int(input(second_name+', введите строку '))
    symbol_Y_col = int(input(second_name+', введите столбец '))
    matrix[symbol_Y_row - 1][symbol_Y_col - 1] = "0"
    start()
    
        #active = False
        #print("Победил "+second_name+"!")
    #if symbol_X_row == 111 or symbol_X_col == 111 or symbol_Y_row == 111 or symbol_Y_col == 111:
     #   break
     #  print("Игра окончена")


