# start


def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],
        'turn': 1
    }


def draw_board(game: dict[str, any]):
    board = game['board']
    # print(board)
    print(" ", end=" ")
    for i in range(1, 3 + 1):
        print(i, end=" ")
    print()

    mona: int = 1
    for shura in board:
        print(mona, end=" ")
        # print(in-shura, end=" ")
        for in_shure in shura:
            print(in_shure, end=" ")
        mona += 1
        print()


def input_square(game, x_or_o: str):
    board = game['board']
    while True:

        mikom_shora = int(input(f"{x_or_o} choose the mikom shora in 1-3: "))
        mikom_hamoda = int(input(f"{x_or_o} choose the mikom hamoda in 1-3: "))

        mikom_shora = mikom_shora-1
        mikom_hamoda = mikom_hamoda-1

        if mikom_shora < 0 or mikom_shora > 2 or mikom_hamoda < 0 or mikom_hamoda > 2:
            print("Oh, try entering a number in the range again")
            continue

        if board[mikom_shora][mikom_hamoda] == "_":
            board[mikom_shora][mikom_hamoda] = x_or_o
            break
        else:
            print("Great, you're in range, you can continue the game")



def check_win(game, x_or_o: str):
    board = game['board']

    # Check rows
    for i in range(1,3+1):
        win = True
        for j in range(1,3+1):
            if board[i][j] != x_or_o:
                win = False
                break
        if win:
            print(x_or_o, 'won !')
            return True

    # Check columns
    for j in range(1,3+1):
        win = True
        for i in range(1,3+1):
            if board[i][j] != x_or_o:
                win = False
                break
        if win:
            print(x_or_o, 'won !')
            return True

    # Check diagonal (top-left to bottom-right)
    win = True
    for i in range(1,3+1):
        if board[i][i] != x_or_o:
            win = False
            break
    if win:
        print(x_or_o, 'won !')
        return True

    # Check diagonal (top-right to bottom-left)
    win = True
    for i in range(1,3+1):
        if board[i][2 - i] != x_or_o:
            win = False
            break
    if win:
        print(x_or_o, 'won !')
        return True

    return False


def check_full(game):
    board = game['board']
    for i in range(1,3+1):
        for j in range(1,3+1):
            if board[i][j] == "_":
                return False
    return True


def play_x_o():
    game = create_game()

    while True:
        draw_board(game)
        input_square(game, 'X')
        game['turn'] += 1

        if check_win(game, 'X'):
            draw_board(game)
            print("X win!")
            break

        if check_full(game):
            draw_board(game)
            print("The board is full")
            break

        draw_board(game)
        input_square(game, 'O')
        game['turn'] += 1

        if check_win(game, 'O'):
            draw_board(game)
            print("O win!")
            break

        if check_full(game):
            draw_board(game)
            print("The board is full")
            break


if __name__ == "__main__":
    play_x_o()


