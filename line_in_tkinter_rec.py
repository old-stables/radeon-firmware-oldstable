from tkinter import Tk, Canvas, Frame
from math import sin, cos, pi
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем линии... много")
        self.pack()

        def gen_line(c, x, y, l, alfa):
            x1 = x + l * cos(alfa)
            y1 = y + l * sin(alfa)
            c.create_line(int(x), int(y), int(x1), int(y1))
            if l > 10:
                gen_line(c, x1, y1, 0.9 * l, alfa + pi / 6) 
   
        canvas = Canvas(self, width=1000, height=1000)
        gen_line(canvas, 600, 500, 40, 1)
 
        canvas.pack()
 
 
def main():
    root = Tk()
    ex = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
