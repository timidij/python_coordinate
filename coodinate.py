import math

class Line:
    def __init__(self, cor1, cor2):
        self.cor1 = cor1
        self.cor2 = cor2

    def gradient(self):
        return (self.cor2[1]-self.cor1[1])/(self.cor2[0]-self.cor1[0])


    def distance(self):
        return math.sqrt(((self.cor2[0]-self.cor1[0])**2)+(self.cor2[1]-self.cor1[1])**2)
dis = Line((3,5),(9,6))
print(f"the gradient is: { dis.gradient()}")
print(f"the distance between the two coordinate is :{dis.distance()}")
