import json
import boxnotes2html


def import_settings():
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
    print(settings['source_directory'])


def get_filenames():
    pass


def convert_boxnote():
    pass
