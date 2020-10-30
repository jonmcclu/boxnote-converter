import json
import boxnotes2html  # https://pypi.org/project/boxnotes2html/
from htmldocx import HtmlToDocx  # https://pypi.org/project/htmldocx/


def import_settings():
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
    return settings


def get_filenames():
    pass


def convert_boxnote(filename, destination):
    note = boxnotes2html.BoxNote.from_file(filename)
    try:
        html_file = destination.replace('.boxnote', '.html')
        docx_file = destination.replace('.boxnote', '')
        html = note.as_html()
        # print(html)
        html_rework = html.replace('<style>body {\n    font-family: Sans-Serif;\n}\n', '')
        with open(html_file, 'w') as file:
            file.write(html_rework)

        new_parser = HtmlToDocx()
        new_parser.parse_html_file(html_file, docx_file)
    except KeyError as error:
        print(f'KeyError:  {filename}')
