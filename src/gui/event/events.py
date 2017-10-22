class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.down = False
        self.over = False

class Events:
    def __init__(self, *roots):
        self.roots = [root for root in roots]
        self.keys = {}
        self.mouse = Mouse()

    def bindMouseDown(self, event):
        for root in self.roots:
            root.bind('<Button-1>', lambda e: (self.onMouseDown(), event(e)))

    def bindMouseRelease(self, event):
        for root in self.roots:
            root.bind('<ButtonRelease-1>', lambda e: (self.onMouseRelease(), event(e)))

    def bindMouseMove(self, event):
        for root in self.roots:
            root.bind('<B1-Motion>', lambda e: (self.onMouseMove(e), event(e)))

    def bindMouseEnter(self, event):
        for root in self.roots:
            root.bind('<Enter>', lambda e: (self.onMouseEnter(), event(e)))

    def bindMouseLeave(self, event):
        for root in self.roots:
            root.bind('<Leave>', lambda e: (self.onMouseLeave(), event(e)))

    def bindKeyDown(self, event):
        for root in self.roots:
            root.bind('<Key>', lambda e: (self.onKeyDown(e), event(e)))

    def bindKeyRelease(self, event):
        for root in self.roots:
            root.bind('<KeyRelease>', lambda e: (self.onKeyRelease(e), event(e)))

    def onMouseDown(self):
        self.mouse.down = True

    def onMouseRelease(self):
        self.mouse.down = False

    def onMouseMove(self, event):
        self.mouse.x = event.x
        self.mouse.y = event.y

    def onMouseEnter(self):
        self.mouse.over = True

    def onMouseLeave(self):
        self.mouse.over = False

    def onKeyDown(self, event):
        self.keys[event.keysym] = True

    def onKeyRelease(self, event):
        self.keys[event.keysym] = False
