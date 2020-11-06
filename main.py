import functions.functions as functions
import os

if __name__ == "__main__":
    settings = functions.import_settings()
    # print(settings['source_directory'])
    source = settings['source_directory']

    for subdir, dirs, files in os.walk(source):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith('.boxnote'):
                # print(filepath)
                functions.convert_boxnote(filepath)
