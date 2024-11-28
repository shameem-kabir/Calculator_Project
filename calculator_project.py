import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root, width=20, borderwidth=5, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons and add them to the grid
row_val, col_val = 1, 0
for button in buttons:
    if button.isdigit() or button in "+-*/":
        action = lambda x=button: button_click(x)
    elif button == 'C':
        action = clear_entry
    elif button == '=':
        action = calculate

    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=action).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()