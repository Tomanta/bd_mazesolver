from time import sleep
from cell import Cell
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for x in range(self._num_cols):
            new_col = []
            for y in range(self._num_rows):
                new_cell = Cell(self._win)
                new_col.append(new_cell)
            self._cells.append(new_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _reset_cells_visited(self):
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._cells[x][y].visited = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i-1,j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i+1,j))
            # up
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i,j-1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i,j+1))

            if len(possible_directions) == 0:
                self._draw_cell(i,j)
                return

            # Pick a random direction
            direction = random.randrange(0,len(possible_directions))
            chosen_direction = possible_directions[direction]
            
            # Knock out the walls
            # right
            if chosen_direction[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # left
            if chosen_direction[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # down
            if chosen_direction[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            # top
            if chosen_direction[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            self._break_walls_r(chosen_direction[0], chosen_direction[1])

                    

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1, self._num_rows - 1)
    
    def _animate(self):
        self._win.redraw()
        sleep(0.05)

    def solve(self):
        return self._solve_r(0, 0)
    
    def _cell_exists(self, i, j):
        if i < 0 or j < 0:
            return False
        if i > self._num_cols-1 or j > self._num_rows-1:
            return False
        
        return True

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        if i == self._num_cols -1 and j == self._num_rows -1:
            return True
        
        # left
        if self._cell_exists(i-1,j) and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            result = self._solve_r(i-1, j)
            if result:
                return result
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        # right
        if self._cell_exists(i+1,j) and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            result = self._solve_r(i+1, j)
            if result:
                return result
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)

        # up
        if self._cell_exists(i,j-1) and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            result = self._solve_r(i, j-1)
            if result:
                return result                
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        # down
        if self._cell_exists(i,j+1) and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            result = self._solve_r(i, j+1)
            if result:
                return result
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

        return False
