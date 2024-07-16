import random
from tkinter import ttk
from tkinter import *
import customtkinter as ctk
from time import strftime
from fpdf import FPDF
import messagebox
import time
import pymysql
from PIL import ImageTk,Image
root=Tk()

root.geometry("1500x800")
root.configure(bg="coral")

def Calculator():
    calci.Calculator

def create_account2():
    f3.destroy()

    def sub():
        fem.destroy()
        adminlogin()
    name=StringVar()
    password=StringVar()
    cpassword=StringVar()

    def connect_database():
        fem.destroy()
        adminlogin()
        if name.get() == '' or password.get() == "" or cpassword.get() == "":
            messagebox.showerror("error", "all fielss are required")
        elif password.get() != cpassword.get():
            messagebox.showwarning("wrong", "check password correctly")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                cur = con.cursor()
            except:
                messagebox.showerror("error", "database connectivicty problem")
                return
            cur.execute("insert into userdata values(%s,%s)", (
                name.get(),
                password.get(),
            ))
            con.commit()

    fem=Frame(root,width=1500,height=800)
    fd=ctk.CTkFrame(fem,corner_radius=40,width=500,height=700,fg_color="white",bg_color="coral")
    Label(fem,text="Create Account",font="c 30 bold",bg="white").place(x=590,y=100)
    Label(fem,text="username",font=("roman 20 bold"),bg="white").place(x=550,y=200)


    Label(fem, text="password", font=("roman 20 bold"),bg="white").place(x=550, y=300)

    Label(fem, text="_____________________________", font=("roman 20 bold"), bg="white").place(x=560, y=260)
    Label(fem, text="conform password", font=("roman 20 bold"), bg="white").place(x=550, y=400)
    Label(fem, text="_____________________________", font=("roman 20 bold"), bg="white").place(x=560, y=480)

    Entry(fem,font=("roman 20 bold"),textvariable=name,bg="white",width=30,border=0).place(x=600,y=240)
    Entry(fem,font=("roman 20 bold"),textvariable=password,bg="white",width=30,border=0).place(x=600,y=340)
    Entry(fem,font=("roman 20 bold"),textvariable=cpassword,bg="white",width=30,border=0).place(x=600,y=440)


    Label(fem, text="_____________________________", font=("roman 20 bold"),bg="white").place(x=560, y=370)
    fd.place(x=500,y=50)
    fem.configure(bg="coral")
    fem.pack()
    #___addimg image_________________________________________________________________
    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(50, 40))
    label=ctk.CTkLabel(fem,image=img,compound=None,bg_color="white",fg_color="white")
    label.place(x=540,y=240)

    img2 = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\666666.jpg"),
        size=(50, 50))

    imgc = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\OIP (7).jpg"),
        size=(50, 50))
    label = ctk.CTkLabel(fem, image=imgc, compound=None, bg_color="white", fg_color="white")
    label.place(x=540, y=440)
    label=ctk.CTkLabel(fem,image=img2,compound=None,bg_color="white",fg_color="white")
    label.place(x=540,y=340)

    #=============adding  button

    button2=ctk.CTkButton(fem,text="proceed",text_color="white",fg_color="orangered",width=400,height=40,corner_radius=100,bg_color="white",hover_color="coral",font=("times",20,"bold"),command=connect_database)
    button2.place(x=550,y=600)
    button2=ctk.CTkButton(fem,text="back",text_color="red",fg_color="white",width=400,height=40,corner_radius=100,bg_color="white",hover_color="white",font=("times",20,"bold"),command=sub)
    button2.place(x=550,y=660)
def create_account1():
    f2.destroy()
    def connect_database():
        fem.destroy()
        login()
        if name.get() == '' or password.get() == "" or cpassword.get() == "":
            messagebox.showerror("error", "all fielss are required")
        elif password.get()!=cpassword.get():
            messagebox.showwarning("wrong","check password correctly")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                cur = con.cursor()
            except:
                messagebox.showerror("error","database connectivicty problem")
                return
            cur.execute("insert into userdata values(%s,%s)", (
                name.get(),
                password.get(),
            ))
            con.commit()

    def sub():
        fem.destroy()
        login()
    global username
    global conform
    name=StringVar()
    username=StringVar()
    conform=StringVar()
    password=StringVar()
    cpassword=StringVar()

    fem=Frame(root,width=1500,height=800)
    fd=ctk.CTkFrame(fem,corner_radius=40,width=500,height=700,fg_color="white",bg_color="coral")
    Label(fem,text="Create Account",font="c 30 bold",bg="white").place(x=590,y=100)
    Label(fem,text="username",font=("roman 20 bold"),bg="white").place(x=550,y=200)


    Label(fem, text="password", font=("roman 20 bold"),bg="white").place(x=550, y=300)

    Label(fem, text="_____________________________", font=("roman 20 bold"), bg="white").place(x=560, y=260)
    Label(fem, text="conform password", font=("roman 20 bold"), bg="white").place(x=550, y=400)
    Label(fem, text="_____________________________", font=("roman 20 bold"), bg="white").place(x=560, y=480)

    Entry(fem,font=("roman 20 bold"),textvariable=name,bg="white",width=30,border=0).place(x=600,y=240)
    Entry(fem,font=("roman 20 bold"),textvariable=password,bg="white",width=30,border=0).place(x=600,y=340)
    Entry(fem,font=("roman 20 bold"),textvariable=cpassword,bg="white",width=30,border=0).place(x=600,y=440)


    Label(fem, text="_____________________________", font=("roman 20 bold"),bg="white").place(x=560, y=370)
    fd.place(x=500,y=50)
    fem.configure(bg="coral")
    fem.pack()
    #___addimg image_________________________________________________________________
    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(50, 40))
    label=ctk.CTkLabel(fem,image=img,compound=None,bg_color="white",fg_color="white")
    label.place(x=540,y=240)

    img2 = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\666666.jpg"),
        size=(50, 50))

    imgc = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\OIP (7).jpg"),
        size=(50, 50))
    label = ctk.CTkLabel(fem, image=imgc, compound=None, bg_color="white", fg_color="white")
    label.place(x=540, y=440)
    label=ctk.CTkLabel(fem,image=img2,compound=None,bg_color="white",fg_color="white")
    label.place(x=540,y=340)

    #=============adding  button

    button2=ctk.CTkButton(fem,text="proceed",text_color="white",fg_color="orangered",width=400,height=40,corner_radius=100,bg_color="white",hover_color="coral",font=("times",20,"bold"),command=connect_database)
    button2.place(x=550,y=600)
    button2=ctk.CTkButton(fem,text="back",text_color="red",fg_color="white",width=400,height=40,corner_radius=100,bg_color="white",hover_color="white",font=("times",20,"bold"),command=sub)
    button2.place(x=550,y=660)
def Quantityystem():
    def sub():
        f2.destroy()
        fr.destroy()
        billmaker()
    def send():
        messagebox.askyesno("Do you want to creat pdf for sharing purpose", "your PDF created successfully")
        if YES:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', size=15)
            pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png",x=45,y=0)
            pdf.set_text_color(0, 0, 0)
            f = open(f"E:\\PROGRAMMS\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
            for x in f:
                pdf.cell(200, 7, txt=x, ln=100, align="C")
            pdf.output(f"E:\\PROGRAMMS\\ {bill_number.get()}.pdf")

    def pending():
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png",x=45,y=0)
        pdf.set_text_color(0, 0, 0)
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pending_bills\\ {bill_number.get()}.pdf")


    def paid():
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png", x=45, y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pade1.png",x=150,y=240)
        pdf.set_text_color(0, 0, 0)
        pdf.text(x=75, y=290, txt="!Thankyou Visit Again!")
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pade_bills\\ {bill_number.get()}.pdf")

    def generate_number():
        global number
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
        number = ""
        for i in range(10):
            number = number + random.choice(list)
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number = ""
        for i in range(8):
            number = number + random.choice(list)
            bill_number.set(number)

    imgemp = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(30, 30))

    def frame():
        global total
        global amount
        global costomer_name
        global contact_no
        global bill_number
        global weight
        global westage
        global tonch
        global category
        global makingcharge
        global fr

        total = IntVar()
        amount = StringVar()
        category = StringVar()
        weight = StringVar()
        westage = StringVar()
        makingcharge = StringVar()
        f2 = Frame(root, width=1600, height=800)
        fr = ctk.CTkFrame(root, corner_radius=40, width=1450, height=750, fg_color="white", bg_color="coral")
        fr.place(x=20, y=20)
        f2.configure(bg="coral")
        f2.pack(fill=BOTH)
        Label(fr, text="Quantity Billing System", font="comicsm 40 bold", bg="white").place(x=400, y=20)
        lf = LabelFrame(fr, border=4, text="Costomor Detail", width=1250, height=80, relief=GROOVE, bg="white")
        lf.place(x=100, y=100)

        # ================================product frame

        pf = LabelFrame(fr, text="Ornaments", border=4, width=500, height=450, relief=GROOVE, bg="white")
        pf.place(x=100, y=187)
        Label(pf, text="Select Category", font=("comicsm 15 bold"), bg="white").place(x=10, y=2)
        category = ttk.Combobox(pf, value=("     Nose pins", "             Rawa", "               Daai", "      Gunghru", "         Casting", "single-stone","  Multi-Stone","  color-stone"), font="c 15 bold",
                                width=40, state='readonly')
        category.place(x=10, y=30)

        def calculate():
            total = f"{(int(weight.get())  *  + int(westage.get()))}"
            amount.set(total)

        def calculator():
            from calci import Calculator
            calc = Calculator()
            calc.run()

        def clearbill():
            textarea.destroy()
            s.destroy()
            text()

        def additem():
            weight.set("")
            tonch.set("")
            westage.set("")
            amount.set("")
            category.set(value="Select New Item")

        Label(pf, text="Enter Number of Pice's", font=("comicsm 15 bold"), bg="white").place(x=10, y=60)
        Entry(pf, textvariable=weight, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=90)
        Label(pf, text="Enter par pice Rate", font=("comicsm 15 bold"), bg="white").place(x=10, y=120)
        Entry(pf, textvariable=westage, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=150)

        costom_ammount = StringVar()
        Label(pf, text="Rate:", font=("comicsm 15 bold"), bg="white").place(x=10, y=364)
        Label(pf, textvariable=amount, font=("comicsm 15 bold"), bg="white", border=5).place(x=140, y=363)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Calculate",
                      font=("roman", 20, "bold"), command=calculate).place(x=210, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Calculator", font=("roman", 20, "bold"), command=calculator).place(x=310, y=390)

        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="PDF", font=("roman", 20, "bold"), command=send).place(x=420, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Clear Bill", font=("roman", 20, "bold"), command=clearbill).place(x=110, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Add item",
                      font=("roman", 20, "bold"), command=additem).place(x=10, y=390)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        bf = LabelFrame(fr, text="Bill Frame", border=4, width=730, height=530, relief=GROOVE, bg="white")
        bf.place(x=620, y=185)

        # ----------------------------------------------------------------------------------------------------textarea
        def text():
            global text
            global textarea
            global s
            s = Scrollbar(bf)
            s.pack(side=RIGHT, fill=Y)
            textarea = Text(bf, width=64, height=23.5, font=("Airal 14 bold"), yscrollcommand=s.set)
            s.config(command=textarea.yview)
            textarea.pack()

        text()

        def my_time():
            global t
            t = StringVar()
            timestr = strftime("  %x")
            lf.config(text=timestr, font=("times", 10, "bold"))
            t.set(timestr)

        my_time()

        def show():
            if category.get() != 0:
                textarea.insert(END,
                                f"{    (category.get())}                   {(weight.get())}                                          {(westage.get())}                            {amount.get()}\n\n")

        def creatbill():
            textarea.insert(END, "\t\t       GAYATRI JEWELLERS\n")
            textarea.insert(END, "\t\t  Shree Sidhi Bilding shop no:5\n")
            textarea.insert(END, "\t\t         SarafBazar Nashik\n")
            textarea.insert(END, "\t\tph-no:8308090190 / 9552720348\n")
            textarea.insert(END,
                            f"\n\n\nCostomer Name:{(costomer_name.get())} \t\t\t\t           Contact Number:{(contact_no.get())}")
            textarea.insert(END,
                            f"\n\nBill Number:{(bill_number.get())}\t                                                     Date:{t.get()}")
            textarea.insert(END,
                            f"\n________________________________________________________________\nOrnament\t                 Number of pices                   Par pice rate            Amount")
            textarea.insert(END,
                            "\n---------------------------------------------------------------------------------------------------------------------\n")

        def clear():
            weight.set("")
            tonch.set("")
            westage.set("")
            costom_ammount.set("")
            bill_number.set("")
            costomer_name.set("")
            contact_no.set("")
            category.set("")

        pl = LabelFrame(fr, text="Bill Option", border=4, width=500, height=80, relief=GROOVE, bg="white")
        ctk.CTkButton(pl, text="add", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=show).place(x=100, y=9)
        ctk.CTkButton(pl, text="pending", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=pending).place(x=370, y=9)
        ctk.CTkButton(pl, text="creat", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=creatbill).place(x=10, y=9)
        ctk.CTkButton(pl, text="pade", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=paid).place(x=280, y=9)
        ctk.CTkButton(pl, text="clear", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=clear).place(x=185, y=9)
        pl.place(x=100, y=650)
        bill_number = StringVar()
        costomer_name = StringVar()
        contact_no = StringVar()

        # =============================================set entry
        Entry(lf, textvariable=bill_number, font=(" c 13 bold"), border=0).place(x=120, y=13)
        Entry(lf, textvariable=costomer_name, font=(" c 13 bold"), border=0).place(x=630, y=13)
        Entry(lf, textvariable=contact_no, font=(" c 13 bold"), border=0).place(x=1015, y=13)

        Label(lf, text="Bill Number", font=("Airal 10 bold"), bg="white").place(x=20, y=15)
        Label(lf, text="________________________", borderwidth=0, font=("Airal 10 bold"), bg="white").place(x=110, y=33)
        ctk.CTkButton(lf, text="Generate Number", text_color="white", fg_color="red", corner_radius=20,
                      command=generate_number, font=("Airal", 20, "bold")).place(x=280, y=20)
        Label(lf, text="Costomer Name", font=("Airal 10 bold"), bg="white").place(x=500, y=15)
        Label(lf, text="__________________________________", font=("Airal 10 bold"), bg="white").place(x=610, y=33)
        Label(lf, text="Contact Number", font=("Airal 10 bold"), bg="white").place(x=900, y=15)
        Label(lf, text="________________________", font=("Airal 10 bold"), bg="white").place(x=1010, y=33)

        ctk.CTkButton(fr, text="Back", fg_color="red", text_color="white", corner_radius=20,
                      font=("Airal", 20, "bold"),command=sub).place(x=20, y=50)
        ctk.CTkLabel(fr, image=imgemp, text="Employ", compound=LEFT).place(x=30, y=10)

    frame()

    def time():
        timestr = strftime("%H:%M:%S %p  %A")
        lf.config(text=timestr)
        lf.after(1000, time)

    lf = Label(fr, font=("times", 20, "bold"), bg="white")
    lf.place(x=1130, y=40)
    time()
