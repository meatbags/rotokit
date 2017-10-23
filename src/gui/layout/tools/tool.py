import tkinter as tk

class Tool:
    def __init__(self, id, name):
        self.id = str(id)
        self.name = str(name)
        self.checkVar = tk.IntVar()

    def getRadioButton(self, root, var=None, cmd=None, row=0, column=0):
        self.radioButton = tk.Radiobutton(
            root,
            command=cmd,
            variable=var,
            value=self.id,
            text=self.name,
            width=10,
            indicatoron=False
        ).grid(row=row, column=column)

    def getCheckButton(self, root, cmd=None, row=0, column=0):
        self.checkButton = tk.Checkbutton(
            root,
            command=cmd,
            variable=self.checkVar,
            text=self.name,
            width=10,
            indicatoron=False
        ).grid(row=row, column=column)
