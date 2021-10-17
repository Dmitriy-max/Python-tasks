from tkinter import *
root = Tk()
canvas = Canvas (width = 500, height = 500 )
canvas.pack()
my_image = PhotoImage(file='C:\\Users\\Лариса\\Desktop\\8cd055e77d5df0fe0bdb229b0d7bb9ff.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
root.mainloop()