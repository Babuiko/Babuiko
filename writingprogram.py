import pywhatkit
from tkinter import *
tk = Tk()

def convert():
    user_entry = txtfld.get()
    pywhatkit.text_to_handwriting(user_entry, rgb=(0, 0, 0))
    
tk.title("Handwriter")
tk.geometry('760x450')

title = Label(tk, text="HANDWRITER", fg='black', font=('Abadi MT Condensed Light', 16, 'bold'))
title.place (x = 10, y = 1)

btn1 = Button(tk, text="Convert", fg='black', bg='white', font=('Abadi MT Condensed Light', 10, 'bold'), command=convert)
btn1.place (x = 350, y = 318)

txtfld = Entry(tk, bd=3)
txtfld.place (x = 125, y = 80, width=500, height=200)

tk.mainloop()