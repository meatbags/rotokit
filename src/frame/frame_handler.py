from src.frame.frame import Frame

class FrameHandler:
    def __init__(self):
        self.frames = []
        self.activeFrames = []
        self.activeIndex = [] # placeholder

    def addFrame(self, *names):
        # add frames
        for name in names:
            self.frames.append(Frame(name))

        if len(self.activeIndex) == 0:
            self.activeIndex.append(0)
            self.activateFrames()

    def activateFrames(self):
        # create list of ordered active frames
        self.activeFrames = []

        for i in range(len(self.frames)):
            if i in self.activeIndex:
                self.frames[i].activate()
                self.activeFrames.append(self.frames[i])
            else:
                self.frames[i].disable()

    def resetDraw(self):
        for frame in self.frames:
            frame.resetDraw()

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
