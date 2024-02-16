from tkinter import Tk, BOTH, Canvas
import time

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
        
class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, x2, y1, y2, win=None):
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
            
    def draw_move(self, to_cell, undo=False):
        if not undo:
            point1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
            point2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
            line = Line(point1, point2)
            self._win.draw_line(line, "red")
        elif undo:
            point1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
            point2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
            line = Line(point1, point2)
            self._win.draw_line(line, "gray")
            
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            cell_rows = []
            for j in range(self.num_cols):
                new_cell = Cell(True, False, False, True, self._x1 + i * self.cell_size_x, (self._x1 + i * self.cell_size_x) + self.cell_size_x, self._y1 + j * self.cell_size_y, (self._y1 + j * self.cell_size_y) + self.cell_size_y, self._win)
                cell_rows.append(new_cell)
            self._cells.append(cell_rows)
            for cell in cell_rows:
                self._draw_cells(cell)
        
    def _draw_cells(self, cell):
        cell.draw()
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
        
        
        
        
                    
def main():
    win = Window(800, 600)
    x1, y1 = 10, 10
    num_rows, num_cols = 8, 8
    cell_size_x, cell_size_y = 50, 50
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()        