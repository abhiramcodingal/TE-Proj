# Importing librarie(s)
from tkinter import *

root = Tk()
root.title("Interest Calculator App")
root.geometry("400x400")
root.configure(bg="aquamarine")

def si():
    p = float(p_ent.get())
    n = float(n_ent.get())
    r = float(r_ent.get())
    simple_i = str(((p*n*r) / 100) + p)
    show_ent.delete(0, END)
    show_ent.insert(END, f"The Simple interest is {simple_i}")

def ci():
    p = float(p_ent.get())
    n = float(n_ent.get())
    r = float(r_ent.get())
    compound_i = str(p*(1+r/100)**n)
    show_ent.delete(0, END)
    show_ent.insert(END, f"The Compound interest is {compound_i}")

frame = Frame(master=root, bg="yellow green", relief="groove", width=360, height=150)
frame.place(x=20, y=20)

p_lbl = Label(master=frame, text="Principle Amount:", font=("Cooper Black", 10), bg="lemon chiffon")
p_ent = Entry(master=frame, font=("Modern No. 20", 10))
p_lbl.place(x=20, y=10)
p_ent.place(x=200, y=10)

n_lbl = Label(master=frame, text="No. of Years:", font=("Cooper Black", 10), bg="lemon chiffon")
n_ent = Entry(master=frame, font=("Modern No. 20", 10))
n_lbl.place(x=20, y=60)
n_ent.place(x=200, y=60)

r_lbl = Label(master=frame, text="Interest Rate:", font=("Cooper Black", 10), bg="lemon chiffon")
r_ent = Entry(master=frame, font=("Modern No. 20", 10))
r_lbl.place(x=20, y=110)
r_ent.place(x=200, y=110)

si_btn = Button(master=root, text="Simple Interst", font=("Cooper Black", 10), bg="lemon chiffon", command=si)
si_btn.place(x=30, y=200)

ci_btn = Button(master=root, text="Compound Interst", font=("Cooper Black", 10), bg="lemon chiffon", command=ci)
ci_btn.place(x=220, y=200)

show_ent = Entry(master=root, font=("Calibri", 12), bg="gray36", fg="white", width=40)
show_ent.place(x=35, y=260)

root.mainloop()