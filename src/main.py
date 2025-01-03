from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(50, 50, 100, 100, win)
    cell1.has_bottom_wall = False
    cell1.draw()

    cell2 = Cell(50, 100, 100, 150, win)
    cell2.has_top_wall = False
    cell2.has_right_wall = False
    cell2.draw()

    cell3 = Cell(100, 100, 150, 150, win)
    cell3.has_left_wall = False
    cell3.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell2, undo=True)

    win.wait_for_close()

if __name__ == "__main__":
    main()