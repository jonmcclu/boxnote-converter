import json
import os
import boxnotes2html  # https://pypi.org/project/boxnotes2html/
from typing import Dict
from htmldocx import HtmlToDocx  # https://pypi.org/project/htmldocx/


def import_settings() -> Dict:
    """
    Function that imports the variables inside the 'settings.json' file. This allows users to change which directory
    houses their Box files.
    :return: Dictionary of the JSON settings
    """
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
    return settings


def convert_boxnote(filename: str) -> None:
    """
    Function that converts the input file into an HTML formatted file and _then_ into a Word document. The initial
    .boxnote file and HTML file are deleted upon successful conversation to a Word Document.
    :param filename:
    :return: None
    """
    note = boxnotes2html.BoxNote.from_file(filename)
    try:
        html_file = filename.replace('.boxnote', '.html')
        docx_file = filename.replace('.boxnote', '')
        html = note.as_html()
        html_rework = html.replace('<style>body {\n    font-family: Sans-Serif;\n}\n', '')
        with open(html_file, 'w') as file:
            file.write(html_rework)

        new_parser = HtmlToDocx()
        new_parser.parse_html_file(html_file, docx_file)

        os.remove(filename)
        os.remove(html_file)

        convert_log(f'Normal:  Converted {filename} to a Word document.')

    except (KeyError, TypeError) as error:
        convert_log(f'FATAL ERROR:  {filename} {error}')


def convert_log(entry: str) -> None:
    with open('converter.log', 'a') as log:
        log.write(f'{entry}\n')
