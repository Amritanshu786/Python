import tkinter
from tkinter import *
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

lb1 =Label(
    root,text ="Label",
    anchor =SE,
    font =("Verdana",20)
    )
lb1.pack(expand =True, fill ="both")
btnrow1 =Frame(root,bg="black")
btnrow1.pack(expand =True, fill ="both",)

btnrow2 =Frame(root,bg="blue")
btnrow2.pack(expand =True, fill ="both")

btnrow3 =Frame(root,bg="green")
btnrow3.pack(expand =True, fill ="both")

btnrow4 =Frame(root,bg="pink")
btnrow4.pack(expand =True, fill ="both")


btn1 =Button(
    btnrow1,
    text ="1",
    font =("Verdana",22)
    )
btn1.pack(side =LEFT, expand =True, fill ="both")

btn2 =Button(
    btnrow1,
    text ="2",
    font =("Verdana",22)
    )
btn2.pack(side =LEFT, expand =True, fill ="both")

btn3 =Button(
    btnrow1,
    text ="3",
    font =("Verdana",22)
    )
btn3.pack(side =LEFT, expand =True, fill ="both")

btn4 =Button(
    btnrow1,
    text ="4",
    font =("Verdana",22)
    )
btn4.pack(side =RIGHT, expand =True, fill ="both")



btn1 =Button(
    btnrow2,
    text ="5",
    font =("Verdana",22)
    )
btn1.pack(side =LEFT, expand =True, fill ="both")

btn2 =Button(
    btnrow2,
    text ="6",
    font =("Verdana",22)
    )
btn2.pack(side =LEFT, expand =True, fill ="both")

btn3 =Button(
    btnrow2,
    text ="7",
    font =("Verdana",22)
    )
btn3.pack(side =LEFT, expand =True, fill ="both")

btn4 =Button(
    btnrow2,
    text ="8",
    font =("Verdana",22)
    )
btn4.pack(side =RIGHT, expand =True, fill ="both")




btn1 =Button(
    btnrow3,
    text ="*",
    font =("Verdana",22)
    )
btn1.pack(side =LEFT, expand =True, fill ="both")

btn2 =Button(
    btnrow3,
    text ="0",
    font =("Verdana",22)
    )
btn2.pack(side =LEFT, expand =True, fill ="both")

btn3 =Button(
    btnrow3,
    text ="9",
    font =("Verdana",22)
    )
btn3.pack(side =LEFT, expand =True, fill ="both")

btn4 =Button(
    btnrow3,
    text ="=",
    font =("Verdana",22)
    )
btn4.pack(side =RIGHT, expand =True, fill ="both")





btn1 =Button(
    btnrow4,
    text ="+",
    font =("Verdana",22)
    )
btn1.pack(side =LEFT, expand =True, fill ="both")

btn2 =Button(
    btnrow4,
    text ="-",
    font =("Verdana",22)
    )
btn2.pack(side =LEFT, expand =True, fill ="both")

btn3 =Button(
    btnrow4,
    text ="*",
    font =("Verdana",22)
    )
btn3.pack(side =LEFT, expand =True, fill ="both")

btn4 =Button(
    btnrow4,
    text ="/",
    font =("Verdana",22)
    )
btn4.pack(side =RIGHT, expand =True, fill ="both")
root.mainloop()
