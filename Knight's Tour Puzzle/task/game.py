def check_input(position):
    global x
    global y
    try:
        p = position.split()
        if len(p) > 2:
            print("Invalid dimensions!")
            return False
        else:
            x = int(p[0])
            y = int(p[1])
    except ValueError:
        print("Invalid dimensions!")
        return False
    except IndexError:
        print("Invalid dimensions!")
        return False
    else:
        if 1 <= x <= 8 and 1 <= y <= 8:
            return True
        else:
            print("Invalid dimensions!")
            return False


def print_board(board):
    print("-------------------")
    for n in range(8, 0, -1):
        print(f"{n}| {' '.join(board[n-1])} |")
    print("-------------------")
    print("   1 2 3 4 5 6 7 8 ")


c_board = [['_' for x in range(8)] for y in range(8)]
x = 0
y = 0
while True:
    position_in = input("Enter the knight's starting position: ")
    if check_input(position_in):
        break
c_board[y - 1][x - 1] = "X"
print_board(c_board)
