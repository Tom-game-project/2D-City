import tkinter

from pip import main


root = tkinter.Tk()
root.geometry("600x600")


root.title("hello world")

def loop_start(e):
    print("hello world")
    canvas.after(0,loop)


def loop():

    canvas.after(10,loop)

def loop2():
    canvas.after(10,loop2)



canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()

canvas.create_rectangle(10,10,100,100,fill="red",tags="red_rect")
canvas.tag_bind("red_rect","<Button-1>",loop_start)



root.mainloop()