def Mettalsystem():
    def sub():
        f2.destroy()
        fr.destroy()
        billmaker()
    def send():
        messagebox.askyesno("Do you want to creat pdf for sharing purpose", "your PDF created successfully")
        if YES:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', size=15)
            pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png",x=45,y=0)
            pdf.set_text_color(0, 0, 0)
            f = open(f"E:\\PROGRAMMS\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
            for x in f:
                pdf.cell(200, 7, txt=x, ln=100, align="C")
            pdf.output(f"E:\\PROGRAMMS\\ {bill_number.get()}.pdf")

    def pending():
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png",x=45,y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pendinglogoo.jpg", x=120, y=220)
        pdf.set_text_color(0, 0, 0)
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pending_bills\\ {bill_number.get()}.pdf")


    def paid():
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png", x=45, y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pade1.png",x=150,y=240)
        pdf.set_text_color(0, 0, 0)
        pdf.text(x=75, y=290, txt="!Thankyou Visit Again!")
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pade_bills\\ {bill_number.get()}.pdf")

    def generate_number():
        global number
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
        number = ""
        for i in range(10):
            number = number + random.choice(list)
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number = ""
        for i in range(8):
            number = number + random.choice(list)
            bill_number.set(number)

    imgemp = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(30, 30))

    def frame():
        global total
        global amount
        global costomer_name
        global contact_no
        global bill_number
        global weight
        global westage
        global tonch
        global category
        global makingcharge
        global fr

        total = IntVar()
        amount = StringVar()
        category = StringVar()
        tonch = StringVar()
        weight = StringVar()
        westage = StringVar()
        makingcharge = StringVar()
        f2 = Frame(root, width=1600, height=800)
        fr = ctk.CTkFrame(root, corner_radius=40, width=1450, height=750, fg_color="white", bg_color="coral")
        fr.place(x=20, y=20)
        f2.configure(bg="coral")
        f2.pack(fill=BOTH)
        Label(fr, text="Metal Billing System", font="comicsm 40 bold", bg="white").place(x=400, y=20)
        lf = LabelFrame(fr, border=4, text="Costomor Detail", width=1250, height=80, relief=GROOVE, bg="white")
        lf.place(x=100, y=100)

        # ================================product frame

        pf = LabelFrame(fr, text="Ornaments", border=4, width=500, height=450, relief=GROOVE, bg="white")
        pf.place(x=100, y=187)
        Label(pf, text="Select Category", font=("comicsm 15 bold"), bg="white").place(x=10, y=2)
        category = ttk.Combobox(pf, value=("Nose pins", "          Nath", "           Bali", "         Tops", "       Ring's", "       Bugdi"), font="c 15 bold",
                                width=40, state='readonly')
        category.place(x=10, y=30)

        def calculate():
            total = f"{(float(weight.get()) ) * (int(tonch.get()) + int(westage.get()))}"
            amount.set(total)

        def calculator():
            from calci import Calculator
            calc = Calculator()
            calc.run()

        def clearbill():
            textarea.destroy()
            s.destroy()
            text()

        def additem():
            weight.set("")
            tonch.set("")
            westage.set("")
            amount.set("")
            category.set(value="Select New Item")

        Label(pf, text="Enter Weight", font=("comicsm 15 bold"), bg="white").place(x=10, y=60)
        Entry(pf, textvariable=weight, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=90)
        Label(pf, text="Enter Westage", font=("comicsm 15 bold"), bg="white").place(x=10, y=120)
        Entry(pf, textvariable=westage, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=150)
        Label(pf, text="Enter Tonch", font=("comicsm 15 bold"), bg="white").place(x=10, y=180)
        Entry(pf, textvariable=tonch, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=210)

        costom_ammount = StringVar()
        Label(pf, text="Fine :", font=("comicsm 15 bold"), bg="white").place(x=10, y=364)
        Label(pf, textvariable=amount, font=("comicsm 15 bold"), bg="white", border=5).place(x=140, y=363)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Calculate",
                      font=("roman", 20, "bold"), command=calculate).place(x=210, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Calculator", font=("roman", 20, "bold"), command=calculator).place(x=310, y=390)

        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="PDF", font=("roman", 20, "bold"), command=send).place(x=420, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Clear Bill", font=("roman", 20, "bold"), command=clearbill).place(x=110, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Add item",
                      font=("roman", 20, "bold"), command=additem).place(x=10, y=390)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        bf = LabelFrame(fr, text="Bill Frame", border=4, width=730, height=530, relief=GROOVE, bg="white")
        bf.place(x=620, y=185)

        # ----------------------------------------------------------------------------------------------------textarea
        def text():
            global text
            global textarea
            global s
            s = Scrollbar(bf)
            s.pack(side=RIGHT, fill=Y)
            textarea = Text(bf, width=64, height=23.5, font=("Airal 14 bold"), yscrollcommand=s.set)
            s.config(command=textarea.yview)
            textarea.pack()

        text()

        def my_time():
            global t
            t = StringVar()
            timestr = strftime("  %x")
            lf.config(text=timestr, font=("times", 10, "bold"))
            t.set(timestr)

        my_time()

        def show():
            if category.get() != 0:
                textarea.insert(END,
                                f"{    (category.get())}                   {(weight.get())}                      {(tonch.get())}                    {(westage.get())}                      {amount.get()}\n\n")

        def creatbill():
            textarea.insert(END, "\t\t       GAYATRI JEWELLERS\n")
            textarea.insert(END, "\t\t  Shree Sidhi Bilding shop no:5\n")
            textarea.insert(END, "\t\t         SarafBazar Nashik\n")
            textarea.insert(END, "\t\tph-no:8308090190 / 9552720348\n")
            textarea.insert(END,
                            f"\n\n\nCostomer Name:{(costomer_name.get())} \t\t\t\t           Contact Number:{(contact_no.get())}")
            textarea.insert(END,
                            f"\n\nBill Number:{(bill_number.get())}\t                                                     Date:{t.get()}")
            textarea.insert(END,
                            f"\n________________________________________________________________\nOrnament\t               Weight               Tonch               Westage               Fine")
            textarea.insert(END,
                            "\n---------------------------------------------------------------------------------------------------------------------\n")

        def clear():
            weight.set("")
            tonch.set("")
            westage.set("")
            costom_ammount.set("")
            bill_number.set("")
            costomer_name.set("")
            contact_no.set("")
            category.set("")

        pl = LabelFrame(fr, text="Bill Option", border=4, width=500, height=80, relief=GROOVE, bg="white")
        ctk.CTkButton(pl, text="add", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=show).place(x=100, y=9)
        ctk.CTkButton(pl, text="pending", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=pending).place(x=370, y=9)
        ctk.CTkButton(pl, text="creat", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=creatbill).place(x=10, y=9)
        ctk.CTkButton(pl, text="pade", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=paid).place(x=280, y=9)
        ctk.CTkButton(pl, text="clear", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=clear).place(x=185, y=9)
        pl.place(x=100, y=650)
        bill_number = StringVar()
        costomer_name = StringVar()
        contact_no = StringVar()

        # =============================================set entry
        Entry(lf, textvariable=bill_number, font=(" c 13 bold"), border=0).place(x=120, y=13)
        Entry(lf, textvariable=costomer_name, font=(" c 13 bold"), border=0).place(x=630, y=13)
        Entry(lf, textvariable=contact_no, font=(" c 13 bold"), border=0).place(x=1015, y=13)

        Label(lf, text="Bill Number", font=("Airal 10 bold"), bg="white").place(x=20, y=15)
        Label(lf, text="________________________", borderwidth=0, font=("Airal 10 bold"), bg="white").place(x=110, y=33)
        ctk.CTkButton(lf, text="Generate Number", text_color="white", fg_color="red", corner_radius=20,
                      command=generate_number, font=("Airal", 20, "bold")).place(x=280, y=20)
        Label(lf, text="Costomer Name", font=("Airal 10 bold"), bg="white").place(x=500, y=15)
        Label(lf, text="__________________________________", font=("Airal 10 bold"), bg="white").place(x=610, y=33)
        Label(lf, text="Contact Number", font=("Airal 10 bold"), bg="white").place(x=900, y=15)
        Label(lf, text="________________________", font=("Airal 10 bold"), bg="white").place(x=1010, y=33)

        ctk.CTkButton(fr, text="Back", fg_color="red", text_color="white", corner_radius=20,
                      font=("Airal", 20, "bold"), command=sub).place(x=20, y=50)
        ctk.CTkLabel(fr, image=imgemp, text="Employ", compound=LEFT).place(x=30, y=10)

    frame()

    def time():
        timestr = strftime("%H:%M:%S %p  %A")
        lf.config(text=timestr)
        lf.after(1000, time)

    lf = Label(fr, font=("times", 20, "bold"), bg="white")
    lf.place(x=1130, y=40)
    time()
