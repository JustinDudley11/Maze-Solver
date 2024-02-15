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
        
class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, x2, y1, y2, win):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if self.has_left_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x1, self._y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x2, self._y1)
            line = Line(point1, point2)
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            point1 = Point(self._x2, self._y1)
            point2 = Point(self._x2, self._y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            point1 = Point(self._x1, self._y2)
            point2 = Point(self._x2, self._y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "black")
                    
def main():
    win = Window(800, 600)
    cell1 = Cell(True, False, True, False, 10, 90, 10, 90, win)
    cell1.draw()
    cell2 = Cell(True, True, True, True, 100, 180, 10, 90, win)
    cell2.draw()
    win.wait_for_close()
    
if __name__ == "__main__":
    main()        