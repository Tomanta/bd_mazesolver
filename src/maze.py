from time import sleep
from cell import Cell

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = None
        self._create_cells()
        pass

    def _create_cells(self):
        self._cells = []
        for x in range(self._num_cols):
            new_row = []
            for y in range(self._num_rows):
                new_cell = Cell(self._win)
                new_row.append(new_cell)
            self._cells.append(new_row)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells)):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = i * self._cell_size_x
        y1 = j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
