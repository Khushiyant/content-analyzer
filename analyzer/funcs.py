############################################
#               Imports                    #
############################################

from tkinter import filedialog, messagebox
from tkinter.messagebox import askyesno
from tkinter.filedialog import asksaveasfile

import cv2

from document_select import perspective
from extractor import text_extract
from language_analyse import language_analyse

############################################
#               End                        #
############################################


class funcs:
    ############################################
    #         Functionalities for GUI          #
    ############################################

    """
    * It captures the new feed
    * Ask to save file
    """
    def new():
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            _, img = cap.read()
            key = cv2.waitKey(1)
            cv2.imshow("Capture", img)
            if key == 27:
                break
            elif key == 13:
                files = [('All Files', '*.*'),
                         ('PNG', '*.png'),
                         ('JPG', '*.jpg')]
                file = asksaveasfile(
                    mode='w', filetypes=files, defaultextension=files)  # Ask for saving file
                if file:
                    cv2.imwrite(file.name, img)
                break
        cap.release()
        cv2.destroAllWindows()

    """
    * Simply open a stored photo
    * Process opened image
    """
    def open():
        file = filedialog.askopenfile(title='Select A File', filetypes=(
            ('jpg', '*.jpg'), ('png', '*.png'),  ('All Files', '*.*')))
        funcs.processImg(file.name)

    """
    * Read Help Material
    * Display through messagebox
    """
    def help():
        string = str()
        with open("Resources\\help.txt", "r") as h:
            string = h.read()
        messagebox.showinfo("Help", string)

    """
    * Read Help Material
    * Display through messagebox
    """
    def about():
        string = str()
        with open("Resources\\about.txt", "r") as h:
            string = h.read()
        messagebox.showinfo("About", string)

    ################################
    # Image parsing for processing #
    ################################

    def processImg(imgSrc):
        
        def text_process(imgSrc):
            cv2.imwrite(imgSrc, scanned[0])

            """ Text is extracted from image here 
            And parsed to language analyser  """

            text = text_extract()
            actual_text = text.processing(imgSrc)                       ## Extracted Data
            correct_text = language_analyse(actual_text).getCorrect()   ## Corrected Form after process

            analysed_text = language_analyse(actual_text).getAnalysis() ## Analysed Errors after processing

            if actual_text == correct_text: ## Content with No Errors
                messagebox.showerror(
                    "Already Good", "Extracted Data don't need any corrections")
            else:
                messagebox.showinfo(
                    "Corrected Version", "Incorrect: "+actual_text+"\nCorrected: "+correct_text)
                analysis = str()
                for data in analysed_text:
                    analysis+=("Incorrect: "+str(data['text'])+"\nCorrect: "+str(data['correct'])+"\nDefinition: "+str(data['definition'])+'\n\n')
                messagebox.showinfo("Analysis Report",analysis)

        img = cv2.imread(imgSrc)
        img = cv2.resize(img, (0, 0), fx=1.2, fy=1.2)
        scanned = perspective(img).returnImg()      # Stored Image
        cv2.imshow("Output", scanned[0])
        if scanned[1]:      ## Checking for unprocessed image
            text_process(imgSrc)
            cv2.destroyAllWindows()
        else:
            choice = askyesno(title='Confirm Save',
                              message='Are you sure that you save?')
            if choice:
                files = [('All Files', '*.*'),
                         ('PNG', '*.png'),
                         ('JPG', '*.jpg')]
                file = asksaveasfile(
                    mode='w', filetypes=files, defaultextension=files)  # Ask for saving file
                if file:
                    text_process(file.name)
            else:
                cv2.destroyAllWindows()

    def processVideo():
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            _, img = cap.read()
            scanned = perspective(img).returnImg()      # Stored Image
            cv2.imshow("Output", scanned[0])
            key = cv2.waitKey(1)
            if key == 27:
                break
        cap.release()
        cv2.destroAllWindows()
