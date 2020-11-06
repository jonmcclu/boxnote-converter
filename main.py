import functions.functions as functions
import os
from tkinter import messagebox
from tkinter import *

if __name__ == "__main__":
    settings = functions.import_settings()
    source = settings['source_directory']

    root = Tk()
    root.withdraw()

    for subdir, dirs, files in os.walk(source):
        for filename in files:
            filepath: str = subdir + os.sep + filename

            if filepath.endswith('.boxnote'):
                # print(filepath)
                functions.convert_boxnote(filepath)

    messagebox.showinfo("Completed", "The process has finished. Please check the converter.log file.")
