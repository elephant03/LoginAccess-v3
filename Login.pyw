'''
This file creats the main login system
'''

'''
Importing the needed moduals
'''
#imports the tkinter libary for the GUI
import tkinter as TK
#Imports the SQL libary for handeling the database
import sqlite3 as lite

#Imports my hashing system
#Wirten out weird as the normal way wouldn't work with the subdictionaries so this way instead
import os
import sys
filename = "Moduals/Utilities/Hash.py"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    Hash = __import__(module_name)
finally:
    sys.path[:] = path # restore

#Imports email server for password resets
filename = "Moduals/Utilities/Email.py"

directory, module_name = os.path.split(filename)
module_name = os.path.splitext(module_name)[0]

path = list(sys.path)
sys.path.insert(0, directory)
try:
    Email = __import__(module_name)
finally:
    sys.path[:] = path # restore


class Main():
    '''
    The main login class containing all needed methods for the longin system
    '''
    #Sets the defult colours and fonts so that each user can constomise it without effecting other users
    Defults = {
        "Background": "#7eccf7",
        "Foreground": "Black",
        "Btn_Background": "#2db4ff",
        "Btn_Active": "#2da9ff",
        "QuitBtn_Background": "#ef2804",
        "QuitBtn_Active": "#f52804",
        "PositiveBtn_Background": "#1ece18",
        "PositiveBtn_Active": "#159b11",
        "Font": ("Arial",14),
        "TitleFont": ("Arial",18,"bold"),
        "SubTitleFont": ("Arial", 14, "bold"),
    }
    
    #Puts the defults into readable varable that can change based off user preferences
    def SetDefults(self, Update = True):
        self.Background = self.Defults["Background"]
        self.Foreground = self.Defults["Foreground"]
        self.Btn_Background = self.Defults["Btn_Background"]
        self.Btn_Active = self.Defults["Btn_Active"]
        self.QuitBtn_Background = self.Defults["QuitBtn_Background"]
        self.QuitBtn_Active = self.Defults["QuitBtn_Active"]
        self.PositiveBtn_Background = self.Defults["PositiveBtn_Background"]
        self.PositiveBtn_Active = self.Defults["PositiveBtn_Active"]
        self.Font = self.Defults["Font"]
        self.TitleFont = self.Defults["TitleFont"]
        self.SubTitleFont = self.Defults["SubTitleFont"]

        #Updates all currently loard widgets to the new defaults
        self.UpdateState_Background(self.Main_fr)
        self.UpdateState_Btn_Active(self.Main_fr)
        self.UpdateState_Btn_Background(self.Main_fr)
        self.UpdateState_Font(self.Main_fr)
        self.UpdateState_Foreground(self.Main_fr)
        self.UpdateState_PositiveBtn_Active(self.Main_fr)
        self.UpdateState_PositiveBtn_Background(self.Main_fr)
        self.UpdateState_QuitBtn_Active(self.Main_fr)
        self.UpdateState_QuitBtn_Background(self.Main_fr)
        self.UpdateState_SubTitleFont(self.Main_fr)
        self.UpdateState_TitleFont(self.Main_fr)


        #If it has been changed (updated) by the user it will go back to the customisation frame
        if Update:
            self.Back(self.Customisation_fr, 2)

    '''
    These allow for the defult colours to change and for all needed widgets to update themselves
    Only the first will have comments as the rest are the same but effective a different varable
    '''
    #Updates the background colour
    def UpdateState_Background(self, Frame):
        #Updates the givens frame background

        try:
            Frame.config(bg = self.Background)

           #Finds all of the frames sub(child) widgets
            for associated_widget in Frame.winfo_children():
                #for everyone resets the background colour
                associated_widget.config(bg = self.Background)
            return
        except Exception:
            pass

    def UpdateState_Foreground(self, Frame):
        try:
            Frame.config(bg = self.Foreground)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.Foreground)
            return
        except Exception:
            pass

    def UpdateState_Btn_Background(self, Frame):
        try:
            Frame.config(bg = self.Btn_Background)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.Btn_Background)
            return
        except Exception:
            pass

    def UpdateState_Btn_Active(self, Frame):
        try:
            Frame.config(bg = self.Btn_Active)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.Btn_Active)
            return
        except Exception:
            pass

    def UpdateState_QuitBtn_Background(self, Frame):
        try:
            Frame.config(bg = self.QuitBtn_Background)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.QuitBtn_Background)
            return
        except Exception:
            pass

    def UpdateState_QuitBtn_Active(self, Frame):
        try:
            Frame.config(bg = self.QuitBtn_Active)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.QuitBtn_Active)
            return
        except Exception:
            pass

    def UpdateState_PositiveBtn_Background(self, Frame):
        try:
            Frame.config(bg = self.PositiveBtn_Background)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.PositiveBtn_Background)
            return
        except Exception:
            pass

    def UpdateState_PositiveBtn_Active(self, Frame):
        try:
            Frame.config(bg = self.PositiveBtn_Active)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.PositiveBtn_Active)
            return
        except Exception:
            pass

    def UpdateState_Font(self, Frame):
        try:
            Frame.config(bg = self.Font)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.Font)
            return
        except Exception:
            pass

    def UpdateState_TitleFont(self, Frame):
        try:
            Frame.config(bg = self.TitleFont)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.TitleFont)
            return
        except Exception:
            pass
    
    def UpdateState_SubTitleFont(self, Frame):
        try:
            Frame.config(bg = self.SubTitleFont)
            for associated_widget in Frame.winfo_children():
                associated_widget.config(bg = self.SubTitleFont)
            return
        except Exception:
            pass
    #Finally they are over

    '''
    Loads the main menu screen for when the user has successfuly loged in
    '''
    def MainMenu(self):
        self.Login_fr.destroy()

        self.MainMenu_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.MainMenu_fr.pack(fill = TK.BOTH, expand = True)


        self.Title_lbl = TK.Label(self.MainMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Main Menu...")
        self.Title_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = 2)

        self.Settings_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Settings", command = lambda: self.Settings())
        self.Settings_btn.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Help_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "?", command = lambda: self.MainMenu_Help())
        self.Help_btn.grid(row = 0, column = 2, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.MainMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew", padx = 2, pady = 2)

        #Connects to my database
        with lite.connect("myDatabase.db") as self.Con:
            #creats a curser object to interact with the database
            self.Cur = self.Con.cursor()

            #Since I am bad at writting these in a try statment for debugging
            try:
                self.Cur.execute("SELECT Warnings FROM Users WHERE Username = ?", ((self.Username, )))
                self.Warnings = self.Cur.fetchall()[0][0]
            except Exception:
                pass
        
        try:

            if int(self.Warnings) > 0:
                self.Space_lbl.config(text = "You have: {Num} Warnings".format(Num = self.Warnings))
        
        
            if int(self.Warnings) >= 3:
                self.Warnings_lbl = TK.Label(self.MainMenu_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "You has reached three warnings\nYour account will now be deleted for these violations")
                self.Warnings_lbl.grid(row = 2, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

                self.OK_btn = TK.Button(self.MainMenu_fr, command = lambda: self.DeleteAccount(self.MainMenu_fr), bg = self.Btn_Background,activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Continue")
                self.OK_btn.grid(row = 3, column = 0, padx = 2, pady = 2, columnspan = 3, sticky = "nsew")

                return
        
        except TypeError:
            #A type error could be raised due to the value of it being null in admin and owner accounts
            pass

        self.Tools_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, foreground = self.Foreground, activebackground = self.Btn_Active, font = self.Font, text = "Tools", command = lambda: self.ToolsMenu())
        self.Tools_btn.grid(row = 2, column = 0, columnspan = 3, padx = 2, pady = 2, sticky = "nsew")

        self.Games_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, foreground = self.Foreground, activebackground = self.Btn_Active, font = self.Font, text = "Games", command = lambda: self.GamesMenu())
        self.Games_btn.grid(row = 3, column = 0, columnspan = 3, padx = 2, pady = 2, sticky = "nsew")
        
        self.Message_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, foreground = self.Foreground, activebackground = self.Btn_Active, font = self.Font, text = "View Messages", command = lambda: self.Messages())
        self.Message_btn.grid(row = 4, column = 0, columnspan = 3, padx = 2, pady = 2, sticky = "nsew")

        
        #Connects to the main database
        with lite.connect("myDatabase.db") as self.Con:
            #creats a curser object to interact with the database
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT AccountType FROM Users WHERE Username = ?", ((self.Username,)))

                self.AccountType = self.Cur.fetchall()[0][0]
            except Exception:
                pass

        #Allows for different levels of authentication between users
        
        if self.AccountType == "admin" or self.AccountType == "owner":
            self.AdminMenu_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Admin Menu", command = lambda: self.AdminMenu())
            self.AdminMenu_btn.grid(row = 5, column = 0, columnspan = 3, padx = 2, pady = 2, sticky = "nsew")

        if self.AccountType == "owner":
            self.OwnerMenu_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Owner Menu", command = lambda: self.OwnerMenu())
            self.OwnerMenu_btn.grid(row = 6, column = 0, columnspan = 3, padx = 2, pady = 2, sticky = "nsew")

        
        self.QUIT_btn = TK.Button(self.MainMenu_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, foreground = self.Foreground, font = self.Font, text = "Quit", command = lambda: self.Quit())
        self.QUIT_btn.grid(row = 7, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Logout_btn = TK.Button(self.MainMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Logout", command = lambda: self.Back(self.MainMenu_fr, 0))
        self.Logout_btn.grid(row = 7 ,column = 1, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")


        self.Align_Grid(self.MainMenu_fr)

    '''
    Displays access to all of the different personal settings
    '''
    def Settings(self):
        self.MainMenu_fr.destroy()
        
        self.Settings_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.Settings_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.Settings_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Settings:")
        self.Title_lbl.grid(row = 0, column = 0, pady = 2, padx = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.Settings_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Customisation_btn = TK.Button(self.Settings_fr, bg = self.Btn_Background, foreground = self.Foreground, font = self.Font, text = "Customisation", activebackground = self.Btn_Active, command = lambda: self.Customisation())
        self.Customisation_btn.grid(row = 2, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Account_btn = TK.Button(self.Settings_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Account", command = lambda: self.AccountSettings())
        self.Account_btn.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.ReportBug_btn = TK.Button(self.Settings_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Report Bug", command = lambda: self.BugReport())
        self.ReportBug_btn.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = "nsew")
        
        self.Other_btn = TK.Button(self.Settings_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Other", command = lambda: self.OtherSettings())
        self.Other_btn.grid(row = 5, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl1 = TK.Label(self.Settings_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 6, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Back_btn = TK.Button(self.Settings_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.Settings_fr, 1))
        self.Back_btn.grid(row = 7, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.Settings_fr)

    '''
    All of the setting sub menus
    '''
    
    #Allows a user to report any bugs they find
    def BugReport(self):
        self.Settings_fr.destroy()
        self.BugReport_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.BugReport_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.BugReport_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Bug Reporter:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.Space_lbl = TK.Label(self.BugReport_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Bug_lbl = TK.Label(self.BugReport_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Bug details:")
        self.Bug_lbl.grid(row = 2, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Bug_ent = TK.Entry(self.BugReport_fr, foreground = self.Foreground, font = self.Font)
        self.Bug_ent.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl1 = TK.Label(self.BugReport_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Back_btn = TK.Button(self.BugReport_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.BugReport_fr, 2))
        self.Back_btn.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Report_btn = TK.Button(self.BugReport_fr, bg = self.PositiveBtn_Background, activebackground = self.PositiveBtn_Active, foreground = self.Foreground, font = self.Font, command = lambda: self.ReportBug(), text = "Report Bug")
        self.Report_btn.grid(row = 4, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Bug_ent.bind("<Return>", lambda e: self.ReportBug())

        self.Align_Grid(self.BugReport_fr)

    #Will place the bug report into the database
    def ReportBug(self):
        self.Bug = str(self.Bug_ent.get())

        if self.Bug == "":
            self.Space_lbl.config(text = "Sorry- you didn't leave any details about the bug")
            return

        
        #Connects to my main database
        with lite.connect("myDatabase.db") as self.Con:
            #creats a curser object to interact with the database
            self.Cur = self.Con.cursor()

            #Attempt to make a bugs table in the database
            try:
                self.Columns = [
                    "Username",
                    "BugDetails",
                    "Status",
                ]
                self.Cur.execute("CREATE TABLE Bugs(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)")#Creates the table
                for i in range(len(self.Columns)):#Adds the kwargs to the table
                    self.Cur.execute("ALTER TABLE Bugs ADD COLUMN {ColumnName} TEXT".format(ColumnName = str(self.Columns[i]), ))
                pass
            except Exception:#If the databse or table already exist it will exit
                pass

            #Adds the bug into the bugs table
            try:
                self.Cur.execute("INSERT INTO Bugs(Username, BugDetails) VALUES(?, ?)", (self.Username, self.Bug))
            except Exception:
                pass
        
        self.Back(self.BugReport_fr, 2)

    #Allows for a customied look of the program for the users current sesson
    #IMPROVMENT
    #DOESN'T EXSTEND INTO SUB-AREAS E.G. GAMES ETC. (yet...)
    #FORGOTEN IF THE USER LOGS OUT (at the moment)
    def Customisation(self):
        
        self.Settings_fr.destroy()
        self.Customisation_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.Customisation_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.Customisation_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Other:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.Space_lbl = TK.Label(self.Customisation_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.CustomisationLables_list =[]
        self.Counter = 2
        self.TypeOrder_list = []

        for i in self.Defults:
            self.TypeOrder_list.append(i)
            self.Customisation_lbl = TK.Label(self.Customisation_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = i)
            self.Customisation_lbl.grid(row = self.Counter, column = 0, padx = 2, pady = 2, sticky = "nsew")
            self.CustomisationLables_list.append(self.Customisation_lbl)
            self.Counter += 1
        
        self.CustomisationEntry_list =[]
        self.Counter = 2

        for i in self.Defults:
            self.Customisation_ent = TK.Entry(self.Customisation_fr, foreground = self.Foreground, font = self.Font)
            self.Customisation_ent.grid(row = self.Counter, column = 1, padx = 2, pady = 2, sticky = "nsew")
            self.CustomisationEntry_list.append(self.Customisation_ent)
            self.Counter += 1

        self.Space_lbl1 = TK.Label(self.Customisation_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 13, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.ResetDefults_btn = TK.Button(self.Customisation_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Restore Defults", command = lambda: self.SetDefults())
        self.ResetDefults_btn.grid(row = 14, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)


        self.Back_btn = TK.Button(self.Customisation_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.Customisation_fr, 2))
        self.Back_btn.grid(row = 15, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Save_btn = TK.Button(self.Customisation_fr, bg = self.PositiveBtn_Background, foreground = self.Foreground, font = self.Font, activebackground = self.PositiveBtn_Active, text = "Save Changes", command = lambda: self.SaveChanges_Customisation())
        self.Save_btn.grid(row = 15, column = 1, padx = 2, pady = 2, sticky = "nsew")

        for i in self.CustomisationEntry_list:
            i.bind("<Return>", lambda e: self.SaveChanges_Customisation())

        self.Align_Grid(self.Customisation_fr)

    def SaveChanges_Customisation(self):
        print(self.TypeOrder_list)

        if self.CustomisationEntry_list[self.TypeOrder_list.index("Background")].get() != "":
            self.Background = self.CustomisationEntry_list[self.TypeOrder_list.index("Background")].get()
            self.UpdateState_Background(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("Foreground")].get() != "":
            self.Foreground = self.CustomisationEntry_list[self.TypeOrder_list.index("Foreground")].get()
            self.UpdateState_Foreground(self.Customisation_fr)

        if self.CustomisationEntry_list[self.TypeOrder_list.index("Btn_Background")].get() != "":
            self.Btn_Background = self.CustomisationEntry_list[self.TypeOrder_list.index("Btn_Background")].get()
            self.UpdateState_Btn_Background(self.Customisation_fr)

        if self.CustomisationEntry_list[self.TypeOrder_list.index("Btn_Active")].get() != "":
            self.Btn_Active = self.CustomisationEntry_list[self.TypeOrder_list.index("Btn_Active")].get()
            self.UpdateState_Btn_Active(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("QuitBtn_Background")].get() != "":
            self.QuitBtn_Background = self.CustomisationEntry_list[self.TypeOrder_list.index("QuitBtn_Background")].get()
            self.UpdateState_QuitBtn_Background(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("QuitBtn_Active")].get() != "":
            self.QuitBtn_Active = self.CustomisationEntry_list[self.TypeOrder_list.index("QuitBtn_Active")].get()
            self.UpdateState_QuitBtn_Active(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("PositiveBtn_Background")].get() != "":
            self.PositiveBtn_Background = self.CustomisationEntry_list[self.TypeOrder_list.index("PositiveBtn_Background")].get()
            self.UpdateState_PositiveBtn_Background(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("PositiveBtn_Active")].get() != "":
            self.PositiveBtn_Active = self.CustomisationEntry_list[self.TypeOrder_list.index("PositiveBtn_Active")].get()
            self.UpdateState_PositiveBtn_Active(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("Font")].get() != "":
            self.Font = self.CustomisationEntry_list[self.TypeOrder_list.index("Font")].get()
            self.UpdateState_Font(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("TitleFont")].get() != "":
            self.TitleFont = self.CustomisationEntry_list[self.TypeOrder_list.index("TitleFont")].get()
            self.UpdateState_TitleFont(self.Customisation_fr)
        
        if self.CustomisationEntry_list[self.TypeOrder_list.index("SubTitleFont")].get() != "":
            self.SubTitleFont = self.CustomisationEntry_list[self.TypeOrder_list.index("SubTitleFont")].get()
            self.UpdateState_SubTitleFont(self.Customisation_fr)

        self.Back(self.Customisation_fr, 2)
    
    def AccountSettings(self):
        
        self.Settings_fr.destroy()
        self.Account_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.Account_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.Account_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Account Settings:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.Account_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.ChangeUsername_btn = TK.Button(self.Account_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Change Username", command = lambda: self.ChangeUsername())
        self.ChangeUsername_btn.grid(row = 2, column = 0, pady = 2, padx = 2, sticky = "nsew")

        self.ChangePassword_btn = TK.Button(self.Account_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Change Password", command = lambda: self.ChangePassword())
        self.ChangePassword_btn.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.AddEmail_btn = TK.Button(self.Account_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Add/Change Email", command = lambda: self.AddChangeEmail())
        self.AddEmail_btn.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.DeleteAccount_btn = TK.Button(self.Account_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, foreground = self.Foreground, font = self.Font, text = "Delete Account", command = lambda: self.DeleteAccount(self.Account_fr))
        self.DeleteAccount_btn.grid(row = 5, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Space_lbl1 = TK.Label(self.Account_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 6, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Back_btn = TK.Button(self.Account_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.Account_fr, 2))
        self.Back_btn.grid(row = 7, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.Account_fr)
    
    def DeleteAccount(self, Frame):
        
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("DELETE FROM Users WHERE Username = ?", (self.Username,))
            except Exception:
                pass

        
        self.Back(Frame, 0)

    def ChangeUsername(self):

        self.Account_fr.destroy()
        self.ChangeUsername_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.ChangeUsername_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.ChangeUsername_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Change Username:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.Space_lbl = TK.Label(self.ChangeUsername_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.ChangeUsername_lbl = TK.Label(self.ChangeUsername_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "New Username:")
        self.ChangeUsername_lbl.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.ChangeUsername_ent = TK.Entry(self.ChangeUsername_fr, foreground = self.Foreground, font = self.Font)
        self.ChangeUsername_ent.grid(row = 2, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Space_lbl1 = TK.Label(self.ChangeUsername_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Back_btn = TK.Button(self.ChangeUsername_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.ChangeUsername_fr, 3))
        self.Back_btn.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Save_btn = TK.Button(self.ChangeUsername_fr, bg = self.PositiveBtn_Background, foreground = self.Foreground, font = self.Font, activebackground = self.PositiveBtn_Active, text = "Save Changes", command = lambda: self.SaveChanges_Username())
        self.Save_btn.grid(row = 4, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.ChangeUsername_ent.bind("<Return>", lambda e: self.SaveChanges_Username())

        self.Align_Grid(self.ChangeUsername_fr)
        
    
    def SaveChanges_Username(self):
        self.NewUsername = Hash.Hash(str(self.ChangeUsername_ent.get()))

        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            
            try:
                #Tests if the username already exists in the database
                self.Cur.execute("SELECT EXISTS (SELECT * FROM Users WHERE Username = ?)", ((self.NewUsername,)))
                for i in self.Cur:
                    for n in i:
                        if n == 1:#0 meand the username isn't there 1 means it already exists
                            #If the username already exists it will tell the userr and clear their inputs
                            self.Space_lbl.config(text = "Sorry this username is already taken")
                            self.ChangeUsername_ent.focus()
                            self.ChangeUsername_ent.delete(0, 'end')
                            return
                        else:
                            pass
                self.Cur.execute("UPDATE Users SET Username = ? WHERE Username = ?", (self.NewUsername, self.Username))
            except Exception:
                pass

        self.Back(self.ChangeUsername_fr, 1)

    def ChangePassword(self):
        
        self.Account_fr.destroy()
        self.ChangePassword_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.ChangePassword_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.ChangePassword_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Change Password:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.Space_lbl = TK.Label(self.ChangePassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.OldPassword_lbl = TK.Label(self.ChangePassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Old Password:")
        self.OldPassword_lbl.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.OldPassword_ent = TK.Entry(self.ChangePassword_fr, foreground = self.Foreground, font = self.Font, show = "•")
        self.OldPassword_ent.grid(row = 2, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.ChangePassword_lbl = TK.Label(self.ChangePassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "New Password:")
        self.ChangePassword_lbl.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.ChangePassword_ent = TK.Entry(self.ChangePassword_fr, foreground = self.Foreground, font = self.Font, show = "•")
        self.ChangePassword_ent.grid(row = 3, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.RepeatChangePassword_lbl = TK.Label(self.ChangePassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Repeat Password:")
        self.RepeatChangePassword_lbl.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.RepeatChangePassword_ent = TK.Entry(self.ChangePassword_fr, foreground = self.Foreground, font = self.Font, show = "•")
        self.RepeatChangePassword_ent.grid(row = 4, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Space_lbl1 = TK.Label(self.ChangePassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 5, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Back_btn = TK.Button(self.ChangePassword_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.ChangePassword_fr, 3))
        self.Back_btn.grid(row = 6, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Save_btn = TK.Button(self.ChangePassword_fr, bg = self.PositiveBtn_Background, foreground = self.Foreground, font = self.Font, activebackground = self.PositiveBtn_Active, text = "Save Changes", command = lambda: self.SaveChanges_Password())
        self.Save_btn.grid(row = 6, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.RepeatChangePassword_ent.bind("<Return>", lambda e: self.SaveChanges_Password())
        self.ChangePassword_ent.bind("<Return>", lambda e: self.SaveChanges_Password())
        self.OldPassword_ent.bind("<Return>", lambda e: self.SaveChanges_Password())

        self.Align_Grid(self.ChangePassword_fr)
        
    
    def SaveChanges_Password(self):
        self.NewPassword = Hash.Hash(str(self.ChangePassword_ent.get()))
        self.RepeatPassword = Hash.Hash(str(self.RepeatChangePassword_ent.get()))
        self.OldPassword = Hash.Hash(str(self.OldPassword_ent.get()))

        if self.NewPassword != self.RepeatPassword:
            self.Space_lbl.congfig(text = "The passwords didn't match")
            self.ChangePassword_ent.delete(0, 'end')
            self.OldPassword_ent.delete(0, "end")
            self.RepeatChangePassword_ent.delete(0, "end")
            return


        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            
            try:
                self.Cur.execute("SELECT Password FROM Users WHERE Username = ?", (self.Username,))

                self.UserPassword = self.Cur.fetchall()[0][0]

                if self.UserPassword == self.OldPassword:

                    self.Cur.execute("UPDATE Users SET Password = ? WHERE Username = ?", (self.NewPassword, self.Username))
                else:
                    self.Space_lbl.congfig(text = "This isn't the correct old password")
                    self.ChangePassword_ent.delete(0, 'end')
                    self.OldPassword_ent.delete(0, "end")
                    self.RepeatChangePassword_ent.delete(0, "end")
                    return

            except Exception:
                pass

        self.Back(self.ChangePassword_fr, 1)
    
    def AddChangeEmail(self):
                
        self.Account_fr.destroy()
        self.AddEmail_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.AddEmail_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.AddEmail_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Add/Change Email:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.Space_lbl = TK.Label(self.AddEmail_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.AddEmail_lbl = TK.Label(self.AddEmail_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "New Email:")
        self.AddEmail_lbl.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.AddEmail_ent = TK.Entry(self.AddEmail_fr, foreground = self.Foreground, font = self.Font)
        self.AddEmail_ent.grid(row = 2, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Space_lbl1 = TK.Label(self.AddEmail_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Back_btn = TK.Button(self.AddEmail_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.AddEmail_fr, 3))
        self.Back_btn.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Save_btn = TK.Button(self.AddEmail_fr, bg = self.PositiveBtn_Background, foreground = self.Foreground, font = self.Font, activebackground = self.PositiveBtn_Active, text = "Save Changes", command = lambda: self.SaveChanges_Email())
        self.Save_btn.grid(row = 4, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.AddEmail_ent.bind("<Return>", lambda e: self.SaveChanges_Email())

        self.Align_Grid(self.AddEmail_fr)
        
    
    def SaveChanges_Email(self):
        self.NewEmail = Hash.Hash(str(self.AddEmail_ent.get()))

        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            
            try:
                self.Cur.execute("UPDATE Users SET Email = ? WHERE Username = ?", (self.NewEmail, self.Username))
            except Exception:
                pass

        self.Back(self.AddEmail_fr, 1)
    
    def OtherSettings(self):

        self.Settings_fr.destroy()
        self.Other_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.Other_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.Other_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Other:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.Other_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Back_btn = TK.Button(self.Other_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.Other_fr, 2))
        self.Back_btn.grid(row = 2, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.Other_fr)
    
    def MainMenu_Help(self):
        self.Help_tl = TK.Toplevel()
        self.Help_tl.title("Help")
        self.Help_tl.config(bg= self.Background)

        self.ExplainationText = """I really cannot think why people will be confused here
        Um..  i guess i will think about it latter
        Cheese
        """

        self.Explaination_lbl = TK.Label(self.Help_tl, bg = self.Background, foreground = self.Foreground, font = self.Font, text = self.ExplainationText)
        self.Explaination_lbl.pack(fill = TK.BOTH, expand= True)

    def ToolsMenu(self):

        self.MainMenu_fr.destroy()
        self.ToolsMenu_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.ToolsMenu_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.ToolsMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Tools:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.ToolsMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Tools_list = []
        import glob

        self.Tools_File = __file__
        self.Tools_File = self.Tools_File[:-9]
        self.Tools_File += r"\Moduals\Tools\*.pyw"
        self.Tools_File.replace("\\", "\\\\")

        self.Files = glob.glob(self.Tools_File)

        self.EndRow_Value = 2

        for i in range(len(self.Files)):

            self.directory, self.module_name = os.path.split(self.Files[i])
            self.module_name = os.path.splitext(self.module_name)[0]

            self.path = list(sys.path)
            sys.path.insert(0, self.directory)
            try:
                Tool = __import__(self.module_name)
                self.Tools_list.append(Tool)
            finally:
                sys.path[:] = self.path # restore

            self.Tools_btn = TK.Button(self.ToolsMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = self.module_name, command = lambda Num = i: self.RunTool(Num))
            self.Tools_btn.grid(row = i+2, column = 0, pady = 2, padx = 2, sticky = "nsew")

            self.EndRow_Value += 1
        

        self.Space_lbl1 = TK.Label(self.ToolsMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = self.EndRow_Value, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Back_btn = TK.Button(self.ToolsMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.ToolsMenu_fr, 1))
        self.Back_btn.grid(row = self.EndRow_Value+1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.ToolsMenu_fr)

    def RunTool(self, Num):
        self.Tools_list[Num].Run()
    
    def GamesMenu(self):
        self.MainMenu_fr.destroy()
        self.GamesMenu_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.GamesMenu_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.GamesMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Games:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.GamesMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Games_list = []
        import glob

        self.Games_File = __file__
        self.Games_File = self.Games_File[:-9]
        self.Games_File += r"\Moduals\Games\*.pyw"
        self.Games_File.replace("\\", "\\\\")

        self.Files = glob.glob(self.Games_File)

        self.EndRow_Value = 2

        for i in range(len(self.Files)):

            self.directory, self.module_name = os.path.split(self.Files[i])
            self.module_name = os.path.splitext(self.module_name)[0]

            self.path = list(sys.path)
            sys.path.insert(0, self.directory)
            try:
                Game = __import__(self.module_name)
                self.Games_list.append(Game)
            finally:
                sys.path[:] = self.path # restore

            self.Tools_btn = TK.Button(self.GamesMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = self.module_name, command = lambda Num = i: self.RunGame(Num))
            self.Tools_btn.grid(row = i+2, column = 0, pady = 2, padx = 2, sticky = "nsew")

            self.EndRow_Value += 1
        

        self.Space_lbl1 = TK.Label(self.GamesMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = self.EndRow_Value, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Back_btn = TK.Button(self.GamesMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.GamesMenu_fr, 1))
        self.Back_btn.grid(row = self.EndRow_Value+1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.GamesMenu_fr)
    
    def RunGame(self, Num):
        self.Games_list[Num].Run()
    
    def Messages(self):
        self.MainMenu_fr.destroy()
        self.Messages_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.Messages_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.Messages_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Messages:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 3)

        self.Space_lbl = TK.Label(self.Messages_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 3)
        
        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT Messages FROM Users WHERE Username = ?", (self.Username,))
                for i in self.Cur:
                    for n in i:
                        self.Message_list = n.split(",")
            except Exception:
                self.Message_list = ["You have no messages!"]
        
        for i in self.Message_list:
            if i == "":
                self.Message_list.pop(self.Message_list.index(i))
        if not self.Message_list:
            self.Message_list = ["You have no messages!"]
        
        for i in range(len(self.Message_list)):
            
            self.IndividualMessage_fr = TK.Frame(self.Messages_fr, bg = self.Background)
            self.IndividualMessage_fr.grid(row = i+2, column = 0, columnspan = 2)

            self.Message_txt = TK.Text(self.IndividualMessage_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, height = 3, width = 25)
            self.Message_txt.grid(row = i, column = 0, pady = 2, sticky = "nsew", columnspan = 2)

            self.Message_txt.insert("end", "{Num}: {Message}".format(Num = i+1, Message = self.Message_list[i]))
            self.Message_txt.config(state = "disabled")

            self.ScrollBar = TK.Scrollbar(self.IndividualMessage_fr)
            self.ScrollBar.grid(row = i, column = 2, sticky = "nsew", pady = 2)

            self.ScrollBar.config(command = self.Message_txt.yview)
            self.Message_txt.config(yscrollcommand = self.ScrollBar.set)


            self.DeleteMessage_btn = TK.Button(self.Messages_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, foreground = self.Foreground, font = self.Font, text = "X", command = lambda Num = i: self.DeleteMessage(Num))
            self.DeleteMessage_btn.grid(row = i+2, column = 2, padx = 2, pady = 2, sticky = "nsew")

            if i == len(self.Message_list)-1:
                self.Space_lbl1 = TK.Label(self.Messages_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
                self.Space_lbl1.grid(row = i+3, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 3)

                self.Back_btn = TK.Button(self.Messages_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.Messages_fr, 1))
                self.Back_btn.grid(row = i+4, column = 0, sticky = "nsew", padx = 2, pady = 2)

                self.NewMessage_btn = TK.Button(self.Messages_fr, bg = self.PositiveBtn_Background, activebackground = self.PositiveBtn_Active, foreground = self.Foreground, font = self.Font, text = "New Message", command = lambda: self.NewMessage())
                self.NewMessage_btn.grid(row = i+4, column = 1, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Align_Grid(self.Messages_fr)

    def DeleteMessage(self, Num):
        self.Message_list.pop(Num)
        
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Message_list = ",".join(self.Message_list)
                self.Cur.execute("UPDATE Users SET Messages = ? WHERE Username = ?", (self.Message_list, self.Username))
            except Exception as Identifier:
                print(Identifier)
                pass
        self.Messages_fr.destroy()
        self.MainMenu_fr = TK.Frame(bg = self.Background)
        self.Messages()
    
    def NewMessage(self):
        self.Messages_fr.destroy()
        self.NewMessage_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.NewMessage_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.NewMessage_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Other:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.Space_lbl = TK.Label(self.NewMessage_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.SendTo_lbl = TK.Label(self.NewMessage_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Send To:")
        self.SendTo_lbl.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.SendTo_ent = TK.Entry(self.NewMessage_fr, foreground = self.Foreground, font = self.Font)
        self.SendTo_ent.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.Message_lbl = TK.Label(self.NewMessage_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Message:")
        self.Message_lbl.grid(row = 3, column = 0, pady = 2, sticky = "nsew")

        self.Message_txt = TK.Text(self.NewMessage_fr, font = self.Font, foreground = self.Foreground, height = 4, width = 20)
        self.Message_txt.grid(row = 3, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Message_sb = TK.Scrollbar(self.NewMessage_fr)
        self.Message_sb.grid(row = 3, column = 2, pady = 2, sticky ="nsew")

        self.Message_sb.config(command = self.Message_txt.yview)
        self.Message_txt.config(yscrollcommand = self.Message_sb.set)

        self.Space_lbl1 = TK.Label(self.NewMessage_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Remeber to include your username in the message")
        self.Space_lbl1.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Back_btn = TK.Button(self.NewMessage_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.NewMessage_fr, 1))
        self.Back_btn.grid(row = 5, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Send_btn = TK.Button(self.NewMessage_fr, bg = self.PositiveBtn_Background, activebackground = self.PositiveBtn_Active, foreground = self.Foreground, font = self.Font, text = "Send!", command = lambda: self.SendMessage())
        self.Send_btn.grid(row = 5, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.SendTo_ent.bind("<Return>", lambda e: self.SendMessage())

        self.Align_Grid(self.NewMessage_fr)

    def SendMessage(self):

        if self.SendTo_ent.get() == "":
            self.Space_lbl.config(text = "Your target username is empty")
            return
        if self.Message_txt.get("1.0", "end") == "":
            self.Space_lbl.config(text = "Your message feild was empty")
            return
        self.TargetUser = Hash.Hash(str(self.SendTo_ent.get()))
        self.Message = str(self.Message_txt.get("1.0", "end"))

        
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT Messages FROM Users WHERE Username = ?", (self.TargetUser,))
                for i in self.Cur:
                    for n in i:
                        self.TargetMessage_list = n.split(",")
            except Exception as Identifier:
                self.TargetMessage_list = []

            try:
                self.TargetMessage_list.append(self.Message)
            except AttributeError:
                self.Space_lbl.config(text = "That user doesn't exist")
                return
            self.TargetMessage_list = ",".join(self.TargetMessage_list)

            try:
                self.Cur.execute("UPDATE Users SET Messages = ? WHERE Username = ?", (self.TargetMessage_list, self.TargetUser))
            except Exception as Identifier:
                self.Space_lbl.config(text = Identifier)
                return

        self.Back(self.NewMessage_fr, 1)
    
    def AdminMenu(self):

        self.MainMenu_fr.destroy()
        self.AdminMenu_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.AdminMenu_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.AdminMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Admin Menu:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.AdminMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.GiveWarning_btn = TK.Button(self.AdminMenu_fr, bg = self.Btn_Background, foreground = self.Foreground, font = self.Font, activebackground = self.Btn_Active, text = "Give Warning", command = lambda: self.GiveWarning())
        self.GiveWarning_btn.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.viewBugs_btn = TK.Button(self.AdminMenu_fr, bg = self.Btn_Background, foreground = self.Foreground, activebackground = self.Btn_Active, font = self.Font, command = lambda: self.ViewBugs(), text = "View Bugs")
        self.viewBugs_btn.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl1 = TK.Label(self.AdminMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Back_btn = TK.Button(self.AdminMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, command = lambda: self.Back(self.AdminMenu_fr, 1), text = "Back")
        self.Back_btn.grid(row = 5, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Align_Grid(self.AdminMenu_fr)

    
    def ViewBugs(self):
        self.AdminMenu_fr.destroy()

        self.ViewBugs_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.ViewBugs_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.ViewBugs_fr, bg = self.Background, foreground = self.Foreground, text = "Bug Viewer", font = self.TitleFont)
        self.Title_lbl.grid(row = 0, column = 0 ,padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.ViewBugs_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "nsew")

        
        with lite.connect("myDatabase.db") as self.Con:
            self.BugReports = []
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT * FROM Bugs")
                for i in self.Cur:
                        self.BugReports.append(i)
            except Exception:
                self.BugReports.append(("","","No bugs reported"))
                pass
        if not self.BugReports:
            self.BugReports.append(("","","No bugs reported"))
            pass
        for i in self.BugReports:
            self.BugDetail_btn = TK.Button(self.ViewBugs_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, command = lambda Num = self.BugReports.index(i): self.BugDetails(Num), text = i[2])
            self.BugDetail_btn.grid(row = self.BugReports.index(i) + 2, column = 0, sticky = "nsew", padx = 2, pady = 2)

            if i[2] == "No bugs reported":
                self.BugDetail_btn.config(state = "disabled")

            if self.BugReports.index(i) == len(self.BugReports)-1:
                self.Space_lbl = TK.Label(self.ViewBugs_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
                self.Space_lbl.grid(row = self.BugReports.index(i) + 3, column = 0, padx = 2, pady = 2, sticky = "nsew")

                self.Back_btn = TK.Button(self.ViewBugs_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.ViewBugs_fr, 4))
                self.Back_btn.grid(row = self.BugReports.index(i) + 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

    
    def BugDetails(self, Num):
        self.BugNumber = Num
        self.ViewBugs_fr.destroy()
        self.BugDetails_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.BugDetails_fr.pack(fill = TK.BOTH, expand = True)
			
        self.BugTitle_lbl = TK.Label(self.BugDetails_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = self.BugReports[Num][2])
        self.BugTitle_lbl.grid(row = 0 , column = 0, padx = 2, pady = 2,sticky = "nsew")
			
        self.Space_lbl = TK.Label(self.BugDetails_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = self.BugReports[self.BugNumber][3])
        self.Space_lbl.grid(row = 1, column = 0, padx = 2, pady = 2, sticky  = "nsew")

        self.Button_fr = TK.Frame(self.BugDetails_fr, bg = self.Background)
        self.Button_fr.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.SetImportant_btn = TK.Button(self.Button_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, command = lambda: self.UpdateStatus("Important"), text = " ! ")
        self.SetImportant_btn.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.SetFixing_btn = TK.Button(self.Button_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Fixing", command = lambda: self.UpdateStatus("Fixing"))
        self.SetFixing_btn.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.DeleteReport_btn = TK.Button(self.Button_fr, bg = self.QuitBtn_Background, foreground = self.Foreground, activebackground = self.QuitBtn_Active, text = " X ", font = self.Font, command = lambda: self.DeleteBugReport())
        self.DeleteReport_btn.grid(row = 0, column = 2, pady = 2, padx = 2, sticky = "nsew")

        self.Back_btn = TK.Button(self.BugDetails_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.BugDetails_fr, 5))
        self.Back_btn.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.BugDetails_fr)
        self.Align_Grid(self.Button_fr)
		

    def UpdateStatus(self, Status):
        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("UPDATE Bugs SET Status = ? WHERE ID = ?", (str(Status), self.BugReports[self.BugNumber][0]))
            except Exception as Identifier:
                print(Identifier)
                return
        
        self.Back(self.BugDetails_fr, 5)

    def DeleteBugReport(self):
        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("DELETE FROM Bugs WHERE ID = ?", (self.BugReports[self.BugNumber][0],))
            except Exception as Identifier:
                print(Identifier)
                return

        self.Back(self.BugDetails_fr, 5)
    
    def GiveWarning(self):
        self.AdminMenu_fr.destroy()
        self.GiveWarning_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.GiveWarning_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.GiveWarning_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Give Warnings")
        self.Title_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.Space_lbl = TK.Label(self.GiveWarning_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)

        self.WarnedUser_lbl = TK.Label(self.GiveWarning_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Username:")
        self.WarnedUser_lbl.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.WarnedUser_ent = TK.Entry(self.GiveWarning_fr, foreground = self.Foreground, font = self.Font)
        self.WarnedUser_ent.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "nsew")
        self.WarnedUser_ent.focus()

        self.Space_lbl1 = TK.Label(self.GiveWarning_fr, foreground = self.Foreground, font = self.Font, bg = self.Background)
        self.Space_lbl1.grid(row = 3, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

        self.WarnUser_btn = TK.Button(self.GiveWarning_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Give Warning", command = lambda: self.WarnUser())
        self.WarnUser_btn.grid(row = 4, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

        self.Back_btn = TK.Button(self.GiveWarning_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.GiveWarning_fr, 4))
        self.Back_btn.grid(row = 5, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

        self.WarnedUser_ent.bind("<Return>", lambda e: self.WarnUser())

        self.Align_Grid(self.GiveWarning_fr)
    

    def WarnUser(self):
        self.WarnedUsername = Hash.Hash(str(self.WarnedUser_ent.get()))

        
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT Warnings FROM Users WHERE UserName = ?", (self.WarnedUsername,))

                try:

                    self.NumWarnings = int(self.Cur.fetchall()[0][0])
                    self.NumWarnings += 1
                    self.NumWarnings = str(self.NumWarnings)

                    self.Cur.execute("UPDATE Users SET Warnings = ? WHERE UserName = ?", (self.NumWarnings, self.WarnedUsername))
                except TypeError:
                    pass
            except Exception as Identifier:
                print(Identifier)
    
    def OwnerMenu(self):
        self.MainMenu_fr.destroy()
        self.OwnerMenu_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.OwnerMenu_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.OwnerMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Owner Menu:")
        self.Title_lbl.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.OwnerMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.ChangeAccountType_btn = TK.Button(self.OwnerMenu_fr, bg = self.Btn_Background, foreground = self.Foreground, font = self.Font, activebackground = self.Btn_Active, text = "Change Account Type", command = lambda: self.ChangeAccountType_GUI())
        self.ChangeAccountType_btn.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.DeleteUserAccount_btn = TK.Button(self.OwnerMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Delete Account", command = lambda: self.DeleteUserAccount())
        self.DeleteUserAccount_btn.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Space_lbl1 = TK.Label(self.OwnerMenu_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Back_btn = TK.Button(self.OwnerMenu_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, command = lambda: self.Back(self.OwnerMenu_fr, 1), text = "Back")
        self.Back_btn.grid(row = 5, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Align_Grid(self.OwnerMenu_fr)

    def DeleteUserAccount(self):
        self.OwnerMenu_fr.destroy()
        self.DeleteUserAccount_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.DeleteUserAccount_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.DeleteUserAccount_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Delete User Account:")
        self.Title_lbl.grid(row = 0, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.DeleteUserAccount_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, columnspan = 2, padx = 2, pady = 2)

        self.TargetUser_lbl = TK.Label(self.DeleteUserAccount_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Username:")
        self.TargetUser_lbl.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.TargetUser_ent = TK.Entry(self.DeleteUserAccount_fr, foreground = self.Foreground, font = self.Font)
        self.TargetUser_ent.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl1 = TK.Label(self.DeleteUserAccount_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl1.grid(row = 3, padx = 2, pady = 2, column = 0 ,columnspan = 2, sticky = "nsew")

        self.ConfurmDeleteUserAccount_btn = TK.Button(self.DeleteUserAccount_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, foreground = self.Foreground, font = self.Font, text = "Delete Account", command = lambda: self.DeleteUserAccountAction())
        self.ConfurmDeleteUserAccount_btn.grid(row = 4, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.Back_btn = TK.Button(self.DeleteUserAccount_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, command = lambda: self.Back(self.DeleteUserAccount_fr, 6), text = "Back")
        self.Back_btn.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Align_Grid(self.DeleteUserAccount_fr)
    
    def DeleteUserAccountAction(self):
        
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("DELETE FROM Users WHERE Username = ?", (Hash.Hash(str(self.TargetUser_ent.get())),))
            except Exception as Identifier:
                self.Space_lbl.config(text = Identifier)
        self.Back(self.DeleteUserAccount_fr, 6)
    
    
    def ChangeAccountType_GUI(self):
        self.OwnerMenu_fr.destroy()
        self.ChangeAccountType_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.ChangeAccountType_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.ChangeAccountType_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Change Account Types:")
        self.Title_lbl.grid(row = 0, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.ChangeAccountType_fr, bg = self.Background, font = self.Font, foreground = self.Foreground)
        self.Space_lbl.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2)

        self.TargetUsername_lbl = TK.Label(self.ChangeAccountType_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Username:")
        self.TargetUsername_lbl.grid(row = 2, padx = 2, pady = 2, sticky = "nsew", column = 0)

        self.TargetUsername_ent = TK.Entry(self.ChangeAccountType_fr, foreground = self.Foreground, font = self.Font)
        self.TargetUsername_ent.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.AccountType_lbl = TK.Label(self.ChangeAccountType_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Account Type:")
        self.AccountType_lbl.grid(row = 3, column = 0, sticky = "nsew", padx=2, pady = 2)

        self.StrVar = TK.StringVar(self.ChangeAccountType_fr)
        self.StrVar.set("standered")

        self.AccountType_dd = TK.OptionMenu(self.ChangeAccountType_fr, self.StrVar, "standered", "admin", "owner", "higher")
        self.AccountType_dd.config(bg = self.Background, foreground = self.Foreground, font = self.Font, activebackground = self.Background)
        self.AccountType_dd["menu"].config(bg = self.Background, foreground = self.Foreground, font = self.Font, activebackground = self.Background)
        self.AccountType_dd["highlightthickness"] = 0
        self.AccountType_dd.grid(row = 3, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl1 = TK.Label(self.ChangeAccountType_fr, bg = self.Background, font = self.Font, foreground = self.Foreground)
        self.Space_lbl1.grid(row = 4, column = 0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2)

        self.ConfurmChangeAccountType_btn = TK.Button(self.ChangeAccountType_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, text = "Change Account", command = lambda: self.ChangeAccountType())
        self.ConfurmChangeAccountType_btn.grid(row = 5, column = 1, padx = 2, pady = 2, sticky = "nsew")

        self.Back_btn = TK.Button(self.ChangeAccountType_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, foreground = self.Foreground, font = self.Font, command = lambda: self.Back(self.ChangeAccountType_fr, 6), text = "Back")
        self.Back_btn.grid(row = 5, column = 0, padx = 2, pady = 2, sticky = "nsew")

        self.Align_Grid(self.ChangeAccountType_fr)
    
    def ChangeAccountType(self):
        self.NewAccountType = self.StrVar.get()
        self.TargetUsername = Hash.Hash(str(self.TargetUsername_ent.get()))

        
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("UPDATE Users SET AccountType = ? WHERE Username = ?", (self.NewAccountType.lower(), self.TargetUsername))
            except Exception as Identifier:
                self.Space_lbl.config(text = Identifier)
        
        self.Back(self.ChangeAccountType_fr, 6)

    #Allows for the grids to expand with the root window
    def Align_Grid(self, Frame):
        #Gets the nuber of rows and columns of the grid
        self.Grid_Size = Frame.grid_size()

        #Loops through every column
        for i in range(self.Grid_Size[0]):
            #Sets the weight to a non zero value so it can expand
            Frame.columnconfigure(i, weight = 1)
        #Loops through every row
        for i in range( self.Grid_Size[1]):
            #Sets the weight to a non zero value so it can expand
            Frame.rowconfigure(i, weight = 1)

    #Gives a help screen to explain how things work and what to do if you cannot remeber your login
    def Help(self):
        self.Help_tl = TK.Toplevel(bg = self.Background)
        self.Help_tl.title("Help!")

        self.HelpStr = """To login to your account please type in your username and password.
        If you do not have an account please click "new account".
        If you have forgeten your username; please contact an administrator.
        If you have forgoten your password; please click "reset password".
        Otherwise please clixk the X to close this window.
        """

        self.Help_lbl = TK.Label(self.Help_tl, bg = self.Background, foreground = self.Foreground, font = self.Font, text = self.HelpStr)
        self.Help_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.PasswordReset_btn = TK.Button(self.Help_tl, bg = self.Btn_Background, activebackground = self.Btn_Active, text = "Reset Password", font = self.Font, foreground = self.Foreground, command = lambda: self.ResetPassword())
        self.PasswordReset_btn.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.Help_tl)
    
    #Allows a user to reset there password if they have forgoten it and put in there email
    def WorkInProgress(self):
        self.WIP_tl = TK.Toplevel(bg = self.Background)
        self.WIP_lbl = TK.Label(self.WIP_tl, font = self.Font, foreground = self.Foreground, bg = self.Background, text = "This feature is currently a work in progress, we appologise fore any inconvinience")
        self.WIP_lbl.grid(row = 0, column = 0, sticky = "nsew")

        self.Align_Grid(self.WIP_tl)
    
    def ResetPassword(self):
        self.Help_tl.destroy()
        self.Login_fr.destroy()

        self.ResetPassword_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.ResetPassword_fr.pack(fill = TK.BOTH, expand = True)

        self.Title_lbl = TK.Label(self.ResetPassword_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "Reset Password")
        self.Title_lbl.grid(row = 0, column = 0, columnspan =2, sticky = "nsew", padx = 2, pady = 2)

        self.Space_lbl = TK.Label(self.ResetPassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 2)

        self.ExplainationText = """Please type in your username and the email asocioated with it.
        If you haven't linked your email this will not work; please conntact a system admin.
        If you do not reseve a reset email; please contact a system admin.
        """

        self.Explaination_lbl = TK.Label(self.ResetPassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = self.ExplainationText)
        self.Explaination_lbl.grid(row = 2, column = 0, columnspan = 2, padx = 2, pady = 2)

        self.Username_lbl = TK.Label(self.ResetPassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Username:")
        self.Username_lbl.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Username_ent = TK.Entry(self.ResetPassword_fr, foreground = self.Foreground, font = self.Font)
        self.Username_ent.grid(row = 3, column = 1, sticky = "nsew", padx = 2, pady = 2)
        self.Username_ent.focus()

        self.Email_lbl = TK.Label(self.ResetPassword_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = "Email:")
        self.Email_lbl.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Email_ent = TK.Entry(self.ResetPassword_fr, foreground = self.Foreground, font = self.Font)
        self.Email_ent.grid(row = 4, column = 1, sticky = "nsew", padx = 2, pady =2)

        self.Button_fr = TK.Frame(self.ResetPassword_fr, bg = self.Background)
        self.Button_fr.grid(row = 5, column =0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2)

        self.ResetPassword_btn = TK.Button(self.Button_fr, bg = self.PositiveBtn_Background, foreground = self.Foreground, activebackground = self.PositiveBtn_Active, font = self.Font, text = "Reset Password", command = lambda: self.PasswordReset())
        self.ResetPassword_btn.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

        self.Email_ent.bind("<Return>", lambda e: self.PasswordReset())
        self.Username_ent.bind("<Return>", lambda e: self.PasswordReset())

        self.QUIT_btn = TK.Button(self.Button_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, foreground = self.Foreground, font = self.Font, text = "Quit", command = lambda: self.Quit())
        self.QUIT_btn.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2)

        self.Back_btn = TK.Button(self.Button_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.ResetPassword_fr, 0))
        self.Back_btn.grid(row = 0, column = 2, sticky = "nsew", padx = 2, pady = 2)

        self.Align_Grid(self.Button_fr)
        self.Align_Grid(self.ResetPassword_fr)


    def PasswordReset(self):
        self.Space_lbl.config(text = "")

        self.Username = Hash.Hash(str(self.Username_ent.get()))
        self.Email = Hash.Hash(str(self.Email_ent.get()))

        if self.Username == "" or str(self.Email_ent.get()) == "":
            self.Space_lbl.config(text = "Sorry one of your feilds was empty")
            self.Username_ent.focus()
            self.Username_ent.delete(0, 'end')
            self.Email_ent.delete(0, 'end')
            return

        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT Email FROM Users WHERE Username = ?", ((self.Username,)))
                self.UsersEmail = self.Cur.fetchall()[0][0]
            except Exception as Identifier:
                self.Space_lbl.config(text = "Sorry this username dosn't have an email associated with it")
                self.Username_ent.focus()
                self.Username_ent.delete(0, "end")
                self.Email_ent.delete(0, "end")
                return
            
        
        if self.UsersEmail == self.Email:
            from random import randint
            self.RandomNum = randint(10000, 100000)
            Email.Email(str(self.Email_ent.get()), NewPassword = self.RandomNum)

            

            with lite.connect("myDatabase.db") as self.Con:
                self.Cur = self.Con.cursor()
                try:
                    self.Cur.execute("UPDATE Users SET Password = ? WHERE Username = ?", (Hash.Hash(self.RandomNum), self.Username))
                except Exception as Identifier:
                    print(Identifier)
            
            self.Space_lbl.config(text = "You new password has been successfully sent!")
            self.Username_ent.delete(0, 'end')
            self.Email_ent.delete(0, 'end')
            return
        else:
            self.Space_lbl.config(text = "Sorry that email wasn't the one in our database")
            self.Username_ent.delete(0, 'end')
            self.Email_ent.delete(0, 'end')
            return

    
    def Quit(self):
        root.destroy()

    def Login(self):
        
        self.Username = Hash.Hash(str(self.Username_ent.get()))
        self.Password = Hash.Hash(str(self.Password_ent.get()))

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                self.Cur.execute("SELECT Password FROM Users WHERE UserName = ?", ((self.Username,)))

                self.UserPassword = self.Cur.fetchall()[0][0]
            except Exception:
                self.Space_lbl.config(text = "Username/Password is incorrect")
                self.Username_ent.delete(0, "end")
                self.Password_ent.delete(0, "end")
                return

            if self.Password == self.UserPassword:
                self.Username_ent.delete(0, "end")
                self.Password_ent.delete(0, "end")

                self.MainMenu()

                return
            else:
                self.Space_lbl.config(text = "Username/Password is incorrect")
                self.Username_ent.focus()
                self.Username_ent.delete(0, "end")
                self.Password_ent.delete(0, "end")
                return
    
    def Back(self, CurrentFrame, GoTo):
        CurrentFrame.destroy()

        if GoTo == 0:
            self.LoginScreen()
        elif GoTo == 1:
            self.MainMenu()
        elif GoTo == 2:
            self.Settings()
        elif GoTo == 3:
            self.AccountSettings()
        elif GoTo == 4:
            self.AdminMenu()
        elif GoTo == 5:
            self.ViewBugs()
        elif GoTo == 6:
            self.OwnerMenu()
        else:
            pass
    
    def CreateAccount(self):
        #Clears the space lbl
        self.Space_lbl.config(text = "")

        #Sets all of the column varables for the new user
        self.Username = Hash.Hash(str(self.Username_ent.get()))
        #These are hashed so i never see there real passwords
        self.Password = str(Hash.Hash(str(self.Password_ent.get())))
        self.RepeatPassword = str(Hash.Hash(str(self.RepeatPassword_ent.get())))
        self.AccountType = "standered"
        self.Warnings = 0

        #Makes sure your passwords match
        if self.Password == self.RepeatPassword:
            pass
        #If they don't it will tell the user and clear their inputs
        else:
            self.Space_lbl.config(text = "Sorry your passwords didn't match")
            self.Username_ent.focus()
            self.Username_ent.delete(0, 'end')
            self.Password_ent.delete(0, 'end')
            self.RepeatPassword_ent.delete(0, 'end')
            return
        
        #checksthe feild isn't empty
        if self.Username == "" or self.Password_ent.get() == "" or self.RepeatPassword_ent.get() == "":
            self.Space_lbl.config(text = "Sorry one of your feils was empty")
            self.Username_ent.delete(0, 'end')
            self.Password_ent.delete(0, 'end')
            self.RepeatPassword_ent.delete(0, 'end')
            self.Username_ent.focus()
            return
        
        

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            try:
                #Tests if the username already exists in the database
                self.Cur.execute("SELECT EXISTS (SELECT * FROM Users WHERE Username = ?)", ((self.Username,)))
                for i in self.Cur:
                    for n in i:
                        if n == 1:#0 meand the username isn't there 1 means it already exists
                            #If the username already exists it will tell the userr and clear their inputs
                            self.Space_lbl.config(text = "Sorry this username is already taken")
                            self.Username_ent.focus()
                            self.Username_ent.delete(0, 'end')
                            self.Password_ent.delete(0, 'end')
                            self.RepeatPassword_ent.delete(0, 'end')
                            return
                        else:
                            pass
            except Exception:
                return

        #Connects to the database

        with lite.connect("myDatabase.db") as self.Con:#Automatically closes the connection when it is done
            self.Cur = self.Con.cursor()#Creates the curser object
            try:
                self.Cur.execute("INSERT INTO USERS(Username, Password, AccountType, Warnings) VALUES(?, ?, ?, ?)", (self.Username, self.Password,self.AccountType, self.Warnings))
            except Exception:
                pass
        self.NewAccount_fr.destroy()

        self.LoginScreen(SpaceText = "Account sucessfully created")
    
    def NewAccount(self):
        #Creats a new standered user account
        #Destroys the old login frame
        self.Login_fr.destroy()

        #Creats a new new account frame to build up from
        self.NewAccount_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.NewAccount_fr.pack(fill = TK.BOTH, expand = True)

        #Adds a title
        self.Title_lbl = TK.Label(self.NewAccount_fr, bg = self.Background, foreground = self.Foreground, font = self.TitleFont, text = "New Account")
        self.Title_lbl.grid(row = 0, column =0, columnspan = 2, padx = 2, pady = 2, sticky = "nsew")

        self.Space_lbl = TK.Label(self.NewAccount_fr, bg = self.Background, foreground = self.Foreground, font = self.Font)
        self.Space_lbl.grid(row = 1, column = 0, columnspan = 2, padx = 2, pady =2, sticky = "nsew")

        #Shows where to type your new username
        self.Username_lbl = TK.Label(self.NewAccount_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Username:")
        self.Username_lbl.grid(row = 2, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #Gives a place to type in your new username
        self.Username_ent = TK.Entry(self.NewAccount_fr, font = self.Font, foreground = self.Foreground)
        self.Username_ent.grid(row = 2, column = 1, sticky = "nsew", padx = 2, pady = 2)
        self.Username_ent.focus()

        #Shows where to type your new password
        self.Password_lbl = TK.Label(self.NewAccount_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Password:")
        self.Password_lbl.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #Gives a place to type in your new password which hides the text
        self.Password_ent = TK.Entry(self.NewAccount_fr, font = self.Font, foreground = self.Foreground, show = "•")
        self.Password_ent.grid(row = 3, column = 1, sticky = "nsew", padx = 2, pady = 2)

        #Shows where to type your new password
        self.RepeatPassword_lbl = TK.Label(self.NewAccount_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Password (Again):")
        self.RepeatPassword_lbl.grid(row = 4, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #Gives a place to type in your new password which hides the text
        self.RepeatPassword_ent = TK.Entry(self.NewAccount_fr, font = self.Font, foreground = self.Foreground, show = "•")
        self.RepeatPassword_ent.grid(row = 4, column = 1, sticky = "nsew", padx = 2, pady = 2)

        #Creats a frame to store the buttons
        self.Button_fr = TK.Frame(self.NewAccount_fr, bg = self.Background)
        self.Button_fr.grid(row = 5, column = 0, columnspan = 2, sticky = "nsew", padx = 2, pady = 2)

        #When clicked will run the quting processes
        self.QUIT_btn = TK.Button(self.Button_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, font = self.Font, foreground = self.Foreground, text = "QUIT", command = lambda: self.Quit())
        self.QUIT_btn.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #When clicked will run the create account processes
        self.CreateAccount_btn = TK.Button(self.Button_fr, bg = self.PositiveBtn_Background, activebackground = self.PositiveBtn_Active, font = self.Font, foreground = self.Foreground, text = "Create Account", command = lambda: self.CreateAccount())
        self.CreateAccount_btn.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

        #When clicked will take the user back to the login screen
        self.Back_btn = TK.Button(self.Button_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "Back", command = lambda: self.Back(self.NewAccount_fr, 0))
        self.Back_btn.grid(row = 0, column = 2, sticky = "nsew", padx = 2, pady = 2)

        self.RepeatPassword_ent.bind("<Return>", lambda e: self.CreateAccount())
        self.Password_ent.bind("<Return>", lambda e: self.CreateAccount())
        self.Username_ent.bind("<Return>", lambda e: self.CreateAccount())

        self.Align_Grid(self.Button_fr)

        self.Align_Grid(self.NewAccount_fr)


    def __init__(self, root):
        #Creats the main window for the login screen to load into

        #Used incase the db doesn't exist to add all of the needed columns
        self.Title = [
            "UserName",
            "Password", 
            "AccountType",
            "Warnings",
            "Email", 
            "Messages",
        ]

        #If the database dosn't exist it will create it if it does nothing will happen
        #Connects to the database

        with lite.connect("myDatabase.db") as self.Con:#Automatically closes the connection when it is done
            self.Cur = self.Con.cursor()#Creates the curser object
            try:
                self.Cur.execute("CREATE TABLE Users(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)")#Creates the table
                for i in range(len(self.Title)):#Adds the kwargs to the table
                    self.Cur.execute("ALTER TABLE Users ADD COLUMN {ColumnName} TEXT".format(ColumnName = str(self.Title[i]), ))
                pass
            except Exception:#If the databse or table already exist it will exit
                pass
        
        #Sets the main frame- this will achally control the screen instead of the root
        self.Main_fr = TK.Frame(root, bg = "#7eccf7")
        self.Main_fr.pack(fill = TK.BOTH, expand = True)

        self.SetDefults(Update = False)#Sets all of the GUI personilation varibes to their defult value

        #Calls the login screen
        self.LoginScreen()

    
    def LoginScreen(self, SpaceText = ""):
        #Sets up the login screen for entering usernames and passwords
        self.SetDefults(Update = False)#Resets all of the defult values

        #Creats the login frame
        self.Login_fr = TK.Frame(self.Main_fr, bg = self.Background)
        self.Login_fr.pack(fill = TK.BOTH, expand = True)

        #Titles the screen
        self.Title_lbl = TK.Label(self.Login_fr, bg = self.Background, font = self.TitleFont, foreground = self.Foreground, text = "Please Login...")
        self.Title_lbl.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2, columnspan = 3)

        self.Space_lbl = TK.Label(self.Login_fr, bg = self.Background, foreground = self.Foreground, font = self.Font, text = SpaceText)
        self.Space_lbl.grid(row = 1, column = 0, columnspan = 2, padx = 2, pady =2, sticky = "nsew")

        #Shows where to type your username
        self.Username_lbl = TK.Label(self.Login_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Username:")
        self.Username_lbl.grid(row = 2, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #Gives a place to type in your username
        self.Username_ent = TK.Entry(self.Login_fr, font = self.Font, foreground = self.Foreground)
        self.Username_ent.grid(row = 2, column = 1, sticky = "nsew", padx = 2, pady = 2)
        self.Username_ent.focus()

        #Shows where to type your password
        self.Password_lbl = TK.Label(self.Login_fr, bg = self.Background, font = self.Font, foreground = self.Foreground, text = "Password:")
        self.Password_lbl.grid(row = 3, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #Gives a place to type in your password which hides the text
        self.Password_ent = TK.Entry(self.Login_fr, font = self.Font, foreground = self.Foreground, show = "•")
        self.Password_ent.grid(row = 3, column = 1, sticky = "nsew", padx = 2, pady = 2)


        #Will provide instructions of what to do if you cannot work it out
        self.Help_btn = TK.Button(self.Login_fr, bg = self.Background, activebackground = self.Background, font = self.Font, foreground = self.Foreground, text = "?", command = lambda: self.Help())
        self.Help_btn.grid(row = 2, column = 2, sticky = "nsew", padx = 1, pady = 2, rowspan = 2)

        #Will house and grid all of the buttons
        self.Button_fr = TK.Frame(self.Login_fr, bg = self.Background)
        self.Button_fr.grid(row = 4, column = 0, columnspan = 3, sticky = "nsew", padx = 2, pady = 2)

        #When clicked will run the quting processes
        self.QUIT_btn = TK.Button(self.Button_fr, bg = self.QuitBtn_Background, activebackground = self.QuitBtn_Active, font = self.Font, foreground = self.Foreground, text = "Quit", command = lambda: self.Quit())
        self.QUIT_btn.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2)

        #When clicked will run the login processes
        self.Login_btn = TK.Button(self.Button_fr, bg = self.PositiveBtn_Background, activebackground = self.PositiveBtn_Active, font = self.Font, foreground = self.Foreground, text = "Login", command = lambda: self.Login())
        self.Login_btn.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

        #When clicked will run the newaccount processes
        self.NewAccount_btn = TK.Button(self.Button_fr, bg = self.Btn_Background, activebackground = self.Btn_Active, font = self.Font, foreground = self.Foreground, text = "New Account", command = lambda: self.NewAccount())
        self.NewAccount_btn.grid(row = 0, column = 2, sticky = "nsew", padx = 2, pady = 2)

        self.Username_ent.bind("<Return>", lambda e: self.Login())
        self.Password_ent.bind("<Return>", lambda e: self.Login())
        self.Login_fr.bind("<Return>", lambda e: self.Login())

        self.Align_Grid(self.Button_fr)

        self.Align_Grid(self.Login_fr)


#Will only run if it is the program originally started
if __name__ == "__main__":

    #Creasts the GUI root and titles it
    root = TK.Tk()
    root.title("LoginAccess 3.0")
    Run = Main(root)

    #Allows for the GUI to dynamically respond
    while True:
        try:
            root.update()
            root.update_idletasks()
        except TK._tkinter.TclError:
            raise SystemExit