def retail():
    def sub():
        f2.destroy()
        fr.destroy()
        billmaker()
    def send():
        messagebox.askyesno("Do you want to creat pdf for sharing purpose", "your PDF created successfully")
        if YES:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', size=15)
            pdf.set_text_color(0, 0, 0)
            pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png", x=45, y=0)
            f = open(f"E:\\PROGRAMMS\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
            for x in f:
                pdf.cell(200, 7, txt=x, ln=100, align="C")
            pdf.output(f"E:\\PROGRAMMS\\{bill_number.get()}.pdf")

    def pending():
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png",x=45,y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pendinglogoo.jpg", x=120, y=220)
        pdf.set_text_color(0, 0, 0)
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pending_bills\\ {bill_number.get()}.pdf")


    def paid():
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png", x=45, y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pade1.png",x=150,y=240)
        pdf.set_text_color(0, 0, 0)
        pdf.text(x=75, y=290, txt="!Thankyou Visit Again!")
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pade_bills\\ {bill_number.get()}.pdf")

    def generate_number():
        global number
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
        number = ""
        for i in range(10):
            number = number + random.choice(list)
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number = ""
        for i in range(8):
            number = number + random.choice(list)
            bill_number.set(number)
        print(number)

    imgemp = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(30, 30))

    def frame():
        global making_charge
        global amount
        global costomer_name
        global contact_no
        global bill_number
        global weight
        global goldrate
        global category
        global fr
        amount = StringVar()
        category = StringVar()
        goldrate = StringVar()
        making_charge = StringVar()
        weight = StringVar()
        f2 = Frame(root, width=1600, height=800)
        fr = ctk.CTkFrame(root, corner_radius=40, width=1450, height=750, fg_color="white", bg_color="coral")
        fr.place(x=20, y=20)
        f2.configure(bg="coral")
        f2.pack(fill=BOTH)
        Label(fr, text="Retail Billing System", font="comicsm 40 bold", bg="white").place(x=400, y=20)
        lf = LabelFrame(fr, border=4, text="Costomor Detail", width=1250, height=80, relief=GROOVE, bg="white")
        lf.place(x=100, y=100)

        # ================================product frame

        pf = LabelFrame(fr, text="Ornaments", border=4, width=500, height=450, relief=GROOVE, bg="white")
        pf.place(x=100, y=187)
        Label(pf, text="Select Category", font=("comicsm 15 bold"), bg="white").place(x=10, y=2)
        category = ttk.Combobox(pf, value=("Nose pins", "          Nath", "           Bali", "         Tops", "       Ring's", "       Bugdi"), font="c 15 bold",
                                width=40, state='readonly')
        category.place(x=10, y=30)

        def calculate():
            price = f"{float(weight.get()) * int(goldrate.get()) }"
            h=price[:-3]
            v=int(h)+ int(making_charge.get())
            amount.set(v)

        def calculator():
            from calci import Calculator
            calc = Calculator()
            calc.run()

        def clearbill():
            textarea.destroy()
            s.destroy()
            text()

        def additem():
            weight.set("")
            amount.set("")
            category.set(value="Select New Item")

        Label(pf, text="Enter Weight", font=("comicsm 15 bold"), bg="white").place(x=10, y=60)
        Entry(pf, textvariable=weight, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=90)
        Label(pf, text="Enter Gold Rate", font=("comicsm 15 bold"), bg="white").place(x=10, y=120)
        Entry(pf, textvariable=goldrate, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=150)

        Label(pf, text="Enter Making Charge", font=("comicsm 15 bold"), bg="white").place(x=10, y=180)
        Entry(pf, textvariable=making_charge, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=210)
        ctk.CTkButton(pf, text="Generate PDF ", font=("Arial", 15, "bold"), fg_color="coral", text_color="white",
                      width=450,
                      corner_radius=20, command=send).place(x=20, y=310)

        Label(pf, text="Ammount :", font=("comicsm 15 bold"), bg="white").place(x=10, y=350)
        Label(pf, textvariable=amount, font=("comicsm 15 bold"), bg="white", border=5).place(x=140, y=345)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Calculate",
                      font=("roman", 20, "bold"), command=calculate).place(x=250, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Calculator", font=("roman", 20, "bold"), command=calculator).place(x=370, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Clear Bill", font=("roman", 20, "bold"), command=clearbill).place(x=140, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Add item",
                      font=("roman", 20, "bold"), command=additem).place(x=30, y=390)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        bf = LabelFrame(fr, text="Bill Frame", border=4, width=730, height=530, relief=GROOVE, bg="white")
        bf.place(x=620, y=185)

        # ----------------------------------------------------------------------------------------------------textarea
        def text():
            global text
            global textarea
            global s
            s = Scrollbar(bf)
            s.pack(side=RIGHT, fill=Y)
            textarea = Text(bf, width=64, height=23.5, font=("Airal 14 bold"), yscrollcommand=s.set)
            s.config(command=textarea.yview)
            textarea.pack()

        text()

        def my_time():
            global t
            t = StringVar()
            timestr = strftime("  %x")
            lf.config(text=timestr, font=("times", 10, "bold"))
            t.set(timestr)

        my_time()

        def show():
            if category.get() != 0:
                textarea.insert(END,
                                f"{(category.get())}                 {(weight.get())}                       {making_charge.get()}                            {goldrate.get()}              {amount.get()}\n\n")

        def creatbill():
            textarea.insert(END, "\t\t       GAYATRI JEWELLERS\n")
            textarea.insert(END, "\t\t  Shree Sidhi Bilding shop no:5\n")
            textarea.insert(END, "\t\t         SarafBazar Nashik\n")
            textarea.insert(END, "\t\tph-no:8308090190 / 9552720348\n")
            textarea.insert(END,
                            f"\n\n\nCostomer Name:{(costomer_name.get())} \t\t\t\t           Contact Number:{(contact_no.get())}")
            textarea.insert(END,
                            f"\n\nBill Number:{(bill_number.get())}\t                                                     Date:{t.get()}")

            textarea.insert(END,
                            f"\n________________________________________________________________\nOrnament\t             Weight             making-charge             Goldrate             Price")
            textarea.insert(END,
                            "\n---------------------------------------------------------------------------------------------------------------------\n")

        def clear():
            goldrate.set("")
            weight.set("")
            bill_number.set("")
            costomer_name.set("")
            contact_no.set("")
            category.set("")

        pl = LabelFrame(fr, text="Bill Option", border=4, width=500, height=80, relief=GROOVE, bg="white")
        ctk.CTkButton(pl, text="add", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=show).place(x=100, y=9)
        ctk.CTkButton(pl, text="paid", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=paid).place(x=280, y=9)
        ctk.CTkButton(pl, text="creat", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=creatbill).place(x=10, y=9)
        ctk.CTkButton(pl, text="pending", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=pending).place(x=370, y=9)
        ctk.CTkButton(pl, text="clear", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=clear).place(x=185, y=9)
        pl.place(x=100, y=650)
        bill_number = StringVar()
        costomer_name = StringVar()
        contact_no = StringVar()

        # =============================================set entry
        Entry(lf, textvariable=bill_number, font=(" c 13 bold"), border=0).place(x=120, y=13)
        Entry(lf, textvariable=costomer_name, font=(" c 13 bold"), border=0).place(x=630, y=13)
        Entry(lf, textvariable=contact_no, font=(" c 13 bold"), border=0).place(x=1015, y=13)

        Label(lf, text="Bill Number", font=("Airal 10 bold"), bg="white").place(x=20, y=15)
        Label(lf, text="________________________", borderwidth=0, font=("Airal 10 bold"), bg="white").place(x=110, y=33)
        ctk.CTkButton(lf, text="Generate Number", text_color="white", fg_color="red", corner_radius=20,
                      command=generate_number, font=("Airal", 20, "bold")).place(x=280, y=20)
        Label(lf, text="Costomer Name", font=("Airal 10 bold"), bg="white").place(x=500, y=15)
        Label(lf, text="__________________________________", font=("Airal 10 bold"), bg="white").place(x=610, y=33)
        Label(lf, text="Contact Number", font=("Airal 10 bold"), bg="white").place(x=900, y=15)
        Label(lf, text="________________________", font=("Airal 10 bold"), bg="white").place(x=1010, y=33)

        ctk.CTkButton(fr, text="Back", fg_color="red", text_color="white", corner_radius=20,
                      font=("Airal", 20, "bold"),command=sub).place(x=20, y=50)
        ctk.CTkLabel(fr, image=imgemp, text="Employ", compound=LEFT).place(x=30, y=10)

    frame()

    def time():
        timestr = strftime("%H:%M:%S %p  %A")
        lf.config(text=timestr)
        lf.after(1000, time)

    lf = Label(fr, font=("times", 20, "bold"), bg="white")
    lf.place(x=1130, y=40)
    time()

