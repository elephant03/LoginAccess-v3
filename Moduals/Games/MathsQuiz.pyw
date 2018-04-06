'''
'''
import random as rn
import tkinter as TK

class Main:

    BgColour = "#7eccf7"

    Font = ("Arial", 14)
    Font_Title = ("Arial", 18)

    Counter = 1

    def __init__(self, root):
        self.Counter = 1
        self.root = root
        self.root.title("Math quiz")
        self.root.config(bg = self.BgColour)

        self.Start_fr = TK.Frame(self.root, bg = self.BgColour)
        self.Start_fr.grid(row = 0, column = 0 ,sticky = "nsew")

        self.Score = 0

        self.Align_Grid(self.root)

        self.Start_Screen()
    
    def Start_Screen(self):
        self.root.geometry("300x200")

        self.Title = TK.Label(self.Start_fr, bg = self.BgColour, font = self.Font_Title, text = "Math Quiz!")
        self.Title.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew", padx = 3, pady = 10)

        self.Quit_btn = TK.Button(self.Start_fr, bg = "red", font = self.Font, text = "QUIT", command = lambda: self.Quit())
        self.Quit_btn.grid(row = 1, column = 0, sticky = "nsew", padx = 3, pady = 3)


        self.StrVar = TK.StringVar(self.Start_fr)
        self.StrVar.set("Normal")

        self.Mode_dd = TK.OptionMenu(self.Start_fr, self.StrVar, "Normal", "Hard", "Super Hard","Survival")
        self.Mode_dd.config(bg = self.BgColour, activebackground = self.BgColour, font = self.Font)
        self.Mode_dd["menu"].config(bg = self.BgColour, font = self.Font)
        self.Mode_dd["highlightthickness"] = 0
        self.Mode_dd.grid(row = 1, column = 1, sticky = "nsew", padx = 3, pady = 4)

        self.Expailnation_lbl = TK.Label(self.Start_fr, bg = self.BgColour, text = "?", font = self.Font)
        self.Expailnation_lbl.grid(row = 1, column = 2, sticky = "nsew", padx = 1, pady = 4)

        self.Expailnation_lbl.bind("<Enter>", lambda e: self.Explain(0))
        self.Expailnation_lbl.bind("<Leave>", lambda e: self.Explain(1))


        self.Start_btn = TK.Button(self.Start_fr, bg = "green", text= "Start", font = self.Font_Title, command = lambda: self.Start())
        self.Start_btn.grid(row = 2, column = 0, columnspan = 3, sticky = "nsew", padx = 3, pady = 3)

        self.Align_Grid(self.Start_fr)

    def Explain(self, Type):
        if Type == 1:
            self.Explaination_tl.destroy()
            return
        self.Explaination_tl = TK.Toplevel(self.Start_fr, bg = self.BgColour)

        self.ExpailnationText_lbl = TK.Label(self.Explaination_tl, bg = self.BgColour, font = self.Font, text = "Normal- 5 easy questions\nHard- 5 hard questions\nSuper Hard- 10 hard questions with division\nSurvival- Keep going until you get a question worng")
        self.ExpailnationText_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 3, pady = 3)
        

    def Start(self):
        self.Counter = 0

        self.root.geometry("300x150")

        self.NumRange = 20
        self.Operators = ["+", "-", "*"]

        if self.StrVar.get().lower() == "hard" or self.StrVar.get().lower() == "super hard":
            self.NumRange = 50
        if self.StrVar.get().lower() == "super hard":
            self.Operators.append("/")
        
        self.Question = "{Num1} {Symbol} {Num2}".format(Num1 = rn.randint(-self.NumRange, self.NumRange), Symbol = rn.choice(self.Operators), Num2 = rn.randint(-self.NumRange, self.NumRange))

        self.Quiz_fr = TK.Frame(self.root, bg = self.BgColour)
        self.Quiz_fr.grid(row = 0, column = 0, sticky = "nsew")

        self.Score_lbl = TK.Label(self.Quiz_fr, bg = self.BgColour, font = self.Font_Title, text = "Score:\n{}".format(self.Score))
        self.Score_lbl.grid(row = 0 ,column = 0, sticky = "nsew", padx = 2, pady = 3)

        self.Question_lbl = TK.Label(self.Quiz_fr, bg = self.BgColour, font = self.Font_Title, text = self.Question)
        self.Question_lbl.grid(row = 0, column = 1, sticky = "nsew", padx = 1, pady = 3)

        self.Answer_lbl = TK.Label(self.Quiz_fr, bg = self.BgColour, font = self.Font, text = "Answer:")
        self.Answer_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 3)

        self.Answer_ent = TK.Entry(self.Quiz_fr, font = self.Font)
        self.Answer_ent.grid(row = 1, column = 1, sticky = "nsew", padx = 3, pady = 3)

        self.Enter_btn = TK.Button(self.Quiz_fr, bg = "green", text = "Enter", font = self.Font_Title, command = lambda: self.Check("1"))
        self.Enter_btn.grid(row = 2, column = 0, columnspan = 2, padx = 3, pady = 3)

        self.Align_Grid(self.Quiz_fr)

        self.Answer_ent.bind("<Return>", lambda e: self.Check("1"))
        self.Answer_ent.focus()
    
    def Check(self, Type):
        if Type == 0:
            self.Answer_ent.config(state = "normal")
            self.Answer_ent.update()
            self.Answer_ent.update_idletasks()

            self.NextQuestion()
            return
        if str(eval(self.Question)) == str(self.Answer_ent.get()):
            self.String = "Well done!"

            self.Score += 1
            self.Score_lbl.config(text = "Score:\n{}".format(self.Score))
            self.Score_lbl.update()
            self.Score_lbl.update_idletasks()
        else:
            if self.StrVar.get().lower() == "survival":
                self.End()
                return
            else:
                self.String = "Sorry it was: {}".format(str(eval(self.Question)))
        
        self.Answer_ent.config(state = "disabled")
        self.Answer_ent.update()
        self.Answer_ent.update_idletasks()

        self.Question_lbl.config(text = self.String)
        self.Question_lbl.update()
        self.Question_lbl.update_idletasks()

        self.NextQuestion_btn = TK.Button(self.Quiz_fr, bg = "green", text = "Next Question", font = self.Font_Title, command = lambda: self.Check(0))
        self.NextQuestion_btn.grid(row = 2, column = 0, columnspan = 2,padx = 3, pady = 3)

        self.Answer_ent.bind("<Return>", lambda e: self.Check(0))


    def NextQuestion(self):
        self.NextQuestion_btn.destroy()

        self.Answer_ent.bind("<Return>", lambda e: self.Check("1"))

        self.Answer_ent.delete(0, "end")
        self.Answer_ent.update()
        self.Answer_ent.update_idletasks()

        self.Question = "{Num1} {Symbol} {Num2}".format(Num1 = rn.randint(-self.NumRange, self.NumRange), Symbol = rn.choice(self.Operators), Num2 = rn.randint(-self.NumRange, self.NumRange))
        
        self.Counter += 1
        if((self.StrVar.get().lower() == "normal" or self.StrVar.get().lower() == "hard") and self.Counter == 5):
            self.End()
            return
        elif(self.StrVar.get().lower() == "super hard" and self.Counter == 10):
            self.End()
            return

        self.Question_lbl.config(text = self.Question)
        self.Question_lbl.update()
        self.Question_lbl.update_idletasks()

    def End(self):
        self.Quiz_fr.destroy()
        
        self.root.geometry("300x200")

        self.End_fr = TK.Frame(self.root, bg = self.BgColour)
        self.End_fr.grid(row = 0, column = 0, sticky = "nsew", padx = 3, pady = 3)

        self.End_lbl = TK.Label(self.End_fr, font = self.Font, bg = self.BgColour, text = "End!")
        self.End_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 3, pady = 3)

        self.Overveiw_fr = TK.Frame(self.End_fr, bg = self.BgColour)
        self.Overveiw_fr.grid(row = 1, column = 0, sticky = "nsew", padx = 3, pady = 3)

        self.OverveiwScore_lbl = TK.Label(self.Overveiw_fr, font = self.Font, bg = self.BgColour, text = "Your final score is: {}".format(self.Score))
        self.OverveiwScore_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 3, pady = 3)

        self.OvereiwQuestions_lbl = TK.Label(self.Overveiw_fr, font = self.Font, bg = self.BgColour, text = "Your completed {} questions!".format(self.Counter))
        self.OvereiwQuestions_lbl.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "nsew")

        self.Button_fr = TK.Frame(self.End_fr, bg = self.BgColour)
        self.Button_fr.grid(row = 2, column = 0, sticky = "nsew", padx = 3, pady = 3)

        self.EndQuit_btn = TK.Button(self.Button_fr, bg = "red", font = self.Font, text = "QUIT", command = lambda: self.Quit())
        self.EndQuit_btn.grid(row = 0, column = 0, sticky = "nsew", padx = 3, pady = 3)

        self.Mneu_btn = TK.Button(self.Button_fr, bg = "lawn green", font = self.Font, text = "Menu", command = lambda: self.Menu())
        self.Mneu_btn.grid(row = 0, column = 1, sticky = "nsew", padx = 3, pady = 3)

        self.Play_btn = TK.Button(self.Button_fr, bg = "green", font = self.Font, text = "Play Again", command = lambda: self.Again())
        self.Play_btn.grid(row = 0, column = 2, padx = 3, pady = 3, sticky = "nsew")

        self.Align_Grid(self.Button_fr)
        self.Align_Grid(self.Overveiw_fr)
        self.Align_Grid(self.End_fr)

        self.Score = 0

    def Menu(self):
        self.End_fr.destroy()
    
    def Again(self):
        self.End_fr.destroy()
        
        self.Start()

    def Quit(self):
        self.root.destroy()
        raise SystemExit
    
    def Align_Grid(self,Frame):
        self.Grid_Size = Frame.grid_size()

        for i in range(self.Grid_Size[0]):
            Frame.columnconfigure(i, weight = 3)
        for i in range(self.Grid_Size[1]):
            Frame.rowconfigure(i, weight = 3)

def Run():
    root = TK.Tk()

    Run = Main(root)
    
    root.mainloop()

if __name__ == "__main__":
    root = TK.Tk()

    Run = Main(root)
    
    root.mainloop()
