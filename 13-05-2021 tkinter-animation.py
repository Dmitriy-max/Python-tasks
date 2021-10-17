from tkinter import *
import time
root = Tk()
canvas = Canvas (width = 500, height = 500 )
canvas.pack()
my_image = PhotoImage(file='C:\\Users\\Лариса\\Desktop\\8cd055e77d5df0fe0bdb229b0d7bb9ff.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
for x in range (0,6):
    canvas.move(1, 20, 0)
    root.update()
    time.sleep(0.9)
root.mainloop() - # tkinter работает только с GIF-форматом аргумент anchor=NW означает, что изображение должно выводиться с левого верхнего угла (иначе за отправную точку считался бы центр изображения)