def wholsalesystem():
    def sub():
        f2.destroy()
        fr.destroy()
        billmaker()
    def send():
        messagebox.askyesno("Do you want to creat pdf for sharing purpose", "your PDF created successfully")
        if YES:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', size=15)
            pdf.set_text_color(0, 0, 0)
            f = open(f"E:\\PROGRAMMS\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
            pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png", x=45, y=0)
            for x in f:
                pdf.cell(200, 7, txt=x, ln=100, align="C")
            pdf.output(f"E:\\PROGRAMMS\\ {bill_number.get()}.pdf")

    def pending():
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png",x=45,y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pendinglogoo.jpg", x=120, y=220)
        pdf.set_text_color(0, 0, 0)
        f = open(f"E:\\pending_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pending_bills\\ {bill_number.get()}.pdf")


    def paid():
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "x")
        print("file is created successfully")
        f.write(f"{textarea.get('4.31', END)}")
        messagebox.showinfo("operation completed", "your file created successfully")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\Screenshot544.png", x=45, y=0)
        pdf.image("E:\\PROGRAMMS\\python\\GUI of Python\\pade1.png",x=150,y=240)
        pdf.set_text_color(0, 0, 0)
        pdf.text(x=75, y=290, txt="!Thankyou Visit Again!")
        f = open(f"E:\\pade_bills\\costomer name {costomer_name.get()} bill-number {(bill_number.get())}.txt", "r")
        for x in f:
            pdf.cell(200, 7, txt=x, ln=100, align="C")
        pdf.output(f"E:\\pade_bills\\ {bill_number.get()}.pdf")

    def generate_number():
        global number
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
        number = ""
        for i in range(10):
            number = number + random.choice(list)
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number = ""
        for i in range(8):
            number = number + random.choice(list)
            bill_number.set(number)

    imgemp = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(30, 30))

    def frame():
        global total
        global amount
        global costomer_name
        global contact_no
        global bill_number
        global weight
        global westage
        global tonch
        global goldrate
        global category
        global makingcharge
        global fr

        total = IntVar()
        amount = StringVar()
        category = StringVar()
        goldrate = StringVar()
        tonch = StringVar()
        weight = StringVar()
        westage = StringVar()
        makingcharge = StringVar()
        f2 = Frame(root, width=1600, height=800)
        fr = ctk.CTkFrame(root, corner_radius=40, width=1450, height=750, fg_color="white", bg_color="coral")
        fr.place(x=20, y=20)
        f2.configure(bg="coral")
        f2.pack(fill=BOTH)
        Label(fr, text="Wholesale Billing System", font="comicsm 40 bold", bg="white").place(x=400, y=20)
        lf = LabelFrame(fr, border=4, text="Costomor Detail", width=1250, height=80, relief=GROOVE, bg="white")
        lf.place(x=100, y=100)

        # ================================product frame

        pf = LabelFrame(fr, text="Ornaments", border=4, width=500, height=450, relief=GROOVE, bg="white")
        pf.place(x=100, y=187)
        Label(pf, text="Select Category", font=("comicsm 15 bold"), bg="white").place(x=10, y=2)
        category = ttk.Combobox(pf, value=("Nose pins", "          Nath", "           Bali", "         Tops", "       Ring's", "       Bugdi"), font="c 15 bold",
                                width=40, state='readonly')
        category.place(x=10, y=30)

        def calculate():
            total = f"{(float(weight.get()) * int(goldrate.get())) * (int(tonch.get()) + int(westage.get()))}"
            # during calculation take care of tupel and mathmetical otations
            # amount.set(total)
            # amount.set(total[:-5])
            ant = total[:-5]
            value=(int(ant)+int(makingcharge.get()))
            amount.set(value)

        def calculator():
            from calci import Calculator
            calc = Calculator()
            calc.run()

        def clearbill():
            textarea.destroy()
            s.destroy()
            text()

        def additem():
            weight.set("")
            tonch.set("")
            westage.set("")
            amount.set("")
            category.set(value="Select New Item")

        Label(pf, text="Enter Weight", font=("comicsm 15 bold"), bg="white").place(x=10, y=60)
        Entry(pf, textvariable=weight, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=90)
        Label(pf, text="Enter Westage", font=("comicsm 15 bold"), bg="white").place(x=10, y=120)
        Entry(pf, textvariable=westage, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=150)
        Label(pf, text="Enter Tonch", font=("comicsm 15 bold"), bg="white").place(x=10, y=180)
        Entry(pf, textvariable=tonch, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=210)
        Label(pf, text="Enter Gold Rate", font=("comicsm 15 bold"), bg="white").place(x=10, y=240)
        Entry(pf, textvariable=goldrate, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=270)

        Label(pf, text="Enter Making Charge", font=("comicsm 15 bold"), bg="white").place(x=10, y=300)
        Entry(pf, textvariable=makingcharge, width=41, border=1, bg="white", font="c 15 bold", borderwidth=1,
              relief=SUNKEN).place(x=10, y=330)

        costom_ammount = StringVar()
        Label(pf, text="Ammount :", font=("comicsm 15 bold"), bg="white").place(x=10, y=364)
        Label(pf, textvariable=amount, font=("comicsm 15 bold"), bg="white", border=5).place(x=140, y=363)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Calculate",
                      font=("roman", 20, "bold"), command=calculate).place(x=210, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Calculator", font=("roman", 20, "bold"), command=calculator).place(x=310, y=390)

        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="PDF", font=("roman", 20, "bold"), command=send).place(x=420, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white",
                      text="Clear Bill", font=("roman", 20, "bold"), command=clearbill).place(x=110, y=390)
        ctk.CTkButton(pf, width=50, height=10, corner_radius=20, fg_color="coral", text_color="white", text="Add item",
                      font=("roman", 20, "bold"), command=additem).place(x=10, y=390)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        bf = LabelFrame(fr, text="Bill Frame", border=4, width=730, height=530, relief=GROOVE, bg="white")
        bf.place(x=620, y=185)

        # ----------------------------------------------------------------------------------------------------textarea
        def text():
            global text
            global textarea
            global s
            s = Scrollbar(bf)
            s.pack(side=RIGHT, fill=Y)
            textarea = Text(bf, width=64, height=23.5, font=("Airal 14 bold"), yscrollcommand=s.set)
            s.config(command=textarea.yview)
            textarea.pack()

        text()

        def my_time():
            global t
            t = StringVar()
            timestr = strftime("  %x")
            lf.config(text=timestr, font=("times", 10, "bold"))
            t.set(timestr)

        my_time()

        def show():
            if category.get() != 0:
                textarea.insert(END,
                                f"{(category.get())}       {(weight.get())}         {(tonch.get())}             {(westage.get())}              {goldrate.get()}                {makingcharge.get()}                {amount.get()}\n\n")

        def creatbill():
            textarea.insert(END, "\t\t       GAYATRI JEWELLERS\n")
            textarea.insert(END, "\t\t  Shree Sidhi Bilding shop no:5\n")
            textarea.insert(END, "\t\t         SarafBazar Nashik\n")
            textarea.insert(END, "\t\tph-no:8308090190 / 9552720348\n")
            textarea.insert(END,
                            f"\n\n\nCostomer Name:{(costomer_name.get())} \t\t\t\t           Contact Number:{(contact_no.get())}")
            textarea.insert(END,
                            f"\n\nBill Number:{(bill_number.get())}\t                                                     Date:{t.get()}")
            textarea.insert(END,
                            f"\n________________________________________________________________\nOrnament\t    Weight    Tonch    Westage    Goldrate    makingcharge    Price")
            textarea.insert(END,
                            "\n---------------------------------------------------------------------------------------------------------------------\n")

        def clear():
            goldrate.set("")
            weight.set("")
            tonch.set("")
            westage.set("")
            costom_ammount.set("")
            bill_number.set("")
            costomer_name.set("")
            contact_no.set("")
            category.set("")

        pl = LabelFrame(fr, text="Bill Option", border=4, width=500, height=80, relief=GROOVE, bg="white")
        ctk.CTkButton(pl, text="add", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=show).place(x=100, y=9)
        ctk.CTkButton(pl, text="pending", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=pending).place(x=370, y=9)
        ctk.CTkButton(pl, text="creat", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=creatbill).place(x=10, y=9)
        ctk.CTkButton(pl, text="pade", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=paid).place(x=280, y=9)
        ctk.CTkButton(pl, text="clear", font=("Aiiral", 20, "bold"), fg_color="coral", text_color="white",
                      corner_radius=20, width=5, command=clear).place(x=185, y=9)
        pl.place(x=100, y=650)
        bill_number = StringVar()
        costomer_name = StringVar()
        contact_no = StringVar()

        # =============================================set entry
        Entry(lf, textvariable=bill_number, font=(" c 13 bold"), border=0).place(x=120, y=13)
        Entry(lf, textvariable=costomer_name, font=(" c 13 bold"), border=0).place(x=630, y=13)
        Entry(lf, textvariable=contact_no, font=(" c 13 bold"), border=0).place(x=1015, y=13)

        Label(lf, text="Bill Number", font=("Airal 10 bold"), bg="white").place(x=20, y=15)
        Label(lf, text="________________________", borderwidth=0, font=("Airal 10 bold"), bg="white").place(x=110, y=33)
        ctk.CTkButton(lf, text="Generate Number", text_color="white", fg_color="red", corner_radius=20,
                      command=generate_number, font=("Airal", 20, "bold")).place(x=280, y=20)
        Label(lf, text="Costomer Name", font=("Airal 10 bold"), bg="white").place(x=500, y=15)
        Label(lf, text="__________________________________", font=("Airal 10 bold"), bg="white").place(x=610, y=33)
        Label(lf, text="Contact Number", font=("Airal 10 bold"), bg="white").place(x=900, y=15)
        Label(lf, text="________________________", font=("Airal 10 bold"), bg="white").place(x=1010, y=33)

        ctk.CTkButton(fr, text="Back", fg_color="red", text_color="white", corner_radius=20,
                      font=("Airal", 20, "bold"), command=sub).place(x=20, y=50)
        ctk.CTkLabel(fr, image=imgemp, text="Employ", compound=LEFT).place(x=30, y=10)

    frame()

    def time():
        timestr = strftime("%H:%M:%S %p  %A")
        lf.config(text=timestr)
        lf.after(1000, time)

    lf = Label(fr, font=("times", 20, "bold"), bg="white")
    lf.place(x=1130, y=40)
    time()



