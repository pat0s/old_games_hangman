# Hangman Game
# Author: Patrik Sehnoutek
# Date: 2017

import random
from tkinter import*
import tkinter
import tkinter.messagebox

canvas = Tk()
canvas.title("Hangman Game")
canvas.geometry('600x600+0+0')
canvas.resizable(False,False) # users can't resize the gamescreen

window_height = 600 # centered gamescreen
window_width = 600

screen_width = canvas.winfo_screenwidth()
screen_height = canvas.winfo_screenheight()

xs = int((screen_width/2) - (window_width/2))
ys = int((screen_height/2) - (window_height/2))
canvas.geometry("{}x{}+{}+{}".format(window_width, window_height, xs, ys))


#=================================Frames=========================================

hangman = Canvas(canvas, width = 600, height = 350)
hangman.pack(side="top")
hangman.configure(background='white')
guess = Canvas(canvas, width = 600, height = 100)
guess.pack()
keyboard = Frame(canvas, width = 600, height = 150)
keyboard.pack(side="bottom")

#==================================Functions======================================


def click(letter):
    global x
    draw(checker(letter,word),letter,listOfLetters)
    if isWinner(word,listOfLetters):
        tkinter.messagebox.showinfo("Winner", "You have just won a game!!!")
        restart(word)
    else:
        
        if checker2(letter,word):
            None
        else:
            x += 1
            Hangman(x)
            if x == 10:
                tkinter.messagebox.showinfo("Lost", "No more attemps. You lost a game!")
                restart(word)
    
def createField(word):

    for i in range(len(word)):
        lbl = Label(guess, text="_", font = ("Velvetica 25 bold"))
        lbl.grid(row = 0, column = i)

def checker(letter,word):
    position = []
    for i in range(len(word)):
        if letter == word[i]:
            position.append(i)
    return position

def checker2(letter,word):
    for i in range(len(word)):
        if letter == word[i]:
            return True
    return False
        

def draw(position, letter,lst):
    for i in position:
        lbl1 = Label(guess, text = letter, font = ("Velvetica 15 bold"))
        lbl1.grid(row = 0, column = i)
        lst[i] = letter

def isWinner(word,lst):
    if list(word) == lst:
        return True
      
def restart(wrd):
    global listOfLetters
    global word
    global x
    
    for i in range(len(wrd)):
        lbl = Label(guess, text="  ", font = ("Velvetica 25 bold"))
        lbl.grid(row = 0, column = i)
        
    word = random.choice(words)
    listOfLetters = [" "]*len(word)
    
    for i in range(len(word)):
        lbl = Label(guess, text="_", font = ("Velvetica 25 bold"))
        lbl.grid(row = 0, column = i)
        
    x = 0
    
    hangman.create_rectangle(200,290,400,80, fill="white", outline = "white")
    hangman.create_rectangle(450,15,590,45, fill = "white", outline = "green")                                      
    hangman.create_text(520,30,font = ("Velvetica 12 bold"),text = str(10-x) + " attemps left", fill="green")
    

def Hangman(x):
    hangman.create_rectangle(450,15,590,45, fill = "white", outline = "red") # hover the old text
    hangman.create_text(520,30,font = ("Velvetica 12 bold"),text = str(10-x) + " attemps left", fill="red") # new text
    
    if x == 1:
        hangman.create_rectangle(200,280,400,290, fill ="brown", outline="black")
    elif x == 2:
        hangman.create_rectangle(220,280,227,80, fill="brown")
    elif x == 3:
        hangman.create_rectangle(227,80,350,87, fill="brown")
    elif x == 4:
        hangman.create_rectangle(345,87,350,110, fill="brown")
    elif x == 5:
        hangman.create_oval(327,110,367,150)
    elif x == 6:
        hangman.create_line(348,150,348,210)
    elif x == 7:
        hangman.create_line(348,170,328,195)
    elif x == 8:
        hangman.create_line(348,170,368,195)
    elif x == 9:
        hangman.create_line(348,210,328,235)
    elif x == 10:
        hangman.create_line(348,210,368,235)
        # eyes
        hangman.create_text(338,123, text = "X")
        hangman.create_text(355,123, text = "X")

    

#------------------------------------Words + StartOfGame---------------------------------------

