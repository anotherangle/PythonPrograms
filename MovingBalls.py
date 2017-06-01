from Tkinter import *
from random import randint

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="#"+("%06x"%randint(0,16777215)))

    def move_ball(self):
        deltax = randint(0,5)
        deltay = randint(0,5)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

def callback(event):
    print "clicked at", event.x, event.y
    ball=Ball(canvas,event.x,event.y,event.x+30,event.y+30)
    ball.move_ball()
    

    
# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
root.overrideredirect(True)
rwidth=root.winfo_screenwidth()
rheight=root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(rwidth,rheight))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
canvas = Canvas(root, bg="black",width = rwidth, height = rheight)
canvas.bind("<Button-1>", callback)
#canvas.bind("<Key>", key)
canvas.pack()
root.mainloop()
