import tkinter as TK
root = Tk()
canvas = Canvas( width = 500, height = 500)
canvas.pack()
mytriangle = canvas.create_polygon(10,10,10,60,50,35,fill='red')
root.mainloop()