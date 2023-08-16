import turtle as tr
import tkinter as tk
from Node import Node
import time

class Screen(tk.Tk):
    WIDTH = 500
    HEIGHT = 350
    def __init__(self):
        super().__init__()        
        self.title("Djikstra Algorithm")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.__setCanvas()

    def __setCanvas(self) -> None:
        self.__cv = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT, bg="#535353")
        self.__cv.pack(expand=True, fill='both')        

        self.__tr = tr.TurtleScreen(self.__cv)
        self.__tr.bgcolor("#535353")        

        self.__pen = tr.RawTurtle(self.__tr)
        self.__pen.hideturtle()
    
    def drawNode(self, node:Node) -> None:
        x, y = node.getPos()
        radius = 20
        self.__cv.create_oval(x - radius, y - radius, x + radius, y + radius, fill=node.color, outline=node.color)
        self.__cv.create_text(x, y, text=node.getID(), fill='black', font=('Helvetica', 10, 'bold'))
    
    def drawArist(self, nodes:dict[str:Node]) -> None:
        self.__pen.color("white")
        self.__tr.tracer(0,0)
        for i in nodes:
            for j in nodes[i].getChildren():                
                self.__pen.penup()
                x, y = nodes[i].getPos()
                self.__pen.goto(x,-1*y)
                self.__pen.pendown()
                x, y = nodes[j].getPos()
                self.__pen.goto(x, -1*y)
    
    def printTrack(self, id:(str | None), nodes:dict):
        if id is not None:
            self.__tr.tracer(1)
            self.__pen.speed(1)
            self.__pen.color("yellow")
            minTag = nodes[id].getMinTag()
            if minTag is not None: 
                self.__pen.pendown()
                x, y = nodes[id].getPos()
                self.__pen.goto(x,-1*y)
                self.printTrack(minTag[1], nodes)
            return 
        return 

    def posPenNode(self, cor:tuple):
        x, y = cor
        self.__tr.tracer(0)
        self.__pen.penup()
        self.__pen.goto(x,-1*y)

