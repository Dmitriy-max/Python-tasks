import turtle
t=turtle.Pen()
def myfigure (size,failled):
    if failled == True:
        t.begin_fill()
    for x in range (1,9):
        t.forward(size)
        t.left(45)
    if failled == True:
        t.end_fill()
t.color(0.9,0.75,0)
myfigure(50,True)
t.color(0,0,0)
myfigure(50,True)