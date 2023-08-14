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
        lygtis.set("ERR0R")
        langelis = ""

def isvalyti():
    global langelis
    langelis = ""
    lygtis.set("")

if __name__ == "__main__":
    langas = Tk()
    lygtis = StringVar()
    e_langelis = Entry(langas, textvariable=lygtis, font=("Ariel", 24))
    e_langelis.grid(columnspan=4)

    myg_1 = Button(langas, text="1", fg="black", bg="lightgrey", command= lambda: press(1), height=3, width=5, font=("Ariel", 20))
    myg_1.grid(row=4, column=0)
    myg_2 = Button(langas, text="2", fg="black", bg="lightgrey", command= lambda: press(2), height=3, width=5, font=("Ariel", 20))
    myg_2.grid(row=4, column=1)
    myg_3 = Button(langas, text="3", fg="black", bg="lightgrey", command= lambda: press(3), height=3, width=5, font=("Ariel", 20))
    myg_3.grid(row=4, column=2)
    myg_4 = Button(langas, text="4", fg="black", bg="lightgrey", command= lambda: press(4), height=3, width=5, font=("Ariel", 20))
    myg_4.grid(row=3, column=0)
    myg_5 = Button(langas, text="5", fg="black", bg="lightgrey", command= lambda: press(5), height=3, width=5, font=("Ariel", 20))
    myg_5.grid(row=3, column=1)
    myg_6 = Button(langas, text="6", fg="black", bg="lightgrey", command= lambda: press(6), height=3, width=5, font=("Ariel", 20))
    myg_6.grid(row=3, column=2)
    myg_7 = Button(langas, text="7", fg="black", bg="lightgrey", command= lambda: press(7), height=3, width=5, font=("Ariel", 20))
    myg_7.grid(row=2, column=0)
    myg_8 = Button(langas, text="8", fg="black", bg="lightgrey", command= lambda: press(8), height=3, width=5, font=("Ariel", 20))
    myg_8.grid(row=2, column=1)
    myg_9 = Button(langas, text="9", fg="black", bg="lightgrey", command= lambda: press(9), height=3, width=5, font=("Ariel", 20))
    myg_9.grid(row=2, column=2)
    myg_0 = Button(langas, text="0", fg="black", bg="lightgrey", command= lambda: press(0), height=3, width=5, font=("Ariel", 20))
    myg_0.grid(row=5, column=0)
    myg_C = Button(langas, text="C", fg="black", bg="lightgrey", command= lambda: isvalyti(), height=3, width=5, font=("Ariel", 20))
    myg_C.grid(row=5, column=1)
    myg_lygu = Button(langas, text="=", fg="black", bg="#FF8C00", command= lambda: lygybe(), height=3, width=5, font=("Ariel", 20))
    myg_lygu.grid(row=6, column=3)
    myg_plus = Button(langas, text="+", fg="black", bg="#FF8C00", command= lambda: press("+"), height=3, width=5, font=("Ariel", 20))
    myg_plus.grid(row=2, column=3)
    myg_minus = Button(langas, text="-", fg="black", bg="#FF8C00", command= lambda: press("-"), height=3, width=5, font=("Ariel", 20))
    myg_minus.grid(row=3, column=3)
    myg_daug = Button(langas, text="*", fg="black", bg="#FF8C00", command= lambda: press("*"), height=3, width=5, font=("Ariel", 20))
    myg_daug.grid(row=4, column=3)
    myg_dal = Button(langas, text="/", fg="black", bg="#FF8C00", command= lambda: press("/"), height=3, width=5, font=("Ariel", 20))
    myg_dal.grid(row=5, column=3)
    myg_task = Button(langas, text=".", fg="black", bg="lightgrey", command= lambda: press("."), height=3, width=5, font=("Ariel", 20))
    myg_task.grid(row=5, column=2)

    langas.mainloop()

