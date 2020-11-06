# Convert Boxnote

Python script to convert Box's proprietary note format (.boxnote) into either HTML or Word Documents (.docx).

### Requirements

- Python 3.8+
- Pipenv
  - Installation instructions @ https://docs.pipenv.org/install/#installing-pipenv
  - Windows machines will need Python & Pip set in PATH. This can be done automatically by selecting an option like
  "include Python in PATH" when installing Python.

### Update

- The script now converts the `.boxnote` files in-place. Meaning that the `.boxnote` files will be removed from the
source directory after being converted into Word Documents.
  
### Formatting Issues

This script relies on the Python package `boxnotes2html`. Please refer to their webpage 
(https://pypi.org/project/boxnotes2html/) for up-to-date issues.

- Images are not included
- Tables will be converted to plain text
- Lists will only be converted to asterisks or numbers, depending on the type of list.

### Using the Script

- download your Box files to your computer
- change the source directory path in settings.json to where your Box files are located.
  - Windows machines will need to use double backslashes in the filenames. For example:
    - Good:  `C:\\Users\\Jonas\\Downloads\\2020-09-23-wss-boxmigration-backup`
    - Bad:  `C:\Users\Jonas\Downloads\2020-09-23-wss-boxmigration-backup`
- open a terminal in the repository's directory
- (first time use) ```pipenv install```
- ```pipenv run python main.py```