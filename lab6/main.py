import tkinter as tk
import lib

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    result = lib.uravnenie(a, b, c)
    result_label.config(text=result)


root = tk.Tk()
root.title("lab6")
root.geometry("270x160")
root.resizable(False, False)

label_a = tk.Label(root, text="Коэффициент a:")
label_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b = tk.Label(root, text="Коэффициент b:")
label_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

label_c = tk.Label(root, text="Коэффициент c:")
label_c.grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
