from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x500")
root.title("Tic Tac Toe Game")
root.resizable(0,0)
root.configure(background='Cadet Blue')

PlayerX=IntVar()
PlayerO=IntVar()
PlayerX.set(0)
PlayerO.set(0)

buttons=StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

def scorekeeper():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won a game")
    if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", " You have just won a Game")
    if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won a game")
    if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", " You have just won a Game")
    if (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won a game")
    if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", " You have just won a Game")
    if (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", " You have just won a Game")
    if (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", " You have just won a Game")

    if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won a game")
    if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", " You have just won a Game")
    if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won a game")
    if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", " You have just won a Game")
    if (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won a game")
    if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", " You have just won a Game")
    if (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", " You have just won a Game")
    if (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", " You have just won a Game")


def nframe():
    # messagebox.showinfo("tic","tac toe")
    hframe.destroy()
    root.geometry("1350x750+0+0")
    Tops=Frame(root,bg='Cadet Blue',pady=2,width=1350,height=100,relief=RIDGE)
    Tops.grid(row=0,column=0)
    lblTitle=Label(Tops,font=("Arial",40,"bold"),text="Tic Tac Toe Game",bg="Cadet Blue",bd=21,justify=CENTER)
    lblTitle.grid(row=0,column=0)


    MainFrame=Frame(root,bg='Powder Blue',bd=10,width=1350,height=600,relief=RIDGE)
    MainFrame.grid(row=1,column=0)

    LeftFrame=Frame(MainFrame,bd=10,width=750,height=500,pady=2,padx=10,relief=RIDGE)
    LeftFrame.pack(side=LEFT)

    RightFrame=Frame(MainFrame,bd=10,width=560,height=500,padx=10,pady=2,relief=RIDGE)
    RightFrame.pack(side=RIGHT)

    RightFrame1=Frame(RightFrame,bd=10,width=560,height=200,padx=10,pady=2,relief=RIDGE)
    RightFrame1.grid(row=0,column=0)

    RightFrame2=Frame(RightFrame,bd=10,width=560,height=200,padx=10,pady=2,relief=RIDGE)
    RightFrame2.grid(row=1,column=0)


    def reset():
        button1['text']=" "
        button2['text'] = " "
        button3['text'] = " "
        button4['text'] = " "
        button5['text'] = " "
        button6['text'] = " "
        button7['text'] = " "
        button8['text'] = " "
        button9['text'] = " "

    def NewGame():
        reset()
        PlayerX.set(0)
        PlayerO.set(0)

    lblPlayerX=Label(RightFrame1,font=('arial 40 bold'),text='Player X:',padx=2,pady=2)
    lblPlayerX.grid(row=0,column=0,sticky=W)
    txtPlayerX=Entry(RightFrame1,font=('arial 40 bold'),bd=2,textvariable=PlayerX,width=14,justify=LEFT).grid(row=0,column=1)

    lblPlayerO=Label(RightFrame1,font=('arial 40 bold'),text='Player O:',padx=2,pady=2)
    lblPlayerO.grid(row=1,column=0,sticky=W)
    txtPlayerO=Entry(RightFrame1,font=('arial 40 bold'),bd=2,textvariable=PlayerO,width=14,justify=LEFT).grid(row=1,column=1)

    # lblPlayer1=Label(RightFrame1,font=('arial 40 bold'),text='Computer:',padx=2,pady=2)
    # lblPlayer1.grid(row=2,column=0,sticky=W)
    # txtPlayer1=Entry(RightFrame1,font=('arial 40 bold'),bd=2,textvariable=PlayerO,width=14,justify=LEFT).grid(row=2,column=1)

    btnReset=Button(RightFrame2,text="Reset",font=('Times 26 bold'),height=1,width=20,command=reset)
    btnReset.grid(row=0,column=0,padx=6,pady=11)
    btnNewGame=Button(RightFrame2,text="New Game",font=('Times 26 bold'),height=1,width=20,command=NewGame)
    btnNewGame.grid(row=1,column=0,padx=6,pady=10)
    button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button1))
    button1.grid(row=1, column=0, sticky=S + N + E + W)
    button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button2))
    button2.grid(row=1, column=1, sticky=S + N + E + W)
    button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button3))
    button3.grid(row=1, column=2, sticky=S + N + E + W)
    button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button4))
    button4.grid(row=2, column=0, sticky=S + N + E + W)
    button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button5))
    button5.grid(row=2, column=1, sticky=S + N + E + W)
    button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button6))
    button6.grid(row=2, column=2, sticky=S + N + E + W)
    button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button7))
    button7.grid(row=3, column=0, sticky=S + N + E + W)
    button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button8))
    button8.grid(row=3, column=1, sticky=S + N + E + W)
    button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro',
                     command=lambda: checker(button9))
    button9.grid(row=3, column=2, sticky=S + N + E + W)

hframe=Frame(root,bg='Cadet blue',pady=2,width=500,height=100,relief=RIDGE)
hframe.grid(row=0,column=0)
btn=Button(root,text="VS Computer",pady=2,width=10,height=5).grid(row=0,column=0)
btn1=Button(root,text="VS Player",pady=2,width=10,height=5,command=nframe).grid(row=1,column=0)
btn2=Button(root,text="Quit",pady=2,width=10,height=5,command=root.destroy).grid(row=2,column=0)

