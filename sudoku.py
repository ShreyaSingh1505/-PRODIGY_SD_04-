import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
   
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # Trigger backtracking
    return True  # Board is completely filled and valid

def get_board():
    
    board = []
    for row in range(9):
        row_data = []
        for col in range(9):
            val = cells[row][col].get().strip()
            if val == "":
                row_data.append(0)
            elif val.isdigit() and 1 <= int(val) <= 9:
                row_data.append(int(val))
            else:
                messagebox.showerror("Invalid Input", "Only numbers 1–9 are allowed.")
                return None
        board.append(row_data)
    return board

def fill_board(board):
   
    for row in range(9):
        for col in range(9):
            cells[row][col].delete(0, tk.END)
            cells[row][col].insert(0, str(board[row][col]))

def solve():
   
    board = get_board()
    if board:
        if solve_sudoku(board):
            fill_board(board)
            messagebox.showinfo("Solved", "Puzzle solved successfully!")
        else:
            messagebox.showerror("Unsolvable", " No valid solution exists.")

def clear():
    
    for row in range(9):
        for col in range(9):
            cells[row][col].delete(0, tk.END)

def restrict_input(event, row, col):
    
    val = cells[row][col].get()
    if not val.isdigit() or not (1 <= int(val) <= 9):
        cells[row][col].delete(0, tk.END)


root = tk.Tk()
root.title(" Sudoku Solver")
root.configure(bg="#f7f7f7")

cells = []

# Creating the Sudoku grid
grid_frame = tk.Frame(root, bg="black", padx=2, pady=2)
grid_frame.pack(pady=20)

for row in range(9):
    row_cells = []
    for col in range(9):
        entry = tk.Entry(
            grid_frame,
            width=2,
            font=("Segoe UI", 18),
            justify="center",
            bd=1,
            relief="solid"
        )
        padx = (3 if col % 3 == 0 else 1)
        pady = (3 if row % 3 == 0 else 1)
        entry.grid(row=row, column=col, padx=padx, pady=pady)
        entry.bind("<KeyRelease>", lambda e, r=row, c=col: restrict_input(e, r, c))
        row_cells.append(entry)
    cells.append(row_cells)

# Buttons for actions
button_frame = tk.Frame(root, bg="#f7f7f7")
button_frame.pack(pady=10)

solve_btn = tk.Button(
    button_frame,
    text="Solve",
    width=12,
    bg="#28a745",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=solve
)
solve_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    bg="#dc3545",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=clear
)
clear_btn.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()



