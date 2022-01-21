import tkinter as tk

from controllers.Builder import Builder
from tkinter import filedialog

def run():

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(initialdir="./", title="Select data to be sorted",
                                                filetypes = (("text", "*.txt"), ("all files", "*.*")))
    result = Builder().run(file_path)

    Builder().finish(file_path, result)


run()



