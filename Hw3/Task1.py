def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_winner(board):
    # Проверка строк
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Проверка столбцов
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Проверка диагоналей
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board) - i - 1] == board[0][len(board) - 1] and board[i][len(board) - i - 1] != ' ' for i in range(len(board))):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(len(board)) for j in range(len(board[0])))


def tic_tac_toe():
    board_size = 3
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input("Введите номер строки (1-3): ")) - 1
        col = int(input("Введите номер столбца (1-3): ")) - 1

        if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Игрок {current_player} выиграл!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Некорректный ход. Попробуйте снова.")

if __name__ == "__main__":
    tic_tac_toe()
