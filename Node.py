import math
import time

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

