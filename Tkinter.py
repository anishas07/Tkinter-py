from tkinter import *
window = Tk()
window.title("Sample window")
window.geometry("100x150")

Lb = Label(text="This is a new tab", fg="Blue", bg="white")
Lb.pack()
b = Button(text="Click here", fg="green", bg="white")
b.pack()
e = Entry(fg ="yellow", bg="pink")
e.pack()

f = Frame(master=window, relief=RAISED, borderwidth=5)
f.pack()

Lb2 = Label(master=f,text="Hello")
Lb2.pack()

Tb = Text(master=f, fg="green", bg="pink")
Tb.pack()

window.mainloop()