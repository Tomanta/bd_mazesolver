from graphics import Point, Line

class Cell():
    def __init__(self, x1: int, y1: int, x2: int, y2: int, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall, fill_color="black")
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, fill_color="black")
        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall, fill_color="black")
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall, fill_color="black")

    def get_center(self):
        return Point(self._x1 + (self._x2 - self._x1) // 2, self._y1 + (self._y2 - self._y1) // 2)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        
        self._win.draw_line(Line(self.get_center(), to_cell.get_center()), fill_color=fill_color)
