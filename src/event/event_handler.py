from src.event.mouse import Mouse

class EventHandler:
    def __init__(self, *roots):
        self.roots = [root for root in roots]
        self.keys = {}
        self.mouse = Mouse()

    def bindMouseDown(self, event):
        for root in self.roots:
            root.bind('<Button-1>', lambda e: (self.onMouseDown(e), event(e)))

    def bindMouseRelease(self, event):
        for root in self.roots:
            root.bind('<ButtonRelease-1>', lambda e: (self.onMouseRelease(e), event(e)))

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

    def onMouseDown(self, event):
        self.mouse.down = True
        self.mouse.x = event.x
        self.mouse.y = event.y

    def onMouseRelease(self, event):
        self.mouse.down = False
        self.mouse.x = event.x
        self.mouse.y = event.y

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
