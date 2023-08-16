from screen import Screen
from Node import Node

nodes = {
    'A' : Node('A', (-211, -100), ('B', 'C', 'H'), "#FDFA53"),
    'B' : Node('B', (100, -59), ('A', 'C', 'D', 'E'), "white"),
    'C' : Node('C', (-10, 130), ('A', 'B', 'D', 'F'), "#74FD53"),
    'D' : Node('D', (220, -100), ('B', 'C', 'E', 'F', 'G'), "#D853FD"),
    'E' : Node('E', (200, 120), ('B', 'D','H'), "#FB6666"),
    'F' : Node('F', (-210, 120), ('C', 'D','G'), "#66ABFB"),
    'G' : Node('G', (150, 60), ('F', 'D', 'H'), "#66FBC8"),
    'H' : Node('H', (-56, 0), ('A', 'E', 'G'), "#FD7153"),
}

root = Screen()

root.drawArist(nodes)

for i in nodes:
    root.drawNode(nodes[i])


init = input("Initial: ").upper()[0]
nodes[init].appendTag((0, None))
cola = [init]

def setTrack(check):
    if len(cola) <= 0:
        return
    try:
        if cola.index(check) != 0:
            return
    except:
        return
    cola.remove(check)
    nodes[check].check()
    for child in nodes[check].getChildren():
        if not nodes[child].isChecked():
            d = nodes[child].getDistance(nodes[check].getPos())
            nodes[child].appendTag((d + nodes[check].getMinTag()[0], check))
            if child not in cola:
                cola.append(child)
    for child in nodes[check].getChildren():
        setTrack(child)

final = input("Final: ").upper()[0]
setTrack(init)
root.posPenNode(nodes[final].getPos())
root.printTrack(final, nodes)

root.mainloop()