def billmaker():
    def exitbillmaker():
        f5.destroy()
        mainhome()
    f2.destroy()
    global f5
    f5=Frame(root,width="1500",height="800")
    f5.configure(bg="coral")
    f5.pack()
    ctk.CTkButton(f5, text="Back", fg_color="red", text_color="white", corner_radius=20,border_width=2,border_color="black",
                  font=("Airal", 20, "bold"), command=exitbillmaker).place(x=20, y=50)

    Label(f5,text="Select Billing System",font="comicsm 50 bold",bg="coral",fg="white").place(x=400,y=50)
    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\3594449 (1).png"),
        size=(100, 80))

    button6 = ctk.CTkButton(f5, image=img, height=200, width=200, corner_radius=0, bg_color="coral", fg_color="coral",
                            text="Select",
                            text_color="black",
                            hover_color="coral"
                            ).place(x=650, y=330)

    button9 = ctk.CTkButton(f5, text="Retail Billing System", text_color="white", fg_color="coral",
                            font=('comic sans ms', 30),
                            width=300, height=80, corner_radius=30, border_width=10, border_color="white",
                            border_spacing=8,command=retail).place(x=850, y=500)

    button9 = ctk.CTkButton(f5, text="Wholsale Billing System", text_color="white", fg_color="coral",
                            font=('comic sans ms', 30),
                            width=300, height=80, corner_radius=30, border_width=10, border_color="white",
                            border_spacing=8,command=wholsalesystem).place(x=250, y=500)

    button9 = ctk.CTkButton(f5, text="Metal Billing System", text_color="white", fg_color="coral",
                            font=('comic sans ms', 30),
                            width=300, height=80, corner_radius=30, border_width=10, border_color="white",
                            border_spacing=8,command=Mettalsystem).place(x=850, y=300)
    button9 = ctk.CTkButton(f5, text="Quantity Billing System", text_color="white", fg_color="coral",
                            font=('comic sans ms', 30),
                            width=300, height=80, corner_radius=30, border_width=10, border_color="white",
                            border_spacing=8,command=Quantityystem).place(x=250, y=300)

