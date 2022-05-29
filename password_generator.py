from tkinter import *
import random,string
import pyperclip



def generate():
    password=random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    password = password + ''.join(random.choices(list((string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)),k=(pass_len.get() - 4)))
    new_password.set(password)

def copy_password():
    pyperclip.copy(new_password.get())

generator = Tk()
generator.geometry("400x400")
generator.resizable(0,0)
generator.title("PASSWORD GENERATOR")

Label(generator,text="PASSWORD GENERATOR APPLICATION",font="arial 15 bold").pack()
Label(generator,text="ARSHA",font="arial 15 bold").pack(side = BOTTOM)

Label(generator,text="PASSWORD LENGTH",font="arial 10 bold").pack()
pass_len = IntVar()
Spinbox(generator,from_=8, to_=32,textvariable= pass_len,width=15).pack()

Button(generator,text="GENERATE PASSWORD",command=generate).pack(pady=5)
new_password=StringVar()
Entry(generator,textvariable=new_password).pack()

Button(generator,text="COPY TO CLIPBOARD",command=copy_password).pack(pady=5)

generator.mainloop()
