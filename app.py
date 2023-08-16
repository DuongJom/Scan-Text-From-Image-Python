from tkinter import Tk, Button, Text, filedialog as fd 
from tkinter import ttk
import os

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
        for file in self.selected_files:
            path = file.name
