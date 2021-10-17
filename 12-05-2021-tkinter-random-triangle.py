from tkinter import *
import random
root = Tk()
canvas = Canvas (width = 400, height = 400 )
canvas.pack()
def random_triangel (width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(width)
    y2 = random.randrange(height)
    z1 = random.randrange(width)
    z2 = random.randrange(height)
    de=("%02x"%random.randint(0,255))
    re=("%02x"%random.randint(0,255))
    we=("%02x"%random.randint(0,255))
    ge="#"
    color=ge+de+re+we
    canvas.create_polygon(x1,y1,x2,y2,z1,z2, fill = color)
for x in range (0,10):
        random_triangel(400,400)
root.mainloop()

