import cv2
from document_select import perspective
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile
from time import sleep
from PIL import Image, ImageTk


class interactiveUI:
    def __init__(self, loading, screen_height, screen_width):

        waittime = 0  # Loading Screen Time

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
            self.file.add_command(label='New Capture', command=self.new)
            self.file.add_command(label='Open...', command=self.open)
            self.file.add_separator()
            self.file.add_command(label='Exit', command=self.root.destroy)

            # Adding Help Menu
            self.help_ = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label='Help', menu=self.help_)
            self.help_.add_command(label='Help', command=self.help)
            self.help_.add_separator()
            self.help_.add_command(label='About Analyzer', command=self.about)

            # Main Interaction
            self.leftframe = Frame(self.root)
            self.leftframe.pack(side=LEFT)
            self.rightframe = Frame(self.root,bg="#000")
            self.rightframe.pack(side=RIGHT)

            # START- Content for landing screen

            landing_content = str()
            with open("Resources\landing.txt", "r") as ld:
                landing_content += ld.read()

            # END
            self.leftlabel = Label(self.leftframe, text=landing_content, fg="white",
                                   bg="skyblue", pady=0, padx=0, height=screen_height//15, width=screen_width//20,font=('Helvatical bold',20))
            self.leftlabel.pack()

            self.rightbutton = Button(self.rightframe, text="Get Started", fg="white",
                                      bg="grey", pady=0, padx=0, height=3, width=50,command=self.processVideo)
            self.rightbutton.pack()

        loading.after(waittime, main_window)

    def new(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            _, img = cap.read()
            key = cv2.waitKey(1)
            cv2.imshow("Capture",img)
            if key == 27:
                break
            elif key == 13:
                files = [('All Files', '*.*'), 
                ('PNG', '*.png'),
                ('JPG', '*.jpg')]
                file = asksaveasfile(mode='w', filetypes = files, defaultextension = files)
                if file:
                    cv2.imwrite(file.name,img)
                break
        cap.release()
        cv2.destroAllWindows()


    def open(self):
        file = filedialog.askopenfile(title='Select A File', filetypes=(
            ('PNG', '*.png'), ('JPG', '*.jpg'), ('All Files', '*.*')))
        self.processImg(file.name)

    def help(self):
        string = str()
        with open("Resources\\help.txt", "r") as h:
            string = h.read()
        messagebox.showinfo("Help", string)

    def about(self):
        string = str()
        with open("Resources\\about.txt", "r") as h:
            string = h.read()
        messagebox.showinfo("About", string)

    def processImg(self, img):
        img = cv2.imread(img)
        img = cv2.resize(img, (0, 0), fx=1.2, fy=1.2)
        scanned = perspective(img)
        key = cv2.waitKey(0)

    def processVideo(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            _, img = cap.read()
            scanned = perspective(img)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cap.release()
        cv2.destroAllWindows()


if __name__ == "__main__":
    # Basic Loading Screen Setup
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

    # Object Initialisation
    interactiveUI(loading, screen_height, screen_width)
    mainloop()
