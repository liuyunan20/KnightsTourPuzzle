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


def start_board(position, dimension):
    m = dimension[0]
    n = dimension[1]
    x = position[0]
    y = position[1]
    board = [['__' for a in range(m)] for b in range(n)]
    board[y - 1][x - 1] = " X"
    return board


def display_board(cur_position, cur_board):
    dp_board = [[x for x in y] for y in cur_board]
    x = cur_position[0]
    y = cur_position[1]
    m = len(cur_board[0])
    n = len(cur_board)
    predict_move(cur_position, dp_board)
    return dp_board


def predict_move(cur_position, cur_board):
    next_positions = possible_moves(cur_position, cur_board)
    for next_position in next_positions:
        predict_positions = possible_moves(next_position, cur_board)
        next_x = next_position[0]
        next_y = next_position[1]
        cur_board[next_y - 1][next_x - 1] = f" {len(predict_positions)}"


def check_move_available(position, cur_board):
    x = position[0]
    y = position[1]
    m = len(cur_board[0])
    n = len(cur_board)
    if 1 <= x <= m and 1 <= y <= n and cur_board[y - 1][x - 1] != " X" and cur_board[y - 1][x - 1] != " *":
        return True
    else:
        return False


def possible_moves(cur_position, cur_board):
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
    moves = [move for move in possible_move if check_move_available(move, cur_board)]
    return moves


def process_move(pre_position, cur_board):
    while True:
        cur_position = input("Enter your next move: ")
        cur_position = check_type(cur_position, "move")
        if cur_position is None:
            continue
        elif cur_position in possible_moves(pre_position, cur_board):
            return cur_position
        else:
            print_invalid("move")


def update_board(cur_position, cur_board):
    for y in range(len(cur_board)):
        for x in range(len(cur_board[0])):
            if cur_board[y][x] == " X":
                cur_board[y][x] = " *"
    x = cur_position[0]
    y = cur_position[1]
    cur_board[y - 1][x - 1] = " X"
    return cur_board


def count_moves(cur_board):
    steps = 0
    for y in cur_board:
        for x in y:
            if x == " X" or x == " *":
                steps += 1
    return steps


def check_win(cur_board):
    for y in cur_board:
        if "__" in y:
            return False
    return True


def check_end(cur_position, cur_board):
    moves = possible_moves(cur_position, cur_board)
    if check_win(cur_board):
        print("What a great tour! Congratulations!")
        return True
    elif not moves:
        print("No more possible moves!")
        print(f"Your knight visited {count_moves(cur_board)} squares!")
        return True
    else:
        return False


dimension_in = check_dimension()
c_position = check_position(dimension_in)
c_board = start_board(c_position, dimension_in)
while True:
    d_board = display_board(c_position, c_board)
    print_board(d_board)
    p_position = [x for x in c_position]
    c_position = process_move(p_position, c_board)
    c_board = update_board(c_position, c_board)
    if check_end(c_position, c_board):
        break
