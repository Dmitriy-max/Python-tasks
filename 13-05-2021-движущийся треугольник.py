from tkinter import *
import random
import time
root = Tk()
canvas = Canvas (width = 400, height = 400 )
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range (0,6):
    canvas.move(1, 50, 0)
    root.update()
    time.sleep(0.9)

for j in range (0,6):
    canvas.move(1, 0, 50)
    root.update()
    time.sleep(0.9)

for k in range (0,6):
    canvas.move(1,-50, 0)
    root.update()
    time.sleep(0.9)

for l in range (0,6):
    canvas.move(1, 0, -50)
    root.update()
    time.sleep(0.9)

root.mainloop()