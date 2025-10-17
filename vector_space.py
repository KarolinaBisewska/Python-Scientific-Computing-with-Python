class R2Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def norm(self):
        return (self.x**2 + self.y**2)**0.5
        
    def __str__(self):
        return f'{self.x, self.y}'

class R3Vector(R2Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

v1 = R2Vector(2, 3)
print(v1.norm())
print(v1)
v2 = R3Vector(2, 2, 3)
