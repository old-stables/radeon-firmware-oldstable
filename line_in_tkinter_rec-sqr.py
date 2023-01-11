from tkinter import Tk, Canvas, Frame
from math import sin, cos, pi, radians, degrees
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем линии... много")
        self.pack()

        def gen_line(c, x, y, l, alfa = 0):
            x1 = x + l * cos(alfa)
            y1 = y + l * sin(alfa)

            c.create_line(int(x), int(y),int(x1), int(y1))
           
            if degrees(alfa) < 300:
                gen_line(c, x1, y1, l, alfa + pi / 2)
            else:
                if l > 20:
                    alfa = 0
                    gen_line(c, x1 + l/2, y1, l/2, alfa + pi / 2)
                
   
        canvas = Canvas(self, width=1000, height=1000)
        gen_line(canvas, 600, 500, 90, 0)
        canvas.pack()
 
 
def main():
    root = Tk()
    ex = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
