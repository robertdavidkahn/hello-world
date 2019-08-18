import sys
sys.path.insert(0, "Shapes")

import clsShape

print("Hello, world")

aCircle1 = clsShape.Circle("c1")
aCircle2 = clsShape.Circle("c2")

aSquare1 = clsShape.Circle("sq1")

aList = [ aCircle1, aCircle2, aSquare1 ]

for item in aList:
    item.draw()
