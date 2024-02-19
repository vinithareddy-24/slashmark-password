from tkinter import *
import random
root = Tk()
root.title("Strong password generator")
root.geometry("500x250")

def new_rand():
    pw_entry.delete(0,END)
    my_password=''
    pw_len = int(entry_window.get())
    for i in range(pw_len):
        my_password += chr(random.randint(33,126))
    pw_entry.insert(0, my_password)


lf = LabelFrame(root, text="How many characters?")
lf.pack()

entry_window = Entry(lf, font=("Helvetica",24), width = 10)
entry_window.pack(padx=15, pady=15)

pw_entry = Entry(root, text='', font=("Helvetica",20), border=5, width=25)
pw_entry.pack(padx=20, pady=20)

gsp_btn = Button(root, text = "Generate Strong Password", font = ("Helvetica",10), bg = "lightblue", command=new_rand)
gsp_btn.pack(pady=10)

root.mainloop()
