'''
A program based off the clasic game master mind
The user will have to guess the order of colours
'''


class Main:

    def __init__(self, root, Defults):
        import tkinter as TK

        self.root = root
        self.root.title("Master Mind")

        self.Background = Defults["Background"]
        self.Foreground = Defults["Foreground"]
        self.Btn_Background = Defults["Btn_Background"]
        self.Btn_Active = Defults["Btn_Active"]
        self.QuitBtn_Background = Defults["QuitBtn_Background"]
        self.QuitBtn_Active = Defults["QuitBtn_Active"]
        self.PositiveBtn_Background = Defults["PositiveBtn_Background"]
        self.PositiveBtn_Active = Defults["PositiveBtn_Active"]
        self.Font = Defults["Font"]
        self.TitleFont = Defults["TitleFont"]
        self.SubTitleFont = Defults["SubTitleFont"]

        self.Main_fr = TK.Frame(self.root, bg=self.Background)
        self.Main_fr.pack(fill=TK.BOTH, expand=True)

        self.StartMenu()

    def StartMenu(self):
        self.StartMenu_fr = self.AddFrame()

        self.Title_lbl = self.AddTitle_lbl(
            0, 0, self.StartMenu_fr, "Master Mind", CSpan=3)

        self.Space_lbl = self.AddSpace_lbl(1, 0, self.StartMenu_fr, CSpan=3)

        self.Username_lbl = self.AddLabel(2, 0, self.StartMenu_fr, "Username:")

        self.Username_ent = self.AddEntry(
            self.StartMenu_fr, 2, 1, Focus=True, CSpan=2)

        self.Space_lbl1 = self.AddSpace_lbl(3, 0, self.StartMenu_fr, CSpan=3)

        self.Quit_btn = self.AddQuit_btn(4, 0, self.StartMenu_fr)

        self.HighScores_btn = self.AddButton(
            4, 1, self.StartMenu_fr, "High Scores")
        self.HighScores_btn.config(command=lambda: self.HighScores())

        self.Start_btn = self.AddPositive_btn(4, 2, self.StartMenu_fr, "Start")
        self.Start_btn.config(command=lambda: self.StartGame())

        self.Username_ent.bind("<Return>", lambda e: self.StartGame())

        self.Align_Grid(self.StartMenu_fr)

    def HighScores(self):
        import sqlite3 as lite

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("CREATE TABLE MasterMind(Username, Score)")
            except:
                try:
                    self.Cur.execute(
                        "SELECT Username FROM MasterMind ORDER BY Score;")

                    self.HighScoresUser_list = []
                    for item in self.Cur.fetchall():
                        self.HighScoresUser_list.append(item[0])

                    self.Cur.execute(
                        "SELECT Score FROM MasterMind ORDER BY Score;")

                    self.HighScoresScore_list = []
                    for item in self.Cur.fetchall():
                        self.HighScoresScore_list.append(item[0])
                except:
                    self.HighScoresUser_list = [None]
                    self.HighScoresScore_list = [None]
                pass

        self.StartMenu_fr.destroy()
        self.HighScores_fr = self.AddFrame()

        self.Title_lbl = self.AddTitle_lbl(
            0, 0, self.HighScores_fr, "High Scores", CSpan=2)
        self.Space_lbl = self.AddSpace_lbl(1, 0, self.HighScores_fr, CSpan=2)
        self.Space_lbl.config(text="A lower score is better!")

        for i in range(len(self.HighScoresUser_list)):
            self.Name_lbl = self.AddLabel(
                i+2, 0, self.HighScores_fr, self.HighScoresUser_list[i])

        for i in range(len(self.HighScoresScore_list)):
            self.Score = self.AddLabel(
                i+2, 1, self.HighScores_fr, self.HighScoresScore_list[i])
            self.EndRow = i+3

        self.Back_btn = self.AddButton(
            self.EndRow, 0, self.HighScores_fr, "Back", CSpan=2)
        self.Back_btn.config(
            command=lambda: [self.StartMenu(), self.HighScores_fr.destroy()])

        self.Align_Grid(self.HighScores_fr)

        return

    def StartGame(self):
        import tkinter as TK

        self.Username = self.Username_ent.get()
        if not self.Username:
            self.Space_lbl.config(text="You didn't enter a username")
            return

        self.StartMenu_fr.destroy()

        self.Guess_tl = TK.Toplevel(bg=self.Background)

        self.GTitle_lbl = self.AddTitle_lbl(0, 0, self.Guess_tl, "Guess")

        self.WhitePinsTitle_lbl = self.AddTitle_lbl(
            0, 1, self.Guess_tl, "White")

        self.BlackPinsTitle_lbl = self.AddTitle_lbl(
            0, 2, self.Guess_tl, "Black")

        self.GSpace_lbl = self.AddSpace_lbl(1, 0, self.Guess_tl, CSpan=3)

        self.UserGuess_list = []
        self.UserWhites_list = []
        self.UserBlacks_list = []

        self.Align_Grid(self.Guess_tl)

        from random import choice
        self.Colours = ["red", "yellow", "green", "blue", "black", "white"]
        self.RandomColours = []

        for _i in range(4):
            self.Colour = choice(self.Colours)
            self.RandomColours.append(self.Colour)

            self.Colours.remove(self.Colour)

        self.Colours = ["red", "yellow", "green", "blue", "black", "white"]

        self.Game_fr = self.AddFrame()

        self.StrVar_list = []

        self.Title_lbl = self.AddTitle_lbl(
            0, 0, self.Game_fr, "Guess...", CSpan=2)

        self.Space_lbl = self.AddSpace_lbl(1, 0, self.Game_fr, CSpan=2)

        self.Play_fr = self.AddFrame(
            Row=2, Column=0, Pack=False, Frame=self.Game_fr, CSpan=2)

        for _i in range(4):
            self.Str_var = TK.StringVar(self.Play_fr)
            self.Str_var.set(self.Colours[0])

            self.StrVar_list.append(self.Str_var)

        for i in range(4):
            Colour_dd = TK.OptionMenu(
                self.Play_fr, self.StrVar_list[i], *self.Colours)

            Colour_dd.config(bg=self.Background, activebackground=self.Background,
                             font=self.Font, foreground=self.Foreground)

            Colour_dd["menu"].config(
                bg=self.Background, activebackground=self.Background, font=self.Font, foreground=self.Foreground)

            Colour_dd["highlightthickness"] = 0

            Colour_dd.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

        self.GiveUp_btn = self.AddButton(
            1, 0, self.Play_fr, "Give Up", CSpan=2)

        self.GiveUp_btn.config(command=lambda: self.GiveUp())

        self.Guess_btn = self.AddPositive_btn(
            1, 2, self.Play_fr, "Guess", CSpan=3)
        self.Guess_btn.config(command=lambda: self.Guess())

        self.Align_Grid(self.Game_fr)
        self.Align_Grid(self.Play_fr)

    def GiveUp(self):
        self.Space_lbl.config(text=", ".join(self.RandomColours))

        self.Play_fr.destroy()
        self.Guess_tl.destroy()

        self.Back_btn = self.AddButton(3, 0, self.Game_fr, "Menu")
        self.Back_btn.config(
            command=lambda: [self.Game_fr.destroy(), self.StartMenu()])

        self.Quit_btn = self.AddQuit_btn(3, 1, self.Game_fr)

        return

    def Guess(self):

        self.UserGuess = []
        for item in self.StrVar_list:
            self.UserGuess.append(item.get())

        self.Items = []

        self.BlackPins = 0
        self.WhitePins = 0
        for i in range(len(self.UserGuess)):
            if self.UserGuess[i] == self.RandomColours[i]:
                self.BlackPins += 1
            elif self.UserGuess[i] in self.Items:
                continue
            elif self.UserGuess[i] in self.RandomColours:
                self.WhitePins += 1

            self.Items.append(self.UserGuess[i])

        self.UserGuess_list.append(self.UserGuess)
        self.UserBlacks_list.append(self.BlackPins)
        self.UserWhites_list.append(self.WhitePins)

        self.GuessBoard()

        return

    def GuessBoard(self):
        for i in range(len(self.UserGuess_list)):
            self.AddLabel(i+4, 0, self.Guess_tl,
                          ", ".join(self.UserGuess_list[i]))
            self.AddLabel(i+4, 1, self.Guess_tl,
                          self.UserWhites_list[i])
            self.AddLabel(i+4, 2, self.Guess_tl,
                          self.UserBlacks_list[i])

        self.Align_Grid(self.Guess_tl)
        if self.BlackPins == 4:
            self.Win()

        return

    def Win(self):
        self.Score = len(self.UserGuess_list)
        self.Guess_tl.destroy()

        self.Game_fr.destroy()

        self.Win_fr = self.AddFrame()

        self.Title_lbl = self.AddTitle_lbl(
            0, 0, self.Win_fr, "You Win!", CSpan=2)

        self.Score_lbl = self.AddLabel(
            1, 0, self.Win_fr, "Score: {}".format(self.Score), CSpan=2)

        self.Space_lbl = self.AddSpace_lbl(2, 0, self.Win_fr, CSpan=2)

        self.Back_btn = self.AddButton(3, 0, self.Win_fr, "Menu")
        self.Back_btn.config(
            command=lambda: [self.Win_fr.destroy(), self.StartMenu()])

        self.Quit_btn = self.AddQuit_btn(3, 1, self.Win_fr)

        self.Align_Grid(self.Win_fr)

        import sqlite3 as lite
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("CREATE TABLE MasterMind(Username, Score)")
            except:
                pass
            try:
                self.Cur.execute(
                    "INSERT INTO MasterMind VALUES(?, ?)", (self.Username, self.Score))
            except Exception as Idenifier:
                print(Idenifier)

        return

    def Quit(self):
        self.root.destroy()

    # Allows for the grids to expand with the root window
    def Align_Grid(self, Frame):
        # Gets the nuber of rows and columns of the grid
        self.Grid_Size = Frame.grid_size()

        # Loops through every column
        for i in range(self.Grid_Size[0]):
            # Sets the weight to a non zero value so it can expand
            Frame.columnconfigure(i, weight=1)
        # Loops through every row
        for i in range(self.Grid_Size[1]):
            # Sets the weight to a non zero value so it can expand
            Frame.rowconfigure(i, weight=1)

    '''
    These will simplify the GUI code and help to remove most of the rpetition in it
    '''

    # Will add a frame to a set row or automatically pack it into the main_fr
    def AddFrame(self, Row=None, Column=None, Pack=True, Frame=None, CSpan=1, RSpan=1):
        import tkinter as TK
        if not Frame:
            Frame = self.Main_fr
        Name = TK.Frame(Frame, bg=self.Background)
        if Pack:
            Name.pack(fill=TK.BOTH, expand=True)
        else:
            Name.grid(row=Row, column=Column,
                      padx=2, pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Name

    def AddSpace_lbl(self, Row, Column, Frame, CSpan=1, RSpan=1):
        import tkinter as TK
        Space_lbl = TK.Label(
            Frame, bg=self.Background, font=self.Font, foreground=self.Foreground)
        Space_lbl.grid(row=Row, column=Column, padx=2,
                       pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Space_lbl

    def AddLabel(self, Row, Column, Frame, Text, CSpan=1, RSpan=1):
        import tkinter as TK
        Label = TK.Label(
            Frame, bg=self.Background, font=self.Font, foreground=self.Foreground, text=Text)
        Label.grid(row=Row, column=Column, padx=2,
                   pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Label

    def AddTitle_lbl(self, Row, Column, Frame, Title, CSpan=1, RSpan=1):
        import tkinter as TK
        Title_lbl = TK.Label(
            Frame, bg=self.Background, font=self.TitleFont, foreground=self.Foreground, text=Title)
        Title_lbl.grid(row=Row, column=Column, padx=2,
                       pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Title_lbl

    def AddButton(self, Row, Column, Frame, Text, CSpan=1, RSpan=1):
        import tkinter as TK
        '''
        You must add your own command using the .config method
        '''
        Button = TK.Button(Frame, bg=self.Btn_Background, activebackground=self.Btn_Active,
                           foreground=self.Foreground, font=self.Font, text=Text)
        Button.grid(row=Row, column=Column, padx=2,
                    pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Button

    def AddQuit_btn(self, Row, Column, Frame, CSpan=1, RSpan=1):
        import tkinter as TK

        Quit_btn = TK.Button(Frame, bg=self.QuitBtn_Background, activebackground=self.QuitBtn_Active,
                             foreground=self.Foreground, font=self.Font, text="Quit", command=lambda: self.Quit())
        Quit_btn.grid(row=Row, column=Column, padx=2,
                      pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Quit_btn

    def AddPositive_btn(self, Row, Column, Frame, Text, CSpan=1, RSpan=1):
        '''
        You must add your own command using the .config method
        '''
        import tkinter as TK
        Button = TK.Button(Frame, bg=self.PositiveBtn_Background, activebackground=self.PositiveBtn_Active,
                           foreground=self.Foreground, font=self.Font, text=Text)
        Button.grid(row=Row, column=Column, padx=2,
                    pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Button

    def AddEntry(self, Frame, Row, Column, CSpan=1, Focus=False, Show="", RSpan=1):
        import tkinter as TK
        Entry = TK.Entry(
            Frame, font=self.Font, foreground=self.Foreground)

        if Show:
            Entry.config(show=Show)
        Entry.grid(row=Row, column=Column, sticky="nsew",
                   padx=2, pady=2, columnspan=CSpan)
        if Focus:
            Entry.focus()

        Entry.grid(row=Row, column=Column, padx=2, pady=2,
                   sticky="nsew", columnspan=CSpan, rowspan=RSpan)
        return Entry

    def AddNegetive_btn(self, Frame, Row, Column, Text, CSpan=1, RSpan=1):
        '''
        You must add your own command using the .config method
        '''
        import tkinter as TK
        Button = TK.Button(Frame, bg=self.QuitBtn_Background, activebackground=self.QuitBtn_Active,
                           foreground=self.Foreground, font=self.Font, text=Text)
        Button.grid(row=Row, column=Column, padx=2,
                    pady=2, sticky="nsew", columnspan=CSpan, rowspan=RSpan)

        return Button


def Run(Customisations={}):
    import tkinter as TK

    root = TK.Tk()

    Main(root, Customisations)

    while True:
        try:
            root.update()
            root.update_idletasks()
        except:
            break

    return


if __name__ == "__main__":
    import tkinter as TK

    Defults = {
        "Background": "#7eccf7",
        "Foreground": "Black",
        "Btn_Background": "#2db4ff",
        "Btn_Active": "#2da9ff",
        "QuitBtn_Background": "#ef2804",
        "QuitBtn_Active": "#f52804",
        "PositiveBtn_Background": "#1ece18",
        "PositiveBtn_Active": "#159b11",
        "Font": ("Arial", 14),
        "TitleFont": ("Arial", 18, "bold"),
        "SubTitleFont": ("Arial", 14, "bold"),
    }

    root = TK.Tk()

    Main(root, Defults)

    while True:
        try:
            root.update()
            root.update_idletasks()
        except:
            break

    raise SystemExit