def admin():
    def backtomain():
        f4.destroy()
        mainhome()
    f1.destroy()
    f3.destroy()
    f4=Frame(root,width="1500",height="800",bg="white")
    f4.configure(bg="coral")
    f4.pack()
    Label(f4,text="Admin Login",font="comicsm 50 bold",bg="coral",fg="white").place(x=510,y=120)

    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\5166970.png"),
        size=(100, 80))

    img3 = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\an-inclusive-workplace-employees-protection-filled-outline-icon-illustration-color-editable-eps-10-free-vector.jpg"),
        size=(100, 80))

    img4 = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\pngtree-coin-money-icon-png-image_2049478.jpg"),
        size=(100, 80))

    img5 = ctk.CTkImage(
        Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\4146551-200.png"),
        size=(100, 80))

    def invent():
        def sub():
            frame.destroy()
            admin()
        f4.destroy()
        frame = Frame(root, width=1500, height=800)
        frame.configure(bg="coral")
        frame.pack()

        def searchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from products where " + str(search_by.get()) + " LIKE   '%" + str(search.get()) + "%' ")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        def getdata(ev):
            curosor = stabel.focus()
            contents = stabel.item(curosor)
            row = contents['values']
            sr_no.set(row[0])
            name.set(row[1])
            weight.set(row[2])
            quantaty.set(row[3])
            in_stock.set(row[4])

        def fetchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from products")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        def deletedata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("delete from products where sr_no=%s", sr_no.get())
            con.commit()
            con.close()
            fetchdata()

        def updatedata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("update products set name=%s,weight=%s,quantaty=%s,in_stock=%s where sr_no=%s", (
                name.get(),
                weight.get(),
                quantaty.get(),
                in_stock.get(),
                sr_no.get()

            ))
            con.commit()
            fetchdata()
            con.close()

        def adddata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("insert into products values(%s,%s,%s,%s,%s)", (
                sr_no.get(),
                name.get(),
                weight.get(),
                quantaty.get(),
                in_stock.get()
            ))
            con.commit()
            fetchdata()
            con.close()

        def addfrm():
            def sub():
                a1.destroy()

            a1 = LabelFrame(frame, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="-Back-", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="Add ", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=adddata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Add Product", font="Airal 25 bold", bg="white")
            l.place(x=130, y=10)
            Label(a1, text="product sr no :", bg="white", font="c 12 bold").place(x=20, y=100)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=125)
            Entry(a1, font="c 12 bold", border=0, textvariable=sr_no).place(x=180, y=100)

            Label(a1, text="product name :", bg="white", font="c 12 bold").place(x=20, y=170)
            Entry(a1, font="c 12 bold", border=0, textvariable=name).place(x=180, y=170)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=195)

            Label(a1, text="weight :", bg="white", font="c 12 bold").place(x=20, y=240)
            Entry(a1, font="c 12 bold", border=0, textvariable=weight).place(x=180, y=240)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=265)

            Label(a1, text="quantity :", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=quantaty).place(x=180, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=335)

            Label(a1, text="in stock:", bg="white", font="c 12 bold").place(x=20, y=380)
            Entry(a1, font="c 12 bold", border=0, textvariable=in_stock).place(x=200, y=380)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=405)

        def deletefrm():

            def sub():
                a1.destroy()

            a1 = LabelFrame(frame, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="-Back-", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="Delete", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=deletedata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Delete Product", font="Airal 25 bold", bg="white")
            l.place(x=130, y=10)
            Label(a1, text="product sr no :", bg="white", font="c 12 bold").place(x=20, y=100)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=125)
            Entry(a1, font="c 12 bold", border=0, textvariable=sr_no).place(x=180, y=100)

            Label(a1, text="product name :", bg="white", font="c 12 bold").place(x=20, y=170)
            Entry(a1, font="c 12 bold", border=0, textvariable=name).place(x=180, y=170)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=195)

            Label(a1, text="weight :", bg="white", font="c 12 bold").place(x=20, y=240)
            Entry(a1, font="c 12 bold", border=0, textvariable=weight).place(x=180, y=240)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=265)

            Label(a1, text="quantity :", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=quantaty).place(x=180, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=335)

            Label(a1, text="in stock :", bg="white", font="c 12 bold").place(x=20, y=380)
            Entry(a1, font="c 12 bold", border=0, textvariable=in_stock).place(x=200, y=380)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=405)

        def updatefrm():

            def sub():
                a1.destroy()

            a1 = LabelFrame(frame, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="-Back-", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="Update", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=updatedata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Update Product", font="Airal 25 bold", bg="white")
            l.place(x=100, y=10)
            Label(a1, text="product sr no :", bg="white", font="c 12 bold").place(x=20, y=100)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=125)
            Entry(a1, font="c 12 bold", border=0, textvariable=sr_no).place(x=180, y=100)

            Label(a1, text="product name :", bg="white", font="c 12 bold").place(x=20, y=170)
            Entry(a1, font="c 12 bold", border=0, textvariable=name).place(x=180, y=170)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=195)

            Label(a1, text="weight :", bg="white", font="c 12 bold").place(x=20, y=240)
            Entry(a1, font="c 12 bold", border=0, textvariable=weight).place(x=180, y=240)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=265)

            Label(a1, text="quantity :", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=quantaty).place(x=180, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=335)

            Label(a1, text="in stock :", bg="white", font="c 12 bold").place(x=20, y=380)
            Entry(a1, font="c 12 bold", border=0, textvariable=in_stock).place(x=200, y=380)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=405)

        # ========================tabel frame==============================

        invframe = ctk.CTkFrame(frame, width=1460, height=750, corner_radius=50)
        invframe.configure(fg_color="white")
        invframe.pack(pady=20)
        # _------------------------------------------------------------------------------------------------------------
        inmg = ctk.CTkImage(
            Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\555555555.png"),
            size=(50, 40))
        label = ctk.CTkLabel(invframe, image=inmg, bg_color="white", fg_color="white", text="Admin", compound="left")
        label.place(x=20, y=10)

        ctk.CTkButton(invframe, text="Back", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=110, command=sub).place(x=15, y=50)

        Label(invframe, text="Inventory Management", font=("times", 50, "bold"), bg="white").place(x=400, y=10)

        def time():
            timestr = strftime("%H:%M:%S %p ")
            lf.config(text=timestr)
            lf.after(1000, time)

        global search_by
        global search
        search = StringVar()
        search_by = StringVar()
        lf = Label(invframe, font=("times", 20, "bold"), bg="white")
        lf.place(x=1250, y=40)
        time()
        # menue work------------------------------------------------------------------------------------------
        pf = LabelFrame(invframe, text="Menu", border=4, width=500, height=595, relief=GROOVE, bg="white")
        pf.place(x=40, y=115)
        ctk.CTkButton(pf, text="Search", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=110, border_spacing=1, border_color="white", border_width=2,
                      command=searchdata).place(x=350, y=80)
        ttk.Combobox(pf, value=("sr_no", "name", "weight"), font="roman 15 bold", state='readonly', width=30,
                     textvariable=search_by).place(x=120, y=20)
        # ==============================================================================

        Label(pf, text="By Name / Id", bg="white", font="bold").place(x=10, y=20)
        Entry(pf, font="c 12 bold", width=25, textvariable=search).place(x=120, y=80)  # search ===============
        Label(pf, text="Product Option", bg="white", font="bold").place(x=10, y=120)
        ctk.CTkButton(pf, text="ADD-PRODUCT", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=addfrm).place(x=40, y=180)
        ctk.CTkButton(pf, text="UPDATE-PRODUCT", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=updatefrm).place(x=40, y=240)
        ctk.CTkButton(pf, text="DELETE-PRODUCT", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold",), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=deletefrm).place(x=40, y=300)
        ctk.CTkButton(pf, text="Exit", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white",
                      border_width=2,command=sub).place(
            x=180, y=480)

        # ======================================tabel frame----------------------------------------
        pd = LabelFrame(invframe, border=4, width=840, height=400, relief=GROOVE, bg="white")
        pd.place(x=550, y=120)

        # ======================================================start
        def show():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()

        def getdata(ev):
            curosor = stabel.focus()
            contents = stabel.item(curosor)
            row = contents['values']
            sr_no.set(row[0])
            name.set(row[1])
            weight.set(row[2])
            quantaty.set(row[3])
            in_stock.set(row[4])

        def fetchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from products")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        # ttk for tree view of data

        sr_no = StringVar()
        name = StringVar()
        weight = StringVar()
        quantaty = StringVar()
        in_stock = StringVar()

        # ========================tabel frame==============================
        global stabel
        scrollx = Scrollbar(pd, orient=HORIZONTAL)
        scrolly = Scrollbar(pd, orient=VERTICAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        stabel = ttk.Treeview(pd, columns=("sr_no", "name", "weight", "quantaty", "in_stock"),
                              xscrollcommand=scrollx.set,
                              yscrollcommand=scrolly.set)
        scrollx.config(command=stabel.xview)
        scrolly.config(command=stabel.yview)
        stabel.heading("sr_no", text="sr_no")
        stabel.heading("name", text="name")
        stabel.heading("weight", text="weight")
        stabel.heading("quantaty", text="quantaty")
        stabel.heading("in_stock", text="in_stock")
        stabel['show'] = 'headings'
        stabel.column("sr_no", width=160)
        stabel.column("name", width=160)
        stabel.column("weight", width=160)
        stabel.column("quantaty", width=160)
        stabel.column("in_stock", width=160)
        fetchdata()
        stabel.configure(height=27)
        stabel.pack(fill=BOTH, expand=1)
        stabel.bind('<ButtonRelease-1>', getdata)


    button1 = ctk.CTkButton(f4, text="inventory", image=img, height=150, width=150, corner_radius=30, hover_color="white",
                           fg_color="white", text_color="black", border_width=2, border_spacing=5, border_color="black",
                           compound="top",command=invent).place(x=350,y=300)

    def pending_bill():
        def sub():
            frm.destroy()
            admin()
        f4.destroy()
        frm = Frame(root, width=1500, height=800)
        frm.configure(bg="coral")
        frm.pack()

        def searchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute(
                "select*from pending_list where " + str(search_by.get()) + " LIKE   '%" + str(search.get()) + "%' ")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        def getdata(ev):
            curosor = stabel.focus()
            contents = stabel.item(curosor)
            row = contents['values']
            bill_number.set(row[0])
            biller_name.set(row[1])
            total_amount.set(row[2])
            paid_amount.set(row[3])
            product_name.set(row[4])
            purchasing_date.set(row[5])
            last_payment_date.set(row[6])

        def fetchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from pending_list")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        def deletedata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("delete from pending_list where bill_number=%s", bill_number.get())
            con.commit()
            con.close()
            fetchdata()

        def updatedata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute(
                "update pending_list set biller_name=%s,total_amount=%s,paid_amount=%s,product_name=%s,purchasing_date=%s,last_payment_date=%s where bill_number=%s",
                (
                    biller_name.get(),
                    total_amount.get(),
                    paid_amount.get(),
                    product_name.get(),
                    purchasing_date.get(),
                    last_payment_date.get(),
                    bill_number.get()
                ))
            con.commit()
            fetchdata()
            con.close()

        def adddata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("insert into pending_list values(%s,%s,%s,%s,%s,%s,%s)", (
                bill_number.get(),
                biller_name.get(),
                total_amount.get(),
                paid_amount.get(),
                product_name.get(),
                purchasing_date.get(),
                last_payment_date.get()
            ))
            con.commit()
            fetchdata()
            con.close()

        def addfrm():
            def sub():
                a1.destroy()

            a1 = LabelFrame(frm, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="Back", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="add", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=adddata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Add Product", font="Airal 25 bold", bg="white")
            l.place(x=130, y=10)
            Label(a1, text="bill_number :", bg="white", font="c 12 bold").place(x=20, y=70)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=90)
            Entry(a1, font="c 12 bold", border=0, textvariable=bill_number).place(x=180, y=70)

            Label(a1, text=" biller_name:", bg="white", font="c 12 bold").place(x=20, y=130)
            Entry(a1, font="c 12 bold", border=0, textvariable=biller_name).place(x=180, y=130)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=150)

            Label(a1, text="total_amount :", bg="white", font="c 12 bold").place(x=20, y=190)
            Entry(a1, font="c 12 bold", border=0, textvariable=total_amount).place(x=180, y=190)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=210)

            Label(a1, text="paid_amount :", bg="white", font="c 12 bold").place(x=20, y=250)
            Entry(a1, font="c 12 bold", border=0, textvariable=paid_amount).place(x=180, y=250)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=270)

            Label(a1, text="product_name:", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=product_name).place(x=200, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=330)

            Label(a1, text="purchasing_date:", bg="white", font="c 12 bold").place(x=20, y=370)
            Entry(a1, font="c 12 bold", border=0, textvariable=purchasing_date).place(x=200, y=370)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=390)

            Label(a1, text="last_payment_date:", bg="white", font="c 12 bold").place(x=20, y=430)
            Entry(a1, font="c 12 bold", border=0, textvariable=last_payment_date).place(x=200, y=430)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=450)

        def deletefrm():

            def sub():
                a1.destroy()

            a1 = LabelFrame(frm, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="Back", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="delete", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=deletedata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Delete Product", font="Airal 25 bold", bg="white")
            l.place(x=130, y=10)
            Label(a1, text="bill_number :", bg="white", font="c 12 bold").place(x=20, y=70)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=90)
            Entry(a1, font="c 12 bold", border=0, textvariable=bill_number).place(x=180, y=70)

            Label(a1, text=" biller_name:", bg="white", font="c 12 bold").place(x=20, y=130)
            Entry(a1, font="c 12 bold", border=0, textvariable=biller_name).place(x=180, y=130)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=150)

            Label(a1, text="total_amount :", bg="white", font="c 12 bold").place(x=20, y=190)
            Entry(a1, font="c 12 bold", border=0, textvariable=total_amount).place(x=180, y=190)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=210)

            Label(a1, text="paid_amount :", bg="white", font="c 12 bold").place(x=20, y=250)
            Entry(a1, font="c 12 bold", border=0, textvariable=paid_amount).place(x=180, y=250)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=270)

            Label(a1, text="product_name:", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=product_name).place(x=200, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=330)

            Label(a1, text="purchasing_date:", bg="white", font="c 12 bold").place(x=20, y=370)
            Entry(a1, font="c 12 bold", border=0, textvariable=purchasing_date).place(x=200, y=370)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=390)

            Label(a1, text="last_payment_date:", bg="white", font="c 12 bold").place(x=20, y=430)
            Entry(a1, font="c 12 bold", border=0, textvariable=last_payment_date).place(x=200, y=430)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=450)

        def updatefrm():

            def sub():
                a1.destroy()

            a1 = LabelFrame(frm, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="Back", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="update", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=updatedata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Update Product", font="Airal 25 bold", bg="white")
            l.place(x=100, y=10)
            Label(a1, text="bill_number :", bg="white", font="c 12 bold").place(x=20, y=70)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=90)
            Entry(a1, font="c 12 bold", border=0, textvariable=bill_number).place(x=180, y=70)

            Label(a1, text=" biller_name:", bg="white", font="c 12 bold").place(x=20, y=130)
            Entry(a1, font="c 12 bold", border=0, textvariable=biller_name).place(x=180, y=130)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=150)

            Label(a1, text="total_amount :", bg="white", font="c 12 bold").place(x=20, y=190)
            Entry(a1, font="c 12 bold", border=0, textvariable=total_amount).place(x=180, y=190)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=210)

            Label(a1, text="paid_amount :", bg="white", font="c 12 bold").place(x=20, y=250)
            Entry(a1, font="c 12 bold", border=0, textvariable=paid_amount).place(x=180, y=250)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=270)

            Label(a1, text="product_name:", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=product_name).place(x=200, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=330)

            Label(a1, text="purchasing_date:", bg="white", font="c 12 bold").place(x=20, y=370)
            Entry(a1, font="c 12 bold", border=0, textvariable=purchasing_date).place(x=200, y=370)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=390)

            Label(a1, text="last_payment_date:", bg="white", font="c 12 bold").place(x=20, y=430)
            Entry(a1, font="c 12 bold", border=0, textvariable=last_payment_date).place(x=200, y=430)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=450)

        # ========================tabel frame==============================

        invframe = ctk.CTkFrame(frm, width=1460, height=750, corner_radius=50)
        invframe.configure(fg_color="white")
        invframe.pack(pady=20)
        # _------------------------------------------------------------------------------------------------------------
        inmg = ctk.CTkImage(
            Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\555555555.png"),
            size=(50, 40))
        label = ctk.CTkLabel(invframe, image=inmg, bg_color="white", fg_color="white", text="Admin", compound="left")
        label.place(x=20, y=10)

        ctk.CTkButton(invframe, text="Back", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=110, command=sub).place(x=15, y=50)

        Label(invframe, text="Pending Bill Sections", font=("times", 50, "bold"), bg="white").place(x=400, y=10)

        def time():
            timestr = strftime("%H:%M:%S %p ")
            lf.config(text=timestr)
            lf.after(1000, time)

        global search_by
        global search
        search = StringVar()
        search_by = StringVar()
        lf = Label(invframe, font=("times", 20, "bold"), bg="white")
        lf.place(x=1250, y=40)
        time()
        # menue work------------------------------------------------------------------------------------------
        pf = LabelFrame(invframe, text="Menu", border=4, width=500, height=595, relief=GROOVE, bg="white")
        pf.place(x=40, y=115)
        ctk.CTkButton(pf, text="Search", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=110, border_spacing=1, border_color="white", border_width=2,
                      command=searchdata).place(x=370, y=80)
        ttk.Combobox(pf, value=("bill_number", "name", "total_amount", "paid_amount", "last_payment_date", "purchasing_date"),
                     font="roman 15 bold", state='readonly', width=30, textvariable=search_by).place(x=150, y=20)
        # ==============================================================================

        Label(pf, text="Name Id Amount", bg="white", font="bold").place(x=10, y=20)
        Entry(pf, font="c 12 bold", width=25, textvariable=search).place(x=120, y=80)  # search ===============
        Label(pf, text="Product Option", bg="white", font="bold").place(x=10, y=120)
        ctk.CTkButton(pf, text="ADD MEMBER", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=addfrm).place(x=40, y=180)
        ctk.CTkButton(pf, text="UPDATE MEMBER", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=updatefrm).place(x=40, y=240)
        ctk.CTkButton(pf, text="DELETE MEMBER", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold",), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=deletefrm).place(x=40, y=300)
        ctk.CTkButton(pf, text="Exit", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white",
                      border_width=2,command=sub).place(
            x=180, y=480)

        # ======================================tabel frame----------------------------------------
        pd = LabelFrame(invframe, border=4, width=840, height=400, relief=GROOVE, bg="white")
        pd.place(x=550, y=120)

        # ======================================================start

        def getdata(ev):
            curosor = stabel.focus()
            contents = stabel.item(curosor)
            row = contents['values']
            bill_number.set(row[0])
            biller_name.set(row[1])
            total_amount.set(row[2])
            paid_amount.set(row[3])
            product_name.set(row[5])
            purchasing_date.set(row[6])
            last_payment_date.set(row[7])

        def fetchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from pending_list")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        # ttk for tree view of data

        bill_number = StringVar()
        biller_name = StringVar()
        total_amount = StringVar()
        paid_amount = StringVar()
        product_name = StringVar()
        purchasing_date = StringVar()
        last_payment_date = StringVar()

        # ========================tabel frame==============================
        global stabel

        scrolly = Scrollbar(pd, orient=VERTICAL)

        scrolly.pack(side=RIGHT, fill=Y)

        stabel = ttk.Treeview(pd, columns=(
            "bill_number", "biller_name", "total_amount", "paid_amount", "product_name", "purchasing_date",
            "last_payment_date"),
                              yscrollcommand=scrolly.set)

        scrolly.config(command=stabel.yview)
        stabel.heading("bill_number", text="bill_number")
        stabel.heading("biller_name", text="biller_name")
        stabel.heading("total_amount", text="total_amount")
        stabel.heading("paid_amount", text="paid_amount")
        stabel.heading("product_name", text="product_name")
        stabel.heading("purchasing_date", text="purchasing_date")
        stabel.heading("last_payment_date", text="last_payment_date")
        stabel['show'] = 'headings'
        stabel.column("bill_number", width=120)
        stabel.column("biller_name", width=120)
        stabel.column("total_amount", width=120)
        stabel.column("paid_amount", width=120)
        stabel.column("product_name", width=120)
        stabel.column("purchasing_date", width=120)
        stabel.column("last_payment_date", width=120)
        fetchdata()
        stabel.configure(height=27)
        stabel.pack(fill=BOTH, expand=1)
        stabel.bind('<ButtonRelease-1>', getdata)
    button3 = ctk.CTkButton(f4, text="pending bill section", image=img3, height=150, width=150, corner_radius=30, hover_color="white",
                           fg_color="white", text_color="black", border_width=2, border_spacing=5, border_color="black",
                           compound="top",command=pending_bill).place(x=550, y=300)

    def Trade():
        def sub():
            frame.destroy()
            admin()
        f4.destroy()

        frame = Frame(root, width=1500, height=800)
        frame.configure(bg="coral")
        frame.pack()

        def searchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from trade where " + str(search_by.get()) + " LIKE   '%" + str(search.get()) + "%' ")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        def getdata(ev):
            curosor = stabel.focus()
            contents = stabel.item(curosor)
            row = contents['values']
            sr_no.set(row[0])
            Date.set(row[1])
            Credit_Amount.set(row[2])
            Debit_Amount.set(row[3])

        def fetchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from trade")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        def deletedata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("delete from trade where sr_no=%s", sr_no.get())
            con.commit()
            con.close()
            fetchdata()

        def updatedata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("update trade set Date=%s,Credit_Amount=%s,Debit_Amount=%s where sr_no=%s", (
                Date.get(),
                Credit_Amount.get(),
                Debit_Amount.get(),
                sr_no.get()

            ))
            con.commit()
            fetchdata()
            con.close()

        def adddata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("insert into trade values(%s,%s,%s,%s)", (
                sr_no.get(),
                Date.get(),
                Credit_Amount.get(),
                Debit_Amount.get()
            ))
            con.commit()
            fetchdata()
            con.close()

        def addfrm():
            def sub():
                a1.destroy()

            a1 = LabelFrame(frame, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="-Back-", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="make change", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=adddata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Add Product", font="Airal 25 bold", bg="white")
            l.place(x=130, y=10)
            Label(a1, text="sr no :", bg="white", font="c 12 bold").place(x=20, y=100)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=125)
            Entry(a1, font="c 12 bold", border=0, textvariable=sr_no).place(x=180, y=100)

            Label(a1, text="Date :", bg="white", font="c 12 bold").place(x=20, y=170)
            Entry(a1, font="c 12 bold", border=0, textvariable=Date).place(x=180, y=170)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=195)

            Label(a1, text="Credit_Amount :", bg="white", font="c 12 bold").place(x=20, y=240)
            Entry(a1, font="c 12 bold", border=0, textvariable=Credit_Amount).place(x=180, y=240)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=265)

            Label(a1, text="Debit_Amount :", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=Debit_Amount).place(x=180, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=335)

        def deletefrm():

            def sub():
                a1.destroy()

            a1 = LabelFrame(frame, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="-Back-", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="make change", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=deletedata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Delete Product", font="Airal 25 bold", bg="white")
            l.place(x=130, y=10)
            Label(a1, text="sr no :", bg="white", font="c 12 bold").place(x=20, y=100)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=125)
            Entry(a1, font="c 12 bold", border=0, textvariable=sr_no).place(x=180, y=100)

            Label(a1, text="Date :", bg="white", font="c 12 bold").place(x=20, y=170)
            Entry(a1, font="c 12 bold", border=0, textvariable=Date).place(x=180, y=170)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=195)

            Label(a1, text="Credit_Amount :", bg="white", font="c 12 bold").place(x=20, y=240)
            Entry(a1, font="c 12 bold", border=0, textvariable=Credit_Amount).place(x=180, y=240)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=265)

            Label(a1, text="Debit_Amount :", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=Debit_Amount).place(x=180, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=335)

        def updatefrm():

            def sub():
                a1.destroy()

            a1 = LabelFrame(frame, width=500, height=600, bg="white", relief=GROOVE)
            a1.place(x=60, y=140)
            ctk.CTkButton(a1, text="-Back-", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=sub).place(
                x=260, y=500)

            ctk.CTkButton(a1, text="make change", fg_color="red", text_color="white", corner_radius=50,
                          font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white", border_width=2,
                          command=updatedata).place(
                x=40, y=500)

            # ---------------------------------------------------------ADD            LABEL---------------------
            l = Label(a1, text="Update Product", font="Airal 25 bold", bg="white")
            l.place(x=100, y=10)
            Label(a1, text=" sr no :", bg="white", font="c 12 bold").place(x=20, y=100)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=125)
            Entry(a1, font="c 12 bold", border=0, textvariable=sr_no).place(x=180, y=100)

            Label(a1, text="Date :", bg="white", font="c 12 bold").place(x=20, y=170)
            Entry(a1, font="c 12 bold", border=0, textvariable=Date).place(x=180, y=170)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=195)

            Label(a1, text="Credit_amount :", bg="white", font="c 12 bold").place(x=20, y=240)
            Entry(a1, font="c 12 bold", border=0, textvariable=Credit_Amount).place(x=180, y=240)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=265)

            Label(a1, text="Debit_amount :", bg="white", font="c 12 bold").place(x=20, y=310)
            Entry(a1, font="c 12 bold", border=0, textvariable=Debit_Amount).place(x=180, y=310)
            Label(a1, text="______________________________________________________________________", bg="white").place(
                x=20,
                y=335)

        # ========================tabel frame==============================

        invframe = ctk.CTkFrame(frame, width=1460, height=750, corner_radius=50)
        invframe.configure(fg_color="white")
        invframe.pack(pady=20)
        # _------------------------------------------------------------------------------------------------------------
        inmg = ctk.CTkImage(
            Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\555555555.png"),
            size=(50, 40))
        label = ctk.CTkLabel(invframe, image=inmg, bg_color="white", fg_color="white", text="Admin", compound="left")
        label.place(x=20, y=10)

        ctk.CTkButton(invframe, text="Back", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=110, command=sub).place(x=15, y=50)

        Label(invframe, text="Trade Management", font=("times", 50, "bold"), bg="white").place(x=400, y=10)

        def time():
            timestr = strftime("%H:%M:%S %p ")
            lf.config(text=timestr)
            lf.after(1000, time)

        global search_by
        global search
        search = StringVar()
        search_by = StringVar()
        lf = Label(invframe, font=("times", 20, "bold"), bg="white")
        lf.place(x=1250, y=40)
        time()
        # menue work------------------------------------------------------------------------------------------
        pf = LabelFrame(invframe, text="Menu", border=4, width=500, height=595, relief=GROOVE, bg="white")
        pf.place(x=40, y=115)
        ctk.CTkButton(pf, text="Search", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=110, border_spacing=1, border_color="white", border_width=2,
                      command=searchdata).place(x=350, y=80)
        ttk.Combobox(pf, value=("sr_no", "Credit_Amount", "Date", "Debit_Amount"), font="roman 15 bold",
                     state='readonly', width=30,
                     textvariable=search_by).place(x=120, y=20)
        # ==============================================================================

        Label(pf, text="Amount /Date", bg="white", font="bold").place(x=10, y=20)
        Entry(pf, font="c 12 bold", width=25, textvariable=search).place(x=120, y=80)  # search ===============
        Label(pf, text="Product Option", bg="white", font="bold").place(x=10, y=120)
        ctk.CTkButton(pf, text="ADD-AMOUNT", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=addfrm).place(x=40, y=180)
        ctk.CTkButton(pf, text="UPDATE-AMOUNT", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=updatefrm).place(x=40, y=240)
        ctk.CTkButton(pf, text="DELETE-AMOUNT", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold",), width=411, border_spacing=1, border_color="white", border_width=2,
                      command=deletefrm).place(x=40, y=300)
        ctk.CTkButton(pf, text="Exit", fg_color="red", text_color="white", corner_radius=50,
                      font=("Airal", 20, "bold"), width=111, border_spacing=1, border_color="white",
                      border_width=2,command=sub).place(
            x=180, y=480)

        # ======================================tabel frame----------------------------------------
        pd = LabelFrame(invframe, border=4, width=840, height=400, relief=GROOVE, bg="white")
        pd.place(x=550, y=120)

        # ======================================================start
        def show():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()

        def getdata(ev):
            curosor = stabel.focus()
            contents = stabel.item(curosor)
            row = contents['values']
            sr_no.set(row[0])
            Date.set(row[1])
            Credit_Amount.set(row[2])
            Debit_Amount.set(row[3])

        def fetchdata():
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select*from trade")
            rows = cur.fetchall()
            if len(rows) != 0:
                stabel.delete(*stabel.get_children())
                for row in rows:
                    stabel.insert('', END, values=row)
                    con.commit()
            con.close()

        # ttk for tree view of data

        sr_no = StringVar()
        Date = StringVar()
        Credit_Amount = StringVar()
        Debit_Amount = StringVar()

        # ========================tabel frame==============================
        global stabel
        scrollx = Scrollbar(pd, orient=HORIZONTAL)
        scrolly = Scrollbar(pd, orient=VERTICAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        stabel = ttk.Treeview(pd, columns=("sr_no", "Date", "Credit_Amount", "Debit_Amount"),
                              xscrollcommand=scrollx.set,
                              yscrollcommand=scrolly.set)
        scrollx.config(command=stabel.xview)
        scrolly.config(command=stabel.yview)
        stabel.heading("sr_no", text="sr_no")
        stabel.heading("Date", text="Date")
        stabel.heading("Credit_Amount", text="Credit_Amount")
        stabel.heading("Debit_Amount", text="Debit_Amount")
        stabel['show'] = 'headings'
        stabel.column("sr_no", width=200)
        stabel.column("Date", width=200)
        stabel.column("Credit_Amount", width=200)
        stabel.column("Debit_Amount", width=200)
        fetchdata()
        stabel.configure(height=27)
        stabel.pack(fill=BOTH, expand=1)
        stabel.bind('<ButtonRelease-1>', getdata)
        root.mainloop()

    button4 = ctk.CTkButton(f4, text=" trade", image=img4, height=150, width=150, corner_radius=30, hover_color="white",
                           fg_color="white", text_color="black", border_width=2, border_spacing=5, border_color="black",
                           compound="top",command=Trade).place(x=750, y=300)

    def about_us():
        def sub():
            framee.destroy()
            admin()
        f4.destroy()
        framee = Frame(root, width=1500, height=800, bg="coral")
        framee.pack()
        l = Label(framee, text="About Us?", bg="coral", font=("Airal", 50, "bold"), fg="white")
        l.place(x=600, y=30)

        l = Label(framee, text="______________________________________", bg="coral", font=("Airal", 50, "bold"),
                  fg="white")
        l.place(x=50, y=100)

        frame = ctk.CTkFrame(framee, width=1300, height=500, corner_radius=20)
        frame.configure(fg_color="white")
        frame.place(x=100, y=220)

        canvas = Canvas(frame, width=200, height=500)
        canvas.place(x=10, y=10)

        # ------------------------------------------------------------------------------------------------

        # =================================================================

        image1 = Image.open(
            "E:\\PROGRAMMS\\python\\GUI of Python\\editedimg1.jpg")
        image2 = ImageTk.PhotoImage(image1)
        l = Label(frame, image=image2)
        l.place(x=10, y=10)

        Label(frame, text="Gayatri jewellers", font=("times", 25, "bold"), bg="white", fg="red").place(x=890, y=10)
        Label(frame, text="Ear rings and Nose pins wholsaler", font=("times", 20, "bold"), bg="white").place(x=790,
                                                                                                             y=70)
        Label(frame, text=" Melting 10 to 80 Tonch always in stock", font=("times", 20, "bold"), bg="white").place(
            x=760,
            y=130)
        Label(frame, text="Fixed Westage 10 % for all", font=("times", 20, "bold"), bg="white").place(x=870, y=190)
        Label(frame, text="but will eliminate corresponding ", font=("times", 20, "bold"), bg="white").place(x=800,
                                                                                                             y=250)
        Label(frame, text="to qyantity", font=("times", 20, "bold"), bg="white").place(x=940, y=310)

        img = ctk.CTkImage(
            Image.open(
                "E:\\PROGRAMMS\\python\\GUI of Python\\4146551-200.png"),
            size=(50, 50))
        label = ctk.CTkLabel(framee, image=img, compound=None, bg_color="coral", fg_color="coral")
        label.place(x=60, y=20)
        ctk.CTkButton(framee, text="Back", fg_color="red", text_color="white", corner_radius=25,
                      font=("Airal", 20, "bold"), command=sub).place(x=20, y=70)
        root.mainloop()

    button5 = ctk.CTkButton(f4, text="about us ", image=img5, height=150, width=150, corner_radius=30, hover_color="white",
                           fg_color="white", text_color="black", border_width=2, border_spacing=5, border_color="black",
                           compound="top",command=about_us).place(x=950, y=300)



    ctk.CTkButton(f4,text="logout",fg_color="red",text_color="white",corner_radius=20,hover_color="grey",font=("Arial",15,"bold"),command=backtomain).place(x=10,y=50)

    image = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\png-transparent-computer-icons-management-admin-silhouette-black-and-white-neck-thumbnail.png"),
        size=(50, 40))
    ctk.CTkLabel(f4,image=image,text="Admin",compound="left",bg_color="coral",fg_color="coral").place(x=30,y=10)

