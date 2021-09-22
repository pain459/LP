# gui programming.

import easygui as gui
import greeting as greeting

gui.msgbox("hello EasyGUI", "This is a message box", "Hi there!")

choices = ("Red", "Yellow", "Blue")
gui.buttonbox("What is your fav color?", "Choose wisely", choices)
# There are different types of boxes. Explore them soon.

# File and directory selection dialogs
gui.fileopenbox("Select a file", "fileopenbox demo", default="*.txt")

# Working with Tkinter
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

window.mainloop()