# Notes for Building the Executables

### Using Pyinstaller

- The executables won't work without the underlying `boxnotes2html` package directory being added to the build files.
- Using the following in the Python script will show where the package directory is located 
  `print(boxnotes2html.__file__)`

pyinstaller --windowed --add-data="C:\Users\Jonas\.virtualenvs\boxnote-converter-2EEu4ZAb\lib\site-packages\boxnotes2html:boxnotes2html" --onefile exe-builder.py