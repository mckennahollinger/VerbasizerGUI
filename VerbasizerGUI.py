#Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.filedialog
import re
import random

#NLP Pkg
import nltk
from nltk.tokenize import word_tokenize
nltk.download()


# TODO adjust textfield size in proportion to window size: https://stackoverflow.com/questions/47127875/python-tkinter-how-to-resize-widgets-when-user-expands-the-windows
# TODO attach scrollbar to text widget: https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget/13833338
# TODO number lines in textboxes: https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
# TODO Highlight randomized text based on POS: https://stackoverflow.com/questions/3781670/how-to-highlight-text-in-a-tkinter-text-widget
# TODO Create custom file type to save revision history
# TODO Bowie's original algorithm to incorporate and expand: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
# TODO Open file: https://stackoverflow.com/questions/16429716/opening-file-tkinter
# TODO Rhyme and meter: https://us.pycon.org/2020/schedule/presentation/112/



root = tk.Tk()
root.title("Verbasizer")
w = 690
h = 500
root.geometry(f"{w}x{h}")

my_menu = Menu(root)
root.config(menu=my_menu)

#Basic instructions
enterText = Label(text="Enter desired text here:")
enterText.grid(row=0,column=0, padx=0, pady=5)
outputText = Label(text="Randomized text:")
outputText.grid(row=0, column=4, padx=15)

#Text box for user input
entry = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=30,height=27)
entry.grid(row=2, column=0, pady=5, padx=20)


#Text box for input post-randomization
output = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=30,height=27)
output.config(state=DISABLED)
output.grid(row=2, column=4, padx=35)

#Click command
def our_command():
    pass

#Create menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label="New", command=our_command)
file_menu.add_command(label="Open", command=our_command)
file_menu.add_command(label="Open Recent", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Save", command=our_command)
file_menu.add_command(label="Save As", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#Create edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)
edit_menu.add_command(label="Paste", command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=our_command)
edit_menu.add_command(label="Redo", command=our_command)

#Create "About" menu item
about_menu = Menu(my_menu)
my_menu.add_cascade(label="About",menu=about_menu)
about_menu.add_command(label = "README", command=our_command)

#Create "Options" menu item
options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)

#Define function that randomizes input
# TODO incorporate Markov chains and train model to best organize lyrics according to English grammar structure
# TODO allow user to select text to randomize further: https://stackoverflow.com/questions/4073468/how-do-i-get-a-selected-string-in-from-a-tkinter-text-box?lq=1
def randomize():
    result = output.get("1.0", 'end-1c')
    if len(result)>=1:
       output.delete(1.0,END)
    input = entry.get("1.0", 'end-1c')
    if len(input)>=1:
        words = word_tokenize(input)
        pos_tagged_text = nltk.pos_tag(words)
        print(pos_tagged_text)
        input = re.split('[\s,\n]', input)
        random.shuffle(input)
        output.config(state=NORMAL)
        output.insert(tk.INSERT,input)


#Create frame to organize buttons
buttonFrame = Frame(root)
buttonFrame.grid(row=2, column=3, rowspan=2)

#Randomize button
randomizeButton = Button(buttonFrame, text="Randomize", command=randomize)
randomizeButton.grid(row=1, column=0)

#Runs everything inside window
root.mainloop()




