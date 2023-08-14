from tkinter import *


langelis = ""

def press(num):
    global langelis
    langelis = langelis + str(num)
    lygtis.set(langelis)

def lygybe():
    try:
        global langelis
        total = str(eval(langelis))
        lygtis.set(total)
        langelis = "" 
    except:
        lygtis.set("Klaidingas veiksmas")
        langelis = ""

def isvalyti():
    global langelis
    langelis = ""
    lygtis.set("")

if __name__ == "__main__":
    langas = Tk()
    langas.title("Kalkuliatorius")
    lygtis = StringVar()
   
    # IVEDIMO LANGAS
    e_langelis = Entry(langas, textvariable=lygtis, font=("Ariel", 27))
    e_langelis.grid(columnspan=4)

    # MYGTUKAI
    mygt_1 = Button(langas, text="1", fg="black", bg="lightblue", command= lambda: press(1), height=3, width=5, font=("Ariel", 20))
    mygt_1.grid(row=4, column=0)
    mygt_2 = Button(langas, text="2", fg="black", bg="lightblue", command= lambda: press(2), height=3, width=5, font=("Ariel", 20))
    mygt_2.grid(row=4, column=1)
    mygt_3 = Button(langas, text="3", fg="black", bg="lightblue", command= lambda: press(3), height=3, width=5, font=("Ariel", 20))
    mygt_3.grid(row=4, column=2)
    mygt_4 = Button(langas, text="4", fg="black", bg="lightblue", command= lambda: press(4), height=3, width=5, font=("Ariel", 20))
    mygt_4.grid(row=3, column=0)
    mygt_5 = Button(langas, text="5", fg="black", bg="lightblue", command= lambda: press(5), height=3, width=5, font=("Ariel", 20))
    mygt_5.grid(row=3, column=1)
    mygt_6 = Button(langas, text="6", fg="black", bg="lightblue", command= lambda: press(6), height=3, width=5, font=("Ariel", 20))
    mygt_6.grid(row=3, column=2)
    mygt_7 = Button(langas, text="7", fg="black", bg="lightblue", command= lambda: press(7), height=3, width=5, font=("Ariel", 20))
    mygt_7.grid(row=2, column=0)
    mygt_8 = Button(langas, text="8", fg="black", bg="lightblue", command= lambda: press(8), height=3, width=5, font=("Ariel", 20))
    mygt_8.grid(row=2, column=1)
    mygt_9 = Button(langas, text="9", fg="black", bg="lightblue", command= lambda: press(9), height=3, width=5, font=("Ariel", 20))
    mygt_9.grid(row=2, column=2)
    mygt_0 = Button(langas, text="0", fg="black", bg="lightblue", command= lambda: press(0), height=3, width=5, font=("Ariel", 20))
    mygt_0.grid(row=5, column=0)
    mygt_C = Button(langas, text="C", fg="red", bg="lightblue", command= lambda: isvalyti(), height=3, width=5, font=("Ariel", 20))
    mygt_C.grid(row=5, column=1)
    mygt_lygu = Button(langas, text="=", fg="black", bg="grey", command= lambda: lygybe(), height=3, width=8, font=("Ariel", 20))
    mygt_lygu.grid(row=6, column=3)
    mygt_plus = Button(langas, text="+", fg="black", bg="grey", command= lambda: press("+"), height=3, width=8, font=("Ariel", 20))
    mygt_plus.grid(row=2, column=3)
    mygt_minus = Button(langas, text="-", fg="black", bg="grey", command= lambda: press("-"), height=3, width=8, font=("Ariel", 20))
    mygt_minus.grid(row=3, column=3)
    mygt_daug = Button(langas, text="*", fg="black", bg="grey", command= lambda: press("*"), height=3, width=8, font=("Ariel", 20))
    mygt_daug.grid(row=4, column=3)
    mygt_dal = Button(langas, text="/", fg="black", bg="grey", command= lambda: press("/"), height=3, width=8, font=("Ariel", 20))
    mygt_dal.grid(row=5, column=3)
    mygt_task = Button(langas, text=".", fg="black", bg="lightblue", command= lambda: press("."), height=3, width=5, font=("Ariel", 20))
    mygt_task.grid(row=5, column=2)

    langas.mainloop()

