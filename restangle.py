class Restangle:
    def __init__(self, x, y, width, higth):
          self.x = x
          self.y = y
          self.width = width
          self.higth = higth
    def __str__(self):
          return print(str(f"Restangle{self.x, self.y, self.width, self.higth}"))

exz = Restangle(5, 10, 50, 100)
exz.__str__()