def admin_user():
    if name.get()==""or password=="":
        messagebox.showerror("error","all fields are required")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            mycursor=con.cursor()
        except:
                messagebox.showerror("error","connection is not established try again!")
                return
        query='use stm'
        mycursor.execute(query)
        query="select * from userdata where name=%s and password=%s"
        mycursor.execute(query,(name.get(),password.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showwarning('error',"invalid userrname or password")
        else:
            messagebox.showinfo('welcome',"login sucessfuly")
            admin()
def adminlogin():
    global name
    global password
    global f3
    def dele():
        f3.destroy()
        mainhome()
    f1.destroy()
    f3=Frame(root,width=1500,height=800)
    fr=ctk.CTkFrame(f3,corner_radius=40,width=500,height=700,fg_color="white",bg_color="coral")
    Label(f3,text="Admin Login",font="c 40 bold",bg="white").place(x=585,y=100)
    Label(f3,text="username",font=("roman 20 bold"),bg="white").place(x=550,y=200)

    Label(f3, text="_______________________________", font=("roman 20 bold"),bg="white").place(x=560, y=260)
    Label(f3, text="password", font=("roman 20 bold"),bg="white").place(x=550, y=300)
    name=StringVar()
    password=StringVar()
    Entry(f3,font=("roman 20 bold"),textvariable=name,bg="white",width=30,border=0).place(x=600,y=240)
    Entry(f3,font=("roman 20 bold"),textvariable=password,bg="white",width=30,border=0).place(x=600,y=340)

    Label(f3, text="_____________________________", font=("roman 20 bold"),bg="white").place(x=560, y=370)
    fr.place(x=500,y=50)
    f3.configure(bg="coral")
    f3.pack()
    #___addimg image_________________________________________________________________
    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(50, 40))
    label=ctk.CTkLabel(f3,image=img,bg_color="white",fg_color="white")
    label.place(x=540,y=240)

    img2 = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\666666.jpg"),
        size=(50, 50))
    label=ctk.CTkLabel(f3,image=img2,compound=None,bg_color="white",fg_color="white")
    label.place(x=540,y=340)

    #=============adding  button
    button1=ctk.CTkButton(f3,text="Sign Up",text_color="white",fg_color="orangered",width=400,height=40,corner_radius=100,bg_color="white",hover_color="coral",command=admin_user,font=("times",20,"bold"))
    button1.place(x=550,y=500)

    button2=ctk.CTkButton(f3,text="Back",text_color="white",fg_color="orangered",width=400,height=40,corner_radius=100,bg_color="white",hover_color="coral",command=dele,font=("times",20,"bold"))
    button2.place(x=550,y=570)

    button2=ctk.CTkButton(f3,text="Create Admin Account",text_color="red",fg_color="white",width=400,height=40,corner_radius=100,bg_color="white",hover_color="white",command=create_account2,font=("times",20,"bold"))
    button2.place(x=550,y=640)

