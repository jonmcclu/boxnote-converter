import json
import os
from tkinter import *
from tkinter import filedialog
import boxnotes2html  # https://pypi.org/project/boxnotes2html/
from typing import Dict
from htmldocx import HtmlToDocx  # https://pypi.org/project/htmldocx/


def import_settings() -> Dict:
    """
    Function that imports the variables inside the 'settings.json' file. This allows users to change which directory
    houses their Box files.
    :return: Dictionary of the JSON settings
    """
    if not os.path.exists("../settings.json"):
        settings_dict = {}
        root = Tk()
        root.withdraw()
        settings_dict["source_directory"] = filedialog.askdirectory()
    else:
        with open('../settings.json') as settings_file:
            settings_dict = json.load(settings_file)
    return settings_dict


def convert_boxnote(source_file: str) -> None:
    """
    Function that converts the input file into an HTML formatted file and _then_ into a Word document. The initial
    .boxnote file and HTML file are deleted upon successful conversation to a Word Document.
    :param source_file:
    :return: None
    """
    note = boxnotes2html.BoxNote.from_file(source_file)
    try:
        html_file = source_file.replace('.boxnote', '.html')
        docx_file = source_file.replace('.boxnote', '')
        html = note.as_html()
        html_rework = html.replace('<style>body {\n    font-family: Sans-Serif;\n}\n', '')
        with open(html_file, 'w') as file:
            file.write(html_rework)

        new_parser = HtmlToDocx()
        new_parser.parse_html_file(html_file, docx_file)

        os.remove(source_file)
        os.remove(html_file)

        convert_log(f'Normal:  Converted {source_file} to a Word document.')

    except (KeyError, TypeError, UnicodeEncodeError) as error:
        convert_log(f'FATAL ERROR:  {source_file} {error}')


def convert_log(entry: str) -> None:
    with open('../converter.log', 'a') as log:
        log.write(f'{entry}\n')
