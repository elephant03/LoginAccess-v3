'''
For next version include arrow keys to naigate the text and make root work properly without the user
needing to fill in the brakets- from my standpoit that is too hard to do this late but for the new version it
might work
-Good luck me
'''


class Main():
    Defults = {
        "Bg_Colour": "#7eccf7",

        "Font": ("Arial", 15),
        "Title_Font": ("Arial", 45, "bold"),
        "SubTitle_Font": ("Arial", 20, "bold"),
        "Font_Colour": "Black",


        "Btn_Bg": "#2db4ff",
        "Btn_Active": "#2da9ff",

        "QuitBtn_Bg": "#ef2804",
        "QuitBtn_Active": "#e82502"
    }

    Bg_Colour = Defults["Bg_Colour"]

    Font = Defults["Font"]
    Title_Font = Defults["Title_Font"]
    SubTitle_Font = Defults["SubTitle_Font"]
    Font_Colour = Defults["Font_Colour"]

    Btn_Bg = Defults["Btn_Bg"]
    Btn_Active = Defults["Btn_Active"]

    QuitBtn_Bg = Defults["QuitBtn_Bg"]
    QuitBtn_Active = Defults["QuitBtn_Active"]

    Frames = []

    Sum_str = ""
    Sum_str_List = []
    Display_str = ""

    Answered = False
    Answer = ""

    def __init__(self, Root):
        import tkinter as TK

        self.Frames = []

        self.Root = Root
        self.Root.title("Calculator")

        self.Icon_file = __file__[:-14] + "CalculatorIcon.ico"

        self.Root.wm_iconbitmap(self.Icon_file)
        self.Root.configure(bg=self.Bg_Colour)
        self.Root.geometry("557x393")
        self.Frames.append(self.Root)

        self.Top_Frame = TK.Frame(self.Root, bg=self.Bg_Colour)
        self.Top_Frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.Frames.append(self.Top_Frame)

        self.Display_lbl = TK.Label(self.Top_Frame, bg="white", text="",
                                    font=self.Font, fg=self.Font_Colour, activeforeground=self.Font_Colour)
        self.Display_lbl.grid(row=0, column=0, columnspan=5, sticky="nsew")

        #self.Setting_btn = TK.Button(self.Top_Frame, bg = self.Btn_Bg, text = "Settings", activebackground = self.Btn_Active, font = self.Font, fg = self.Font_Colour, activeforeground = self.Font_Colour, command = lambda: self.Settings())
        #self.Setting_btn.grid(row = 0, column = 5, sticky = "nsew")

        self.Number_fr = TK.Frame(self.Root, bg=self.Bg_Colour)
        self.Number_fr.grid(row=1, column=0, sticky="nsew")
        self.Frames.append(self.Number_fr)

        self.Numbers = [[1, 2, 3, " "], [4, 5, 6, " "],
                        [7, 8, 9, " "], [".", 0, "Ans", " "]]
        self.Symbols = [["+", "-", "*", "/"],
                        ["Power", "Root", " ", "="], ["C", "Del", "(", ")"]]

        self.No_Buttons = []

        for i in range(0, len(self.Numbers)):
            for n in range(0, len(self.Numbers[i])):
                self.No_Btn = TK.Button(self.Number_fr, text=self.Numbers[i][n], font=self.Font, fg=self.Font_Colour, activeforeground=self.Font_Colour,
                                        bg=self.Btn_Bg, activebackground=self.Btn_Active, command=lambda Symbol=self.Numbers[i][n]: self.Sum(Symbol))
                self.No_Btn.grid(row=i, column=n, sticky="nsew")
                if(self.Numbers[i][n] == " "):
                    self.No_Btn.configure(state=TK.DISABLED)

        self.Symbols_fr = TK.Frame(self.Root, bg=self.Bg_Colour)
        self.Symbols_fr.grid(row=1, column=1, sticky="nsew")
        self.Frames.append(self.Symbols_fr)

        for i in range(0, len(self.Symbols)):
            for n in range(0, len(self.Symbols[i])):
                self.Symbol_btn = TK.Button(self.Symbols_fr, text=self.Symbols[i][n], font=self.Font, fg=self.Font_Colour, activeforeground=self.Font_Colour,
                                            bg=self.Btn_Bg, activebackground=self.Btn_Active, command=lambda Symbol=self.Symbols[i][n]: self.Sum(Symbol))
                self.Symbol_btn.grid(row=n, column=i, sticky="nsew")
                if(self.Symbols[i][n] == " "):
                    self.Symbol_btn.configure(state=TK.DISABLED)

        for i in range(len(self.Frames)):
            self.Align_Grid(self.Frames[i])

    def Sum(self, Symbol):

        if(self.Answered):
            self.Sum_Symbol = ""
            self.Display_Symbol = ""
            self.Sum_str = ""
            self.Display_str = ""

            self.Display_lbl.configure(text=self.Display_str)
            self.Display_lbl.update()

            self.Answered = False

        self.Sum_Symbol = str(Symbol)
        self.Display_Symbol = str(Symbol)

        if(str(Symbol) == "Power"):
            self.Sum_Symbol = "**"
            self.Display_Symbol = "^"

        if(str(Symbol) == "Root"):
            self.Sum_Symbol = "**(1/"
            self.Display_Symbol = "√"

        if(str(Symbol) == "C"):
            self.Sum_Symbol = ""
            self.Display_Symbol = ""
            self.Sum_str = ""
            self.Display_str = ""

        if(str(Symbol) == "Ans"):
            self.Sum_Symbol = self.Answer
            self.Display_Symbol = self.Answer

        if(str(Symbol) == "="):
            self.Sum_Symbol = ""
            try:
                self.Answer = str(eval(self.Sum_str))
                self.Display_str = ""
                self.Display_Symbol = self.Answer

            except:
                self.Sum_Symbol = ""
                self.Display_Symbol = ""
                self.Sum_str = ""
                self.Display_str = ""

                self.Display_lbl.configure(text=self.Display_str)
                self.Display_lbl.update()

                self.Sum_Symbol = ""
                self.Display_Symbol = "Error"

            self.Answered = True

        if(str(Symbol) == "Del"):
            self.Sum_Symbol = ""
            self.Display_Symbol = ""
            self.Sum_str = self.Sum_str[:-
                                        len(self.Sum_str_List[len(self.Sum_str_List)-1])]
            self.Display_str = self.Display_str[:-1]
            self.Sum_str_List = self.Sum_str_List[:-1]
        else:
            self.Sum_str_List.append(self.Sum_Symbol)

        self.Sum_str += str(self.Sum_Symbol)
        self.Display_str += str(self.Display_Symbol)

        self.Display_lbl.configure(text=self.Display_str)
        self.Display_lbl.update()

    def Align_Grid(self, Frame):
        # Aligns the grid
        self.Grid_Size = Frame.grid_size()

        for i in range(self.Grid_Size[0]):
            Frame.columnconfigure(i, weight=3)
        for i in range(self.Grid_Size[1]):
            Frame.rowconfigure(i, weight=3)
            if(Frame == self.Frames[0] and i == 0):
                Frame.rowconfigure(i, weight=1)

    '''
    def Settings(self):

        self.Setting_tl = TK.Toplevel(self.Root, bg = self.Bg_Colour)
        self.Setting_tl.title("Settings")
        self.Setting_tl.geometry("")
        self.Setting_widgets = []

        self.Options_fr = TK.Frame(self.Setting_tl, bg = self.Bg_Colour)
        self.Options_fr.grid(row = 0, column = 0, sticky = "nsew")

        self.Options = ["Colours", "Font", "Reset", "", "Quit"]

        for i in range(0,len(self.Options)):
            self.Setting = TK.Button(self.Options_fr, text = self.Options[i], font = self.Font, foreground = self.Font_Colour, bg = self.Btn_Bg, activebackground = self.Btn_Active, command = lambda e = self.Options[i]: self.Option(e))
            self.Setting.grid(row = i, column = 0, sticky = "nsew")

            self.Setting_widgets.append(self.Setting)

            if(self.Options[i] == ""):
                self.Setting.configure(state = TK.DISABLED)

        self.Align_Grid(self.Setting_tl)
        self.Align_Grid(self.Options_fr)

        
        self.Warning_tl = TK.Toplevel(self.Root, bg = self.Bg_Colour)
        self.Warning_tl.title("WARNING")

        self.Warning_lbl = TK.Label(self.Warning_tl, bg = self.Bg_Colour, font = self.Font, fg = self.Font_Colour, text = "Sorry but due to prgraming errors this isn't working see Version 3.0 notes")
        self.Warning_lbl.pack()


    def Option(self, Selection):
        if(Selection == "Colours"):
            self.Colour_Frame = TK.Frame(self.Setting_tl, bg = self.Bg_Colour)
            self.Colour_Frame.grid(row = 0, column = 0, sticky = "nsew")

            self.Colour_Options = ["Background","Forground","Button","Clicked button"]
            self.Colour_Option_Widgets = []

            for i in range(len(self.Colour_Options)):
                self.Colour_Option_lbl = TK.Label(self.Colour_Frame, bg = self.Bg_Colour, text = self.Colour_Options[i], font = self.Font, fg = self.Font_Colour, activeforeground = self.Font_Colour)
                self.Colour_Option_lbl.grid(row = i, column = 0, sticky = "nsew")

                self.Colour_Option_ent = TK.Entry(self.Colour_Frame, font = self.Font, fg = self.Font_Colour)
                self.Colour_Option_ent.insert(0,"Hex colour code")
                self.Colour_Option_ent.grid(row = i, column = 1, sticky = "nsew", padx = 10, pady = 50)

                self.Colour_Option_Widgets.append(self.Colour_Option_ent)

            
            self.Save_btn = TK.Button(self.Colour_Frame, bg = self.Btn_Bg, fg = self.Font_Colour, activebackground = self.Btn_Active, activeforeground = self.Font_Colour, font = self.Font, text = "Save", command = lambda: self.Change_Colour())
            self.Save_btn.grid(row = 4, column = 1, sticky = "nsew")

            self.Quit_btn = TK.Button(self.Colour_Frame, bg = self.QuitBtn_Bg, fg = self.Font_Colour, activebackground = self.QuitBtn_Active, activeforeground = self.Font_Colour, font = self.Font, text = "QUIT", command = lambda: self.Colour_Quit)
            self.Quit_btn.grid(row = 4,column = 0, sticky = "nsew")

            self.Align_Grid(self.Colour_Frame)
    
    def Change_Colour(self):

        self.Hex_Codes = []

        for i in range(len(self.Colour_Option_Widgets)):
            self.Hex_Code = self.Colour_Option_Widgets[i].get()
            self.Hex_Codes.append(self.Hex_Code)
        
        if(self.Hex_Codes[0][0] == "#"):
            self.Bg_Colour = self.Hex_Codes[0]
        if(self.Hex_Codes[1][0] == "#"):
            self.Font_Colour = self.Hex_Codes[1]
        if(self.Hex_Codes[2][0] == "#"):
            self.Btn_Bg = self.Hex_Codes[2]
        if(self.Hex_Codes[3][0]):
            self.Btn_Active = self.Hex_Codes[3]
    
    '''


def Run():
    import tkinter as TK

    Root = TK.Tk()

    Main(Root)

    while True:
        try:
            Root.update_idletasks()
            Root.update()
        except:
            break


if __name__ == "__main__":
    import tkinter as TK

    Root = TK.Tk()

    Run = Main(Root)

    while True:
        try:
            Root.update_idletasks()
            Root.update()
        except:
            break
