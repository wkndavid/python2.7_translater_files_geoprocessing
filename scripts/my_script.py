# -*- coding: utf-8 -*-

import codecs
import tkinter as tk
from tkinter import filedialog


def open_file_dialog():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="teste1", filetypes=[("DBF files", "*.dbf")])

    return file_path

def main():
    # Open file dialog to choose DBF file
    dbf_file_path = open_file_dialog()

    if not dbf_file_path:
        print("No file selected. Exiting.")
        return

    # Open the DBF file using 'with' statement
    with codecs.open(dbf_file_path, encoding='utf-8') as file:
        # Read the content of the file
        data = file.read()

    # Convert the content to uppercase
    data = data.upper()

    # Print the result
    print(data)

if __name__ == "__main__":
    main()
