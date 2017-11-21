import Tkinter as tk
from src.config import Config

class TimelineFrame(tk.Frame):
    def __init__(self, root, id, command, **kw):
        tk.Frame.__init__(self, root, borderwidth=4, relief=tk.SUNKEN, **kw)
        self.pack(side=tk.LEFT)
        self.id = str(id)
        self.command = command

        # vars
        self.active = tk.IntVar()

        # button
        self.button = tk.Checkbutton(self, variable=self.active, command=self.onChange, text=id, padx=8, pady=8, indicatoron=0)
        self.button.pack()

    def onChange(self):
        self.command(self)
