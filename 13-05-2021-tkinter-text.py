from tkinter import *
root = Tk()
canvas = Canvas (width = 500, height = 500 )
canvas.pack()
canvas.create_text(100,100, text = 'Привет!',font=('Times',20),fill='red')
root.mainloop() #-font шрифт,указівается в пунктах 20, и в пикселях -20