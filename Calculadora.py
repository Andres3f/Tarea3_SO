import tkinter as tk
import math

def animate_sum():
    x = 0
    while x <= result:
        input_field.set(str(x))
        root.update()
        x += 1
        root.after(10)

def click_button(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            global result
            result = eval(expression)
            animate_sum()  
            expression = str(result)
        except Exception as e:
            expression = "Error"
    elif text == "C":
        expression = ""
    elif text == "π":
        expression += "math.pi"
    elif text == "e":
        expression += "math.e"
    elif text == "sin":
        expression += "math.sin("
    elif text == "cos":
        expression += "math.cos("
    elif text == "tan":
        expression += "math.tan("
    elif text == "log":
        expression += "math.log10("
    elif text == "ln":
        expression += "math.log("
    elif text == "sqrt":
        expression += "math.sqrt("
    else:
        expression += text
    input_field.set(expression)

expression = ""
result = 0

root = tk.Tk()
root.title("Calculadora Científica")
root.configure(bg="#333333")

input_field = tk.StringVar()

entry = tk.Entry(root, textvariable=input_field, font=("Arial", 18), justify="right", bd=10, relief=tk.FLAT, bg="#444444", fg="#ffffff")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

buttons = [
    "7", "8", "9", "/", "C", "sin",
    "4", "5", "6", "*", "(", "cos",
    "1", "2", "3", "-", ")", "tan",
    "0", ".", "=", "+", "π", "log",
    "e", "sqrt", "ln"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 12), width=4, height=2, bd=0, relief=tk.FLAT, bg="#666666", fg="#ffffff")
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click_button)
    col += 1
    if col > 5:
        col = 0
        row += 1

for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i + 1, weight=1)

root.mainloop()
