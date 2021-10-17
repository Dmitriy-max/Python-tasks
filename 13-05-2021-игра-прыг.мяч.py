from tkinter import *
import time
import random
root = Tk()
root.title("Игра")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0,
canvas = Canvas(width=400, height=400)
canvas.pack()