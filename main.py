import tkinter as tk
from tkinter import messagebox
# from pymouse import PyMouse

# m = PyMouse()
# m.click(x,y)

class Gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def action(self):
        self.status = not self.status
        
        if self.status:
            self.action.config(text="Desativar")
            self.label_status.config(text="ON", fg="white", bg="green")
        else:
            self.action.config(text="Ativar")
            self.label_status.config(text="OFF", fg="white", bg="red")

    def create_widgets(self):
        self.status = False
        self.label_active = tk.Label(self, text="BOT")
        self.label_active.pack(side="top")

        if self.status:
            self.label_status = tk.Label(self, text="ON", fg="white", bg="green")
        else:
            self.label_status = tk.Label(self, text="OFF", fg="white", bg="red")
        self.label_status.pack(side="top")

        self.action = tk.Button(self, text="Desativar", command=self.action)
        self.action.pack(side="bottom")

root = tk.Tk()
root.title("BOT")
root.geometry("150x100")
app = Gui(master=root)
app.mainloop()