import tkinter as tk
from tkinter import messagebox


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False


def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def input(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                num = board[row][col]
                board[row][col] = 0
                if not is_valid(board, row, col, num):
                    return False
                board[row][col] = num
    
    return True


def solve():
    board = []
    ct=0
    for i in range(9):
        row = []
        for j in range(9):
            num = vars[i][j].get()
            if num == "":
                row.append(0)
            elif 1<=int(num)<=9:
                row.append(int(num))
            else:
                ct+=1
                row.append(0)
        board.append(row)

    if ct!=0:
        messagebox.showinfo("Invalid Input", "Please enter a valid Sudoku puzzle.")
    else:
        if input(board):
            if solve_sudoku(board):
                for i in range(9):
                    for j in range(9):
                        widgets[i][j].delete(0, tk.END)
                        widgets[i][j].insert(tk.END, str(board[i][j]))
            else:
                messagebox.showinfo("No Solution", "No solution found for the given Sudoku puzzle.")
        else:
            messagebox.showinfo("No Solution", "No solution found for the given Sudoku puzzle.")


def clear():
    for row in range(9):
        for col in range(9):
            widgets[row][col].delete(0, tk.END)


window = tk.Tk()
window.title("Sudoku Solver")

widgets = []
vars = []
for row in range(9):
    row_widgets = []
    row_vars = []
    for col in range(9):
        col_vars = tk.StringVar()
        col_widgets = tk.Entry(window, textvariable=col_vars, width=2, font=("Arial", 24))
        col_widgets.grid(row=row, column=col, padx=1, pady=1)
        row_widgets.append(col_widgets)
        row_vars.append(col_vars)
    widgets.append(row_widgets)
    vars.append(row_vars)

solve_button = tk.Button(window, text="Solve", command=solve)
solve_button.grid(row=9, column=0, columnspan=5, pady=10)
solve_button.configure(bg="light blue")

clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.grid(row=9, column=5, columnspan=3, pady=10)
clear_button.configure(bg="light blue")

for i in range(9):
    for j in range(9):
        if (i // 3 + j // 3) % 2 == 0:
            widgets[i][j].configure(bg="light blue")
        else:
            widgets[i][j].configure(bg="light yellow")

window.mainloop()