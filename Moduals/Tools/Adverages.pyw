#Imports the tkinter and text editor moduals
import tkinter as TK
from statistics import median, mode, StatisticsError #There is also a mean however, it is inaccurate

def Adverage(Type):
    Answer = 0
    global Number_ent
    global Answer_fr

    Numbers = Number_ent.get().split(",")
    for i in range(len(Numbers)):#Sets all of the numbers to ints
        try:
            Numbers[i] = float(Numbers[i])
        except ValueError:
            Type = "DUD"
            Answer = "This input was invalid please try again"

    if Type == "Mean":#Calculates the mean manually due to python statistics error
        for i in range(len(Numbers)):
            Answer += Numbers[i]
        Answer = Answer/len(Numbers)
    elif Type == "Mode":#Uses the statistics.mode test to find mode or say if there are multipble common ones
        try:
            Answer = mode(Numbers)
        except StatisticsError as Error:
            Answer = Error
    elif Type == "Median":#Output the median
        Answer = median(Numbers)

    Answer_lbl = TK.Label(Answer_fr, bg = "#7eccf7", font = ("Arial",15), text = Answer)#Displays the answer or error
    Answer_lbl.grid(sticky = "nsew", row = 0, column = 0, padx = 3, pady = 3)

    Align_Grid(Answer_fr)
    return

def Quit():#Safly exits the program
    root.destroy()
    raise SystemExit


def Align_Grid(Frame):#Sets every section of a frames grid to weight 1 so they expand
    Grid_Size = Frame.grid_size()

    for i in range(Grid_Size[0]):
        Frame.columnconfigure(i, weight = 1)
    for i in range(Grid_Size[1]):
        Frame.rowconfigure(i, weight = 1)
    return

def Run():
    #creates the screen and sets it up
    global root
    root = TK.Tk()
    root.title("Adverages")
    root.config(bg = "#7eccf7")

    #Gives the instructions to the programes funcition
    Help_lbl = TK.Label(root, font = ("Arial",15), text = "Please enter your numbers with a comma placed between each one\nWhen you've finished, press the appropriate button")
    Help_lbl.config(bg = "#7eccf7")
    Help_lbl.grid(sticky = "nsew", row = 0, column = 0, columnspan = 2, pady = 3, padx = 3)

    #Creats the window for entering text with a label
    Number_lbl = TK.Label(root, font = ("Arial",15), text = "Numbers", bg = "#7eccf7")
    Number_lbl.grid(sticky = "nsew", row = 1, column = 0, pady = 3, padx = 3)

    global Number_ent

    Number_ent = TK.Entry(root, font = ("Arial",15))
    Number_ent.grid(sticky = "nsew", row = 1, column = 1, pady = 3, padx = 3)

    #Creates a space for the answers to be displayed

    global Answer_fr
    Answer_fr = TK.Frame(root, bg = "#7eccf7")
    Answer_fr.grid(sticky = "nsew", row = 2, column = 0, columnspan = 2)

    #Buttons to say if you want mean median or mode and sets them into there own frame
    global Adverage_fr
    Adverage_fr = TK.Frame(root, bg = "#7eccf7")
    Adverage_fr.grid(sticky = "nsew", row = 3, column = 0, columnspan = 2)

    Mean_btn = TK.Button(Adverage_fr, font = ("Arial",15), bg = "#2db4ff", activebackground = "#2da9ff", text = "Mean", command = lambda: Adverage("Mean"))
    Mean_btn.grid(sticky = "nsew", row = 0, column = 0, pady = 3, padx = 3)
    Median_btn = TK.Button(Adverage_fr, font = ("Arial",15), bg = "#2db4ff", activebackground = "#2da9ff", text = "Median", command = lambda: Adverage("Median"))
    Median_btn.grid(sticky = "nsew", row = 0, column = 1, pady = 3, padx = 3)
    Mode_btn = TK.Button(Adverage_fr, font = ("Arial",15), bg = "#2db4ff", activebackground = "#2da9ff", text = "Mode", command = lambda: Adverage("Mode"))
    Mode_btn.grid(sticky = "nsew", row = 0, column = 2, pady = 3, padx = 3)

    #Quit button
    Quit_btn = TK.Button(Adverage_fr, font = ("Arial",15), bg = "#ef2804", activebackground = "#e82502", text= "QUIT", command = lambda: Quit())
    Quit_btn.grid(sticky = "nsew", row = 1, column = 1, padx = 3, pady = 3)

    Align_Grid(root)
    Align_Grid(Adverage_fr)

    root.mainloop()
