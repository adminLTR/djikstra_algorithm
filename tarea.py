import tkinter as tk
import time
import random as rd
import math
import turtle as tr
import sys

class Node:
    def __init__(self, id:int, pos:tuple[float], children, color):
        self.__id = id
        self.__pos = pos
        self.__checked = False
        self.__children = []
        self.__tags = []        
        self.appendChildren(children)
        self.color = color

    def appendChildren(self, children:tuple[str]) -> None:
        for i in children:
            self.__children.append(i)

    def getChildren(self) -> list[str]:
        return self.__children
    
    def isChecked(self) -> bool:
        return self.__checked
    
    def check(self) -> None:
        self.__checked = True
    
    def unCheck(self) -> None:
        self.__checked = False

    def getPos(self) -> tuple[float]:
        return self.__pos

    def getDistance(self, pos2:tuple[float]) -> float:
        return math.sqrt(math.pow(self.__pos[0] - pos2[0], 2) + math.pow(self.__pos[1] - pos2[1], 2))
    
    def getID(self) -> str:
        return self.__id

    def getMinTag(self) -> tuple | None:
        try:
            minTag = self.__tags[0]
        except:
            return None    
        for tag in self.__tags:
            if tag[0] < minTag[0]:
                minTag = tag
        return minTag

    def appendTag(self, tag:tuple) -> None:
        self.__tags.append(tag)

    def __str__(self) -> str:
        return  " -> " + self.__id

class Matrix:
    def __init__(self, n):
        self.__m = []
        for i in range(n):
            x = []
            for j in range(n):
                x.append(rd.randint(0, 50))
            self.__m.append(x)
    
    def manually(self):
        for i in range(len(self.__m)):
            for j in range(len(self.__m)):
                self.__m[i][j] = int(input(f"Inserta numero [{i}][{j}]: "))
        

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


root = Screen()

n = int(input("Inserta N: "))
opc = -1
while opc<0 or opc>2:
    print("1. Llenar manualmente")
    print("2. Llenar aleatoriamente")
    print("0. Salir")

if opc!=0:
    matriz = Matrix(n)
    if opc==2:
        matriz.manually()
    
    while True:
        try:
            root.update()
        except:
            sys.exit()