words = ["CSS", "CODES", "HTML", "TREEHOUSE", "MOUSE", "SCHOOL", "COMPUTER", "NOTEBOOK", "PRINT",
         "PYTHON", "JAVA", "METHOD", "CLASS", "GRID", "INPUT"]
word = random.choice(words)

length = len(word)
listOfLetters = [" "] * length

x = 0

createField(word)
hangman.create_rectangle(450,15,590,45, fill = "white", outline = "green")                                      
hangman.create_text(520,30,font = ("Velvetica 12 bold"),text = str(10-x) + " attemps left", fill="green")

#==================================Keyboard======================================



#-----------------------------------row1---------------------------------------------




btnQ = Button(keyboard, text = "Q", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("Q"))
btnQ.grid(row = 2, column = 0)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 1)

btnW = Button(keyboard, text = "W", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("W"))
btnW.grid(row = 2, column = 2)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 3)

btnE = Button(keyboard, text = "E", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("E"))
btnE.grid(row = 2, column = 4)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 5)

btnR = Button(keyboard, text = "R", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("R"))
btnR.grid(row = 2, column = 6)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 7)

btnT = Button(keyboard, text = "T", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("T"))
btnT.grid(row = 2, column = 8)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 9)

btnZ = Button(keyboard, text = "Z", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("Z"))
btnZ.grid(row = 2, column = 10)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 11)

btnU = Button(keyboard, text = "U", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("U"))
btnU.grid(row = 2, column = 12)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 13)

btnI = Button(keyboard, text = "I", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("I"))
btnI.grid(row = 2, column = 14)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 15)

btnO = Button(keyboard, text = "O", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("O"))
btnO.grid(row = 2, column = 16)
space = Label(keyboard, text = " ")
space.grid(row = 2, column = 17)

btnP = Button(keyboard, text = "P", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("P"))
btnP.grid(row = 2, column = 18)


#-----------------------------------row2---------------------------------------------

btnA = Button(keyboard, text = "A", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("A"))
btnA.grid(row = 3, column = 1)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 2)

btnS = Button(keyboard, text = "S", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("S"))
btnS.grid(row = 3, column = 3)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 4)

btnD = Button(keyboard, text = "D", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("D"))
btnD.grid(row = 3, column = 5)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 6)

btnF = Button(keyboard, text = "F", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("F"))
btnF.grid(row = 3, column = 7)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 8)

btnG = Button(keyboard, text = "G", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("G"))
btnG.grid(row = 3, column = 9)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 10)

btnH = Button(keyboard, text = "H", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("H"))
btnH.grid(row = 3, column = 11)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 12)

btnJ = Button(keyboard, text = "J", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("J"))
btnJ.grid(row = 3, column = 13)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 14)

btnK = Button(keyboard, text = "K", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("K"))
btnK.grid(row = 3, column = 15)
space = Label(keyboard, text = " ")
space.grid(row = 3, column = 16)

btnL = Button(keyboard, text = "L", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("L"))
btnL.grid(row = 3, column = 17)

#-----------------------------------row3---------------------------------------------


btnY = Button(keyboard, text = "Y", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("Y"))
btnY.grid(row = 4, column = 2)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 3)

btnX = Button(keyboard, text = "X", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("X"))
btnX.grid(row = 4, column = 4)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 5)

btnC = Button(keyboard, text = "C", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("C"))
btnC.grid(row = 4, column = 6)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 7)

btnV = Button(keyboard, text = "V", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("V"))
btnV.grid(row = 4, column = 8)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 9)

btnB = Button(keyboard, text = "B", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("B"))
btnB.grid(row = 4, column = 10)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 11)

btnN = Button(keyboard, text = "N", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("N"))
btnN.grid(row = 4, column = 12)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 13)

btnM = Button(keyboard, text = "M", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("M"))
btnM.grid(row = 4, column = 14)
space = Label(keyboard, text = " ")
space.grid(row = 4, column = 15)

btndot = Button(keyboard, text = ".", font = ("Velvetica 12 bold"), height = 1, width = 2, bg = "brown", fg = "white",
              activebackground = "green",activeforeground = "white", command=lambda:click("."))
btndot.grid(row = 4, column = 16)

#-----------------------------------row4---------------------------------------------

space = Label(keyboard, text = " ", height = 3)
space.grid(row = 5, columnspan = 20)


canvas.mainloop()
