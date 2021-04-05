# imports the necessary libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import os
import time
import webbrowser

# variables

global filename
global current
global title

title = "PySheet"

# defines all the functions

def about():
    tk.messagebox.showinfo("PySheet pre-0.0.1", "PySheet pre-0.0.1\nA Python Based Spreadsheet Reader Compatible with CSV files.\n\nThis software was made by Tom Rolfe\nVisit my GitHub @ www.github.com/zeddytbr for more info!\nCoded with Python - GUI made using TKinter\n\nLicensed under GNU General Public License V3.0")

def openfile():
    filename = tk.filedialog.askopenfilename(filetypes =(("CSV Files", "*.csv"),("All Files (may cause errors - CSV files are recommended","*.*")),title = "PySheet File Handler - Choose a file.")
    #print(filename)
    title=str(filename)
    if filename != "":
        answer = messagebox.askokcancel("PySheet File Handler","Open '" + filename + "'?")
        if answer == True:
            current = open(filename,"r+")
            print(current.read())
            master.quit()
            masterstart()
            print(title)
        else:
            filename = False

def github():
    webbrowser.open("https://github.com/zeddytbr/PySheet")

def website():
    webbrowser.open("https://www.tomrolfe.com")


# main window
master = tk.Tk()
master.title("PySheet")

# display the menu
menubar = tk.Menu(master)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Website", command=website)
helpmenu.add_command(label="GitHub", command=github)
menubar.add_cascade(label="Help", menu=helpmenu)

master.config(menu=menubar)

#window elements

sheetframe = tk.LabelFrame(master, borderwidth="10", relief="groove", text=title)
actionbarframe = tk.Frame(master, borderwidth="2", relief="ridge")

a1 = tk.Entry(sheetframe)
a1.grid(row=1, column=1)

sheetframe.grid(row=10, column=10,padx=10, pady=10, sticky="nw")
actionbarframe.grid(row=20, sticky="nw", column=10,padx=10,pady=10)

tk.Button(actionbarframe, text='Open', command=openfile).grid(column=10, sticky="nw", padx=1,pady=1)

# window options

master.geometry("640x480")
master.iconbitmap(os.path.dirname(os.path.realpath(__file__))+"/logobase.ico")

def masterstart():
    master.mainloop()

masterstart()