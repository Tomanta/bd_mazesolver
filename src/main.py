from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close) # Attach the self.close() method to deleting the window
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

        

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()