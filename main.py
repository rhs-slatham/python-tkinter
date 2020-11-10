# Tkinter spelled as "tkinter" or "Tkinter" depending on Python version.
from tkinter import *

root = Tk()

root.title("My GUI title")
root.geometry("500x200")

app = Frame(root)
app.grid()

button1 = Button(app, text = "Button1")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "Button2")

button3 = Button(app)
button3.grid()
button3["text"] = "Button3"
