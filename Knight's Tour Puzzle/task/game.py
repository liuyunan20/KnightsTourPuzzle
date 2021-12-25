def check_dimension(dimension):
    global m
    global n
    try:
        d = dimension.split()
        if len(d) > 2:
            print("Invalid dimensions!")
            return False
        else:
            m = int(d[0])
            n = int(d[1])
    except ValueError:
        print("Invalid dimensions!")
        return False
    except IndexError:
        print("Invalid dimensions!")
        return False
    else:
        if m > 0 and n > 0:
            return True
        else:
            print("Invalid dimensions!")
            return False


def check_position(position):
    global x
    global y
    try:
        p = position.split()
        if len(p) > 2:
            print("Invalid position!")
            return False
        else:
            x = int(p[0])
            y = int(p[1])
    except ValueError:
        print("Invalid position!")
        return False
    except IndexError:
        print("Invalid position!")
        return False
    else:
        if 1 <= x <= m and 1 <= y <= n:
            return True
        else:
            print("Invalid position!")
            return False


def print_board(board):
    bottom = [str(i) for i in range(1, m + 1)]
    print(f" {'-' * (3 + 3 * m)}")
    for i in range(len(board), 0, -1):
        print(f"{i}| {' '.join(board[i-1])} |")
    print(f" {'-' * (3 + 3 * m)}")
    print(f"    {'  '.join(bottom)}")


m = 0
n = 0
while True:
    dimension_in = input("Enter your board dimensions: ")
    if check_dimension(dimension_in):
        break

c_board = [['__' for x in range(m)] for y in range(n)]
x = 0
y = 0

while True:
    position_in = input("Enter the knight's starting position: ")
    if check_position(position_in):
        break
c_board[y - 1][x - 1] = " X"
print_board(c_board)
