# # start



def create_game() -> dict:
    return {
        'board': [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ],
        'turn': 1
    }


def draw_board(game: dict[str, any]):
    board = game['board']
    print(board)
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
        mikom_shora = int(input(f"{x_or_o} choose the mikom shora from 1-3:"))
        mikom_hamoda = int(input(f"{x_or_o} choose the mikom hamoda from 1-3:"))

        if mikom_shora < 1 or mikom_shora > 3 or mikom_hamoda < 1 or mikom_hamoda > 3:
            print("Invalid input. Please choose values between 1 and 3.")
            continue

        if board[mikom_shora - 1][mikom_hamoda - 1] == "-":
            board[mikom_shora - 1][mikom_hamoda - 1] = x_or_o
            break
        else:
            print("Square already taken. Choose another one.")


# בדיקת שורה
def check_win(game, x_or_o: str):
    board = game['board']
    for shora in board:
        win: bool = True
        for in_shora in shora:
            if in_shora != x_or_o:
                win = False
                break
        if win:
            print(x_or_o, 'won')
            return True

    # בדיקת עמודה
    for col in range(3):
        win: bool = True
        for ran in range(3):
            if board[ran][col] != x_or_o:
                win = False
                break
        if win:
            print(x_or_o, 'won')
            return True

    # בדיקת אלכסון ימין
    win: bool = True
    for amoda in range(3):
        if board[amoda][amoda] != x_or_o:
            win = False
            break
    if win:
        print(x_or_o, 'won')
        return True

    # בדיקת אלכסון שמאל
    win = True
    for amoda in range(3):
        if board[amoda][2 - amoda] != x_or_o:
            win = False
            break
    if win:
        print(x_or_o, 'won')
        return True

    return False


# בדיקה עם הלוח מלא
def check_full(game):
    board = game['board']
    for row in board:
        if '-' in row:
            return False
    return True


# הפעלת משחק
def play_x_o():
    game = create_game()

    while True:
        draw_board(game)
        input_square(game, x_or_o='X')
        game['turn'] += 1

        if check_win(game, x_or_o='X') or check_full(game):
            break

        draw_board(game)
        input_square(game, x_or_o='O')
        game['turn'] += 1

        if check_win(game, x_or_o='O') or check_full(game):
            break


if __name__ == "__main__":
    play_x_o()
