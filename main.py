import functions.functions as functions
import os

if __name__ == "__main__":
    settings = functions.import_settings()
    print(settings['source_directory'])
    s = settings['source_directory']
    d = s + os.sep + 'converted'

    for subdir, dirs, files in os.walk(s):
        for filename in files:
            filepath = subdir + os.sep + filename
            dest_dir = subdir.replace(s, d)
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)

            print(dest_dir)
            if filepath.endswith('.boxnote'):
                # print(filepath)
                destination_file = filepath.replace(s, d)
                # print(destination_file)
                functions.convert_boxnote(filepath, destination_file)
