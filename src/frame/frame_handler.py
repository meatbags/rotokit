from src.frame.frame import Frame
from src.config import Config

class FrameHandler:
    def __init__(self):
        self.frames = []
        self.activeFrame = None
        self.activeFrameIndex = None
        self.activeFrames = []
        self.activeIndex = []
        self.size = Config['Canvas']['DefaultSize']

    def addFrame(self, *names):
        # add frames
        for name in names:
            self.frames.append(Frame(name, self.size))

        if len(self.activeIndex) == 0:
            self.activeIndex.append(0)
            self.activateFrames()

    def activateFrames(self):
        # create list of ordered active frames
        self.activeFrames = []

        for i in range(len(self.frames)):
            if i in self.activeIndex:
                self.activeFrames.append(self.frames[i])

    def setActiveFrame(self, index):
        if len(self.activeFrames) > index:
            self.activeFrame = self.activeFrames[index]
            self.activeFrameIndex = index

    def parseToolPath(self, toolPath):
        if self.activeFrame:
            self.activeFrame.parseToolPath(toolPath)

    def toggleFrame(self, timelineFrame, maxActive):
        # add or remove frame from active frames
        index = 0
        for i in range(len(self.frames)):
            if self.frames[i].id == timelineFrame.id:
                index = i
                break

        # check if active
        if index in self.activeIndex:
            self.activeIndex.remove(index)
        else:
            self.activeIndex.insert(0, index)

        # clip
        self.activeIndex = self.activeIndex[:maxActive]
        self.activateFrames()
        print(self.activeIndex)
