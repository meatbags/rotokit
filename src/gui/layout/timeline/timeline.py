import Tkinter as tk
from src.gui.layout.timeline.timeline_frame import TimelineFrame
from src.config import Config

class Timeline(tk.Frame):
    def __init__(self, root, command, **kw):
        tk.Frame.__init__(self, root, borderwidth=4, relief=tk.SUNKEN, **kw)
        self.pack(fill=tk.X, side=tk.TOP)
        self.command = command

        # frames
        self.toolbar = tk.Frame(self, borderwidth=4, relief=tk.SUNKEN)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        self.timeline = tk.Frame(self, borderwidth=4, relief=tk.SUNKEN)
        self.timeline.pack(side=tk.TOP, fill=tk.X)

        # tools
        self.createTools()

    def createTools(self):
        self.tempTool = tk.Checkbutton(self.toolbar, text='Swap Mode', indicatoron=0)
        self.tempTool.pack(side=tk.LEFT)

    def addFrames(self, frames):
        self.frames = [TimelineFrame(self.timeline, frame.id, self.onTimelineChange) for frame in frames]

    def setActiveFrames(self, frames):
        ids = [frame.id for frame in frames]

        for frame in self.frames:
            if frame.id in ids:
                frame.active.set(1)
            else:
                frame.active.set(0)

    def onTimelineChange(self, frame):
        self.command(frame)
