import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ayan Calculator")
        self.geometry("300x400")
        self.configure(bg="orange")
        
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying input and result
        self.entry = tk.Entry(self, font=("Arial", 20), bd=5, relief=tk.FLAT, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Buttons for numbers and operations
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for symbol, row, column in buttons:
            button = tk.Button(self, text=symbol, font=("Arial", 18), bd=2, relief=tk.RAISED, bg="black", fg="orange",
                               command=lambda s=symbol: self.button_click(s))
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

        # Clear button
        clear_button = tk.Button(self, text="Clear", font=("Arial", 14), bd=2, relief=tk.RAISED, bg="black", fg="orange",
                                 command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Equal button
        equal_button = tk.Button(self, text="=", font=("Arial", 18), bd=2, relief=tk.RAISED, bg="black", fg="orange",
                                 command=self.calculate)
        equal_button.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def button_click(self, symbol):
        current = self.entry.get()
        if current == "Error":
            self.entry.delete(0, "end")
            self.entry.insert("end", symbol)
        elif current == "0":
            self.entry.delete(0, "end")
            self.entry.insert("end", symbol)
        else:
            self.entry.insert("end", symbol)

    def clear(self):
        self.entry.delete(0, "end")

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, "end")
            self.entry.insert("end", str(result))
        except:
            self.entry.delete(0, "end")
            self.entry.insert("end", "Error")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
