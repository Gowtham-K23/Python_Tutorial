class Point:

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()

point1.move()
point1.draw()

point2 = Point()
point2.x = 10
print(point2.x)