def login_user():
    if name.get()==""or password=="":
        messagebox.showerror("error","all fields are required")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            mycursor=con.cursor()
        except:
                messagebox.showerror("error","connection is not established try again!")
                return
        query='use stm'
        mycursor.execute(query)
        query="select * from userdata where name=%s and password=%s"
        mycursor.execute(query,(name.get(),password.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showwarning('error',"invalid userrname or password")
        else:
            messagebox.showinfo('welcome',"login sucessfuly")
            billmaker()
def login():
    global name
    global password
    global f2
    def back():
        f2.destroy()
        mainhome()
    f1.destroy()
    f2=Frame(root,width=1500,height=800)
    fr=ctk.CTkFrame(f2,corner_radius=40,width=500,height=700,fg_color="white",bg_color="coral")
    Label(f2,text="Login",font="c 40 bold",bg="white").place(x=660,y=100)
    Label(f2,text="username",font=("roman 20 bold"),bg="white").place(x=550,y=200)

    Label(f2, text="_______________________________", font=("roman 20 bold"),bg="white").place(x=560, y=260)
    Label(f2, text="password", font=("roman 20 bold"),bg="white").place(x=550, y=300)
    name=StringVar()
    password=StringVar()
    Entry(f2,font=("roman 20 bold"),textvariable=name,bg="white",width=30,border=0).place(x=600,y=240)
    Entry(f2,font=("roman 20 bold"),textvariable=password,bg="white",width=30,border=0).place(x=600,y=340)

    Label(f2, text="_____________________________", font=("roman 20 bold"),bg="white").place(x=560, y=370)
    fr.place(x=500,y=50)
    f2.configure(bg="coral")
    f2.pack()
    #___addimg image_________________________________________________________________
    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(50, 40))
    label=ctk.CTkLabel(f2,image=img,bg_color="white",fg_color="white")
    label.place(x=540,y=240)

    img2 = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\666666.jpg"),
        size=(50, 50))
    label=ctk.CTkLabel(f2,image=img2,compound=None,bg_color="white",fg_color="white")
    label.place(x=540,y=340)

    #=============adding  button
    button1=ctk.CTkButton(f2,text="Sign Up",text_color="white",fg_color="orangered",width=400,height=40,corner_radius=100,bg_color="white",hover_color="coral",command=login_user,font=("times",20,"bold"))
    button1.place(x=550,y=500)

    button2=ctk.CTkButton(f2,text="Back",text_color="white",fg_color="orangered",width=400,height=40,corner_radius=100,bg_color="white",hover_color="coral",command=back,font=("times",20,"bold"))
    button2.place(x=550,y=570)

    button=ctk.CTkButton(f2,text="Create Employ Account",text_color="red",fg_color="white",width=400,height=40,corner_radius=100,bg_color="white",hover_color="white",command=create_account1,font=("times",20,"bold"))
    button.place(x=550,y=640)

def mainhome():
    global mainhome
    global f1
    f1=Frame(root,width="1500",height="800")
    f1.configure(bg="coral")
    f1.pack()

    Label(f1, text="Login As?", font="Arial 50 bold", bg="coral", fg="white").place(x=590, y=100)

    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\78948.png"),
        size=(100, 80))

    img2 = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\555555555.png"),
        size=(100, 80))

    button6 = ctk.CTkButton(f1, image=img, height=200, width=200, corner_radius=0, bg_color="coral", fg_color="coral",
                            text_color="black",
                            hover_color="coral"
                            ).place(x=520, y=280)

    button6 = ctk.CTkButton(f1, image=img2, height=200, width=200, corner_radius=0, bg_color="coral", fg_color="coral",
                            text_color="black",
                            hover_color="coral"
                            ).place(x=520, y=430)

    button9 = ctk.CTkButton(f1, text="Employe", text_color="white", fg_color="coral", font=('comic sans ms', 30),
                            width=300, height=80, corner_radius=30, border_width=10, border_color="white",
                            border_spacing=8,command=login).place(x=650, y=350)

    button9 = ctk.CTkButton(f1, text="Admin", text_color="white", fg_color="coral", font=('comic sans ms', 30),
                            width=300, height=80, corner_radius=30, border_width=10, border_color="white",
                            border_spacing=8,command=adminlogin).place(x=650, y=500)

def start():
    task=5
    x=0
    while (x<task):
        time.sleep(1)
        progressbar['value']+=20
        x+=1
        percent.set(str((x/task)*100)+"%")
        root.update_idletasks()
    if task==5:
        f.destroy()
        mainhome()
def look():
    global f
    global progressbar
    global percent
    percent=IntVar()
    f = Frame(root, width=1500, height=800)
    f.pack()
    f.configure(bg="coral")
    Label(f,text="Gayatri Jewellers",font="Arial 90 bold",bg="coral",fg="white").place(x=250,y=320)
    Label(f,text="Ready to use... !",font="roman 20 bold",bg="coral").place(x=635,y=580)
    Label(root, textvariable=percent,bg="coral",font="roman 20 bold").place(x=690,y=500)
    progressbar = ttk.Progressbar(f)
    progressbar.place(x=250,y=650)
    progressbar.configure(length=1000)
    img = ctk.CTkImage(
        Image.open("E:\\PROGRAMMS\\python\\GUI of Python\\Polish_20210110_155724984.png"),
        size=(150, 200))
    button6 = ctk.CTkButton(f,text="TAP TO START", image=img, height=200, width=200, corner_radius=0,compound="top",bg_color="coral",fg_color="coral",text_color="black",
                            hover_color="coral"
                           ).place(x=620, y=80)

    button9=ctk.CTkButton(f,text="Start",text_color="white",fg_color="coral",font=('comic sans ms',30),width=100,height=50,corner_radius=30,border_width=10,border_color="white",border_spacing=8,command=start).place(x=650,y=700)


def call():
    look()
call()
root.wm_iconbitmap("E:\\PROGRAMMS\\python\\GUI of Python\\gj-letter-logo-square-shape-260nw-736505452 (1) (1).ico")
root.mainloop()
