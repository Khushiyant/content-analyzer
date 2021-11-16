############################################
#               Imports                    #
############################################

from time import sleep
from tkinter import *

import cv2
from PIL import Image, ImageTk

from funcs import funcs as fc

############################################
#               End                        #
############################################

class interactiveUI:
    def __init__(self):

        waittime = 2900  # Loading Screen Time

        loading = Tk()
        loading.title("Content Analyzer")
        loading.resizable(width=False, height=False)

        # Loading up the required .png files
        icon = PhotoImage(file="Resources\logo.png")
        cover = Image.open("Resources\screen.png")

        # Icon for program
        loading.iconphoto(False, icon)

        # Extracting the screen size of user screen
        screen_height = loading.winfo_screenheight()
        screen_width = loading.winfo_screenwidth()

        # Setting up the loading screen size
        loading.geometry("%dx%d+%d+%d" % (screen_width//2,
                                          screen_height//2, screen_width//4, screen_height//4))

        # Cover for loading screen
        re_cover = cover.resize((screen_width//2, screen_height//2))
        cover = ImageTk.PhotoImage(re_cover)
        label = Label(loading, image=cover)
        label.pack()

        def main_window():
            # Remove the loading screen after waittime
            loading.destroy()

            # Basic Setup for size,icon,etc;
            self.root = Tk()
            self.root.title("Content Analyzer")
            icon = PhotoImage(file="Resources\logo.png")
            self.root.iconphoto(False, icon)
            self.root.geometry("{0}x{1}+0+0".format(
                self.root.winfo_screenwidth()-0, self.root.winfo_screenheight()-0))

            # About file Menu
            self.menubar = Menu(self.root)
            self.root.config(menu=self.menubar)
            self.file = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label='File', menu=self.file)
            self.file.add_command(label='New Capture', command=fc.new)
            self.file.add_command(label='Open...', command=fc.open)
            self.file.add_separator()
            self.file.add_command(label='Exit', command=self.root.destroy)

            # Adding Help Menu
            self.help_ = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label='Help', menu=self.help_)
            self.help_.add_command(label='Help', command=fc.help)
            self.help_.add_separator()
            self.help_.add_command(label='About Analyzer', command=fc.about)

            # Main Interaction
            self.leftframe = Frame(self.root)
            self.leftframe.pack(side=LEFT)
            self.rightframe = Frame(self.root, bg="#000")
            self.rightframe.pack(side=RIGHT)

            # START- Content for landing screen

            landing_content = str()
            with open("Resources\landing.txt", "r") as ld:
                landing_content += ld.read()

            # END
            self.leftlabel = Label(self.leftframe, text=landing_content, fg="white",
                                   bg="skyblue", pady=0, padx=0, height=screen_height//15, width=screen_width//20, font=('Helvatical bold', 20))
            self.leftlabel.pack()

            self.rightbutton = Button(self.rightframe, text="Get Started", fg="white",
                                      bg="grey", pady=0, padx=0, height=3, width=50, command=fc.processVideo)
            self.rightbutton.pack()

        loading.after(waittime, main_window)
        mainloop()
