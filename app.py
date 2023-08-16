import tkinter as tk
from tkinter import Tk, Button, Text, filedialog as fd 
from tkinter import ttk
from PIL import Image
from pytesseract import pytesseract
import os

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title("Scan Text Tool")
        
        self.btnSelectImage = Button(self.root, text="Select images", command=self.open_select_files_dialog)
        self.btnSelectImage.place(x=20, y=10)
        
        self.cbbPath = ttk.Combobox(self.root, values=(), width=50)
        self.cbbPath.place(x=120, y=15)

        self.extractedText = Text(self.root, width=70, height=20)
        self.extractedText.place(x=10, y=50)

        self.btnExtract = Button(self.root, text="Extract", command=self.extract_text)
        self.btnExtract.place(x=450,y=10)

        self.btnExport = Button(self.root, text="Export", command=self.export_to_excel)
        self.btnExport.place(x=500,y=10)

        self.selected_files = []
        self.root.mainloop()


    def open_select_files_dialog(self):
        file_types = (
            ("JPEG File", "*.jpg"),
            ("PNG File", "*.png")
        )
        files = fd.askopenfiles(filetypes=file_types)

        if files:
            paths = []
            for file in files:
                path = os.path.abspath(file.name)
                self.selected_files.append(path)
                paths.append(path)
            self.cbbPath['values'] = tuple(paths)

    def extract_text(self):
        if self.cbbPath.get():
            self.extractedText.delete(tk.END)
            img = Image.open(self.cbbPath.get())
            self.extractedText.insert(tk.END, pytesseract.image_to_string(img, lang='vie'))

    def export_to_excel(self):
        filetypes = (
            ("Excel File", "*.xlsx"),
            ("CSV File", "*.csv")
        )
        file = fd.asksaveasfile(filetypes=filetypes, initialfile="demo.csv")