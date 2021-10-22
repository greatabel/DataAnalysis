class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None

    def init_grid(self, parent, end):
        self.parent = parent
        if parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 1
            
        self.h = abs(self.x - end.x) + abs(self.y - end.y)
        self.f = self.g + self.h

