from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.c = Canvas(self.__root, width=self.width, height=self.height)
        self.c.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def draw_line(self, line, fill_color):
        line.draw(self.c, fill_color)
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        self.__root.destroy()
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def draw(self, c, fill_color):
        c.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y , fill=fill_color, width=2
        )
        c.pack()
def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    point2 = Point(505, 505)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()
    
if __name__ == "__main__":
    main()        