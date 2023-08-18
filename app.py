from tkinter import Tk, Button, filedialog as fd 

class App():
    def __init__(self):
        self.app = Tk()
        self.app.geometry("600x400")
        self.app.title("Scan Text From Image Tool")
        
        btnSelectImage = Button(self.app, text="Select images", command=self.open_select_files_dialog)
        btnSelectImage.pack(side="left")
        self.app.mainloop()


    def open_select_files_dialog(event):
        file_types = (
            ("JPEG File", "*.jpg"),
            ("PNG File", "*.png")
        )

        file_dialog = fd.askopenfiles(filetypes=file_types)
