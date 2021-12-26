def check_type(user_in):
    try:
        d = user_in.split()
        if len(d) > 2:
            print("Invalid dimensions!")
            return False
        else:
            user_in_1 = int(d[0])
            user_in_2 = int(d[1])
    except ValueError:
        print("Invalid dimensions!")
        return False
    except IndexError:
        print("Invalid dimensions!")
        return False
    else:
        return [user_in_1, user_in_2]


def check_dimension():
    while True:
        dimension = input("Enter your board dimensions: ")
        dimension = check_type(dimension)
        if dimension[0] > 0 and dimension[1] > 0:
            return dimension
            break
        else:
            print("Invalid dimensions!")
            return None


def check_position(dimension):
    while True:
        position = input("Enter the knight's starting position: ")
        position = check_type(position)
        if 1 <= position[0] <= dimension[0] and 1 <= position[1] <= dimension[1]:
            return position
        else:
            print("Invalid position!")
            return None


def print_board(board):
    bottom = [str(i) for i in range(1, m + 1)]
    print(f" {'-' * (3 + 3 * len(board))}")
    for i in range(len(board), 0, -1):
        print(f"{i}| {' '.join(board[i-1])} |")
    print(f" {'-' * (3 + 3 * len(board))}")
    print(f"    {'  '.join(bottom)}")


def build_board(dimension, position):
    m = dimension[0]
    n = dimension[1]
    x = position[0]
    y = position[1]
    board = [['__' for a in range(m)] for b in range(n)]
    board[y - 1][x - 1] = " X"
    return board


dimension_in = check_dimension()
position_in = check_position(dimension_in)
c_board = build_board(dimension_in, position_in)
print_board(c_board)
