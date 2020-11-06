import functions.functions as functions
import os
from tkinter import filedialog
from tkinter import *

if __name__ == "__main__":
    settings = functions.import_settings()
    # print(settings['source_directory'])
    source = settings['source_directory']

    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    for subdir, dirs, files in os.walk(source):
        for filename in files:
            filepath: str = subdir + os.sep + filename

            if filepath.endswith('.boxnote'):
                # print(filepath)
                functions.convert_boxnote(filepath)