root.mainloop()

#
# lblTitle=Label(Tops,font=("Arial",40,"bold"),text="Tic Tac Toe Game",bg="Cadet Blue",bd=21,justify=CENTER)
# lblTitle.grid(row=0,column=0)
#
#
# MainFrame=Frame(root,bg='Powder Blue',bd=10,width=1350,height=600,relief=RIDGE)
# MainFrame.grid(row=1,column=0)
#
# LeftFrame=Frame(MainFrame,bd=10,width=750,height=500,pady=2,padx=10,relief=RIDGE)
# LeftFrame.pack(side=LEFT)
#
# RightFrame=Frame(MainFrame,bd=10,width=560,height=500,padx=10,pady=2,relief=RIDGE)
# RightFrame.pack(side=RIGHT)
#
# RightFrame1=Frame(RightFrame,bd=10,width=560,height=200,padx=10,pady=2,relief=RIDGE)
# RightFrame1.grid(row=0,column=0)
#
# RightFrame2=Frame(RightFrame,bd=10,width=560,height=200,padx=10,pady=2,relief=RIDGE)
# RightFrame2.grid(row=1,column=0)
#
# PlayerX=IntVar()
# PlayerO=IntVar()
# PlayerX.set(0)
# PlayerO.set(0)
#
# buttons=StringVar()
# click=True
#
# def checker(buttons):
#     global click
#     if buttons["text"]==" " and click==True:
#         buttons["text"]="X"
#         click=False
#         scorekeeper()
#     elif buttons["text"]==" " and click==False:
#         buttons["text"]="O"
#         click=True
#         scorekeeper()
#
# def scorekeeper():
#     if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X","You have just won a game")
#     if (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X"," You have just won a Game")
#     if (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X","You have just won a game")
#     if (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X"," You have just won a Game")
#     if (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X","You have just won a game")
#     if (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X"," You have just won a Game")
#     if (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X"," You have just won a Game")
#     if (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
#         n=float(PlayerX.get())
#         score=(n+1)
#         PlayerX.set(score)
#         messagebox.showinfo("Winner X"," You have just won a Game")
#
#     if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O","You have just won a game")
#     if (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O"," You have just won a Game")
#     if (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O","You have just won a game")
#     if (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O"," You have just won a Game")
#     if (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O","You have just won a game")
#     if (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O"," You have just won a Game")
#     if (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O"," You have just won a Game")
#     if (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
#         n=float(PlayerO.get())
#         score=(n+1)
#         PlayerO.set(score)
#         messagebox.showinfo("Winner O"," You have just won a Game")
#
# def reset():
#     button1['text']=" "
#     button2['text'] = " "
#     button3['text'] = " "
#     button4['text'] = " "
#     button5['text'] = " "
#     button6['text'] = " "
#     button7['text'] = " "
#     button8['text'] = " "
#     button9['text'] = " "
#
# def NewGame():
#     reset()
#     PlayerX.set(0)
#     PlayerO.set(0)
#
# lblPlayerX=Label(RightFrame1,font=('arial 40 bold'),text='Player X:',padx=2,pady=2)
# lblPlayerX.grid(row=0,column=0,sticky=W)
# txtPlayerX=Entry(RightFrame1,font=('arial 40 bold'),bd=2,textvariable=PlayerX,width=14,justify=LEFT).grid(row=0,column=1)
#
# lblPlayerO=Label(RightFrame1,font=('arial 40 bold'),text='Player O:',padx=2,pady=2)
# lblPlayerO.grid(row=1,column=0,sticky=W)
# txtPlayerO=Entry(RightFrame1,font=('arial 40 bold'),bd=2,textvariable=PlayerO,width=14,justify=LEFT).grid(row=1,column=1)
#
# # lblPlayer1=Label(RightFrame1,font=('arial 40 bold'),text='Computer:',padx=2,pady=2)
# # lblPlayer1.grid(row=2,column=0,sticky=W)
# # txtPlayer1=Entry(RightFrame1,font=('arial 40 bold'),bd=2,textvariable=PlayerO,width=14,justify=LEFT).grid(row=2,column=1)
#
# btnReset=Button(RightFrame2,text="Reset",font=('Times 26 bold'),height=1,width=20,command=reset)
# btnReset.grid(row=0,column=0,padx=6,pady=11)
# btnNewGame=Button(RightFrame2,text="New Game",font=('Times 26 bold'),height=1,width=20,command=NewGame)
# btnNewGame.grid(row=1,column=0,padx=6,pady=10)
#
# button1=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button1))
# button1.grid(row=1,column=0,sticky=S+N+E+W)
# button2=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button2))
# button2.grid(row=1,column=1,sticky=S+N+E+W)
# button3=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button3))
# button3.grid(row=1,column=2,sticky=S+N+E+W)
# button4=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button4))
# button4.grid(row=2,column=0,sticky=S+N+E+W)
# button5=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button5))
# button5.grid(row=2,column=1,sticky=S+N+E+W)
# button6=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button6))
# button6.grid(row=2,column=2,sticky=S+N+E+W)
# button7=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button7))
# button7.grid(row=3,column=0,sticky=S+N+E+W)
# button8=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button8))
# button8.grid(row=3,column=1,sticky=S+N+E+W)
# button9=Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button9))
# button9.grid(row=3,column=2,sticky=S+N+E+W)
