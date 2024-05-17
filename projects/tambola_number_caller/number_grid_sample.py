import tkinter as tk
import random

class TambolaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tambola Game")
        
        # Variable to store the called numbers
        self.called_numbers = []

        # Create a frame to hold the number buttons
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Generate buttons for numbers 1 to 90
        self.buttons = {}
        for number in range(1, 91):
            row = (number - 1) // 10
            column = (number - 1) % 10
            button = tk.Button(self.frame, text=str(number), command=lambda n=number: self.call_number(n), width=4, height=2)
            button.grid(row=row, column=column)
            self.buttons[number] = button

    def call_number(self, number):
        """Mark the number as called and update the button's appearance."""
        if number not in self.called_numbers:
            self.called_numbers.append(number)
            self.buttons[number].config(bg='red', fg='white')
            print(f"Number {number} called!")  # This will later be replaced by voice output

# Create the main window and pass it to the TambolaApp class
root = tk.Tk()
app = TambolaApp(root)
root.mainloop()
