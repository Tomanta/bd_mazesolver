from graphics import Point, Line

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
        self.visited = False
    
    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        
        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        right_wall = Line(top_right, bottom_right)
        bottom_wall = Line(bottom_left, bottom_right)

        if self.has_left_wall:
            self._win.draw_line(left_wall, fill_color="black")
        else:
            self._win.draw_line(left_wall, fill_color="white")
        if self.has_top_wall:
            self._win.draw_line(top_wall, fill_color="black")
        else:
            self._win.draw_line(top_wall, fill_color="white")
        if self.has_right_wall:
            self._win.draw_line(right_wall, fill_color="black")
        else:
            self._win.draw_line(right_wall, fill_color="white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, fill_color="black")
        else:
            self._win.draw_line(bottom_wall, fill_color="white")

    def get_center(self):
        return Point(self._x1 + (self._x2 - self._x1) // 2, self._y1 + (self._y2 - self._y1) // 2)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        
        self._win.draw_line(Line(self.get_center(), to_cell.get_center()), fill_color=fill_color)
