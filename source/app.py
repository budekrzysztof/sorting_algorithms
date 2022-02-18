import tkinter as tk
from controllers.Builder import Builder
from tkinter import filedialog

from utility.Utils import Utils

def run():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="./", title="Select data to be sorted",
                                                filetypes = (("text", "*.txt"), ("all files", "*.*")))
    result = Builder().run(file_path)
    Builder().finish(file_path, result)

if __name__ == "__main__":
    # Utils().generate_random_numbers_to_file('numbers.txt', 0, 10000, 10000)
    run()

