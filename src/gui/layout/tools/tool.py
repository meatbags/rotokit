import tkinter as tk

class Tool:
    def __init__(self, id, name, command):
        self.id = str(id)
        self.name = str(name)
        self.checkVar = tk.IntVar()
        self.command = command;

    def getRadioButton(self, root, var=None, row=0, column=0):
        self.radioButton = tk.Radiobutton(
            root,
            variable=var,
            value=self.id,
            text=self.name,
            command=self.onChange,
            width=10,
            indicatoron=False
        ).grid(row=row, column=column)

    def getCheckButton(self, root, row=0, column=0):
        self.checkButton = tk.Checkbutton(
            root,
            command=self.onChange,
            variable=self.checkVar,
            text=self.name,
            width=10,
            indicatoron=False
        ).grid(row=row, column=column)

    def onChange(self):
        # pass event up
        self.command(self)
