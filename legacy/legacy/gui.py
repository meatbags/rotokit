from tkinter import *
from gui_config import *

class App(Frame):

  def __init__(self, master):
    super().__init__(master)

    self.var = 3;

    self.pack()
    self.createWidgets(master)

    master.bind('<Key-Control_L>', self.log)
    master.bind('<Key-Control_R>', self.log)
    master.bind('<Key-Escape>', self.log)

  def createWidgets(self, root):
    self.toolbar = Frame(self, bg=Config['colour']['white'])
    self.toolbar.pack(side=LEFT, fill=Y)

    self.label = Label(self.toolbar, text='toolbar')
    self.label.grid(row=0, column=0, sticky=NW, pady=2, padx=2)

    Radiobutton(self.toolbar, text='tool', variable=self.var, value=3).grid(padx=2, pady=2, row=9, column=0, sticky=NW)

    self.canvas = Canvas(self, width=800, height=600, relief=RAISED, borderwidth=5)
    self.canvas.pack(side=RIGHT)

    self.menu = Menu(root)
    self.fileMenu = Menu(self.menu, tearoff=0)
    self.fileMenu.add_command(label='New', command=self.log)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label='Exit', command=root.quit)

    self.menu.add_cascade(label='File', menu=self.fileMenu)

    root.config(menu=self.menu)

  def log(self, key):
    print(key)

  def getMenu(self):
    return self.menu;

root = Tk()
root.title('Title')
app = App(root)
#root.config(menu=app.getMenu())
root.mainloop()
