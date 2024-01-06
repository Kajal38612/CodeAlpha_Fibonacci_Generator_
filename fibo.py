from tkinter import *
kjl_root=Tk()

kjl_root.geometry("730x430")
kjl_root.minsize(730,430)
kjl_root.maxsize(730,430)

def fibo():
    a=int(e_var.get())

    scrollbar=Scrollbar(kjl_root)
    scrollbar.pack(side=RIGHT,fill=BOTH)
    lbx=Listbox(kjl_root,yscrollcommand=scrollbar.set)
    scrollbar.config(command=lbx.yview)
    
    lbx.place(x=250,y=210) 

    n1, n2 = 0, 1
    count = 0

    if a <= 0:
        lbx.insert("Please enter a positive integer")
    # if there is only one term, return n1
    elif a == 1:
        lbx.insert(END,n1)
    
    # generate fibonacci sequence
    else:
    
        while count < a:
            lbx.insert(END,n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


kjl_root.title("kajal\'s GUI")
kjl_lable=Label(text="FIBONACCI GENERATOR").place(x=260,y=100)

Label(kjl_root,text="Enter the term to print fibonacci series:").place(x=230,y=130)

e_var = IntVar()
eenter= Entry(kjl_root, textvariable=e_var).place(x=250,y=160)

btn=Button(kjl_root,text='Print',command=fibo).place(x=290,y=190)

kjl_root.mainloop()


