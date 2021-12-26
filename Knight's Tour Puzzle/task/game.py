def print_invalid(invalid_type):
    print(f"Invalid {invalid_type}!")


def check_type(user_in, input_type):
    result = None
    try:
        d = user_in.split()
        if len(d) > 2:
            print_invalid(input_type)
        else:
            user_in_1 = int(d[0])
            user_in_2 = int(d[1])
    except ValueError:
        print_invalid(input_type)
    except IndexError:
        print_invalid(input_type)
    else:
        result = [user_in_1, user_in_2]
    return result


def check_dimension():
    while True:
        dimension = input("Enter your board dimensions: ")
        dimension = check_type(dimension, "dimensions")
        if dimension is None:
            continue
        elif dimension[0] > 0 and dimension[1] > 0:
            return dimension
        else:
            print_invalid("dimensions")


def check_position(dimension):
    while True:
        position = input("Enter the knight's starting position: ")
        position = check_type(position, "positions")
        if position is None:
            continue
        elif 1 <= position[0] <= dimension[0] and 1 <= position[1] <= dimension[1]:
            return position
        else:
            print_invalid("positions")


def print_board(board):
    bottom = [str(i) for i in range(1, len(board[0]) + 1)]
    print(f" {'-' * (3 + 3 * len(board[0]))}")
    for i in range(len(board), 0, -1):
        print(f"{i}| {' '.join(board[i-1])} |")
    print(f" {'-' * (3 + 3 * len(board[0]))}")
    print(f"    {'  '.join(bottom)}")


def build_board(position, dimension):
    m = dimension[0]
    n = dimension[1]
    x = position[0]
    y = position[1]
    board = [['__' for a in range(m)] for b in range(n)]
    board[y - 1][x - 1] = " X"
    next_positions = possible_moves(position, dimension)
    for next_position in next_positions:
        next_x = next_position[0]
        next_y = next_position[1]
        board[next_y - 1][next_x - 1] = " O"
    return board


def check_move_available(position, dimension):
    x = position[0]
    y = position[1]
    m = dimension[0]
    n = dimension[1]
    if 1 <= x <= m and 1 <= y <= n:
        return True
    else:
        return False


def possible_moves(cur_position, dimension):
    x = cur_position[0]
    y = cur_position[1]
    possible_move = [[x + 1, y + 2],
                     [x + 2, y + 1],
                     [x + 2, y - 1],
                     [x + 1, y - 2],
                     [x - 1, y - 2],
                     [x - 2, y - 1],
                     [x - 2, y + 1],
                     [x - 1, y + 2]]
    return [move for move in possible_move if check_move_available(move, dimension)]


dimension_in = check_dimension()
position_in = check_position(dimension_in)
c_board = build_board(position_in, dimension_in)
print("Here are the possible moves:")
print_board(c_board)
