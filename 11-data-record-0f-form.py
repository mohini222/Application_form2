from tkinter import *

root=Tk()
root.geometry("900x600")
root.title(" ")

root.configure(bg="light blue")
topic=Label(text='Application for Dance classess',bg="light blue",font="comicsansms 25 bold",pady=25).grid(row=0,column=2)

name=Label(root,text="Name",bg="light blue",padx=2,pady=12, font="comicsansms 25 ").grid(row=1,column=1)
addres=Label(root,text="Address",bg="light blue",padx=2,pady=12,font="comicsansms 25 ").grid(row=2,column=1)
phone=Label(root,text="Phone",bg="light blue",padx=2,pady=12,font="comicsansms 25 ").grid(row=3,column=1)
father_name=Label(root,text='Father Name',bg="light blue",padx=2,pady=12,font="comicsansms 25 ").grid(row=4,column=1)
mother_name=Label(root,text="Mother Name",bg="light blue",padx=2,pady=12,font="comicsansms 25 ").grid(row=5,column=1)
Age=Label(root,text="Age",bg="light blue",padx=25, pady=12,font="comicsansms 25 ").grid(row=6,column=1)


def A():
    print("Submitted form :")
    print(f"{namevalue.get(), addresvalue.get(), phonevalue.get(), fathervalue.get(), Mothevalue.get(), agevalue.get()}")
    with open("report of form.py","a") as f:
        f.write(f"{namevalue.get(), addresvalue.get(), phonevalue.get(), fathervalue.get(), Mothevalue.get(), agevalue.get()}\n")


namevalue=StringVar()
addresvalue=StringVar()
phonevalue=StringVar()
fathervalue=StringVar()
Mothevalue=StringVar()
agevalue=StringVar()

enter1=Entry(root,textvariable=namevalue).grid(row=1,column=2)
enter2=Entry(root,textvariable=addresvalue).grid(row=2,column=2)
enter3=Entry(root,textvariable=phonevalue).grid(row=3,column=2)
enter4=Entry(root,textvariable=fathervalue).grid(row=4,column=2)
enter5=Entry(root,textvariable=Mothevalue).grid(row=5,column=2)
enter5=Entry(root,textvariable=agevalue).grid(row=6,column=2)

check1=IntVar()
check=Checkbutton(root,text="Charge for per month 300. Do you want to pay?",font="comicsansms 25 ",bg="light blue",variable=check1,pady=12).grid(row=8,column=2)


Button(root,text="Submit",font="Arail 12 bold",pady=12,command=A).grid(row=11,column=2)

root.mainloop()
