import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __str__(self):
        return f'''
Projectile details:
speed: {self.__speed} m/s
height: {self.__height} m
angle: {round(math.degrees(self.__angle))}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
    
        v0 = self.__speed
        y0 = self.__height
        θ = self.__angle
        g = GRAVITATIONAL_ACCELERATION

        term1 = y0
        term2 = x * math.tan(θ)
        term3 = (g * x**2) / (2 * v0**2 * math.cos(θ)**2)

        return term1 + term2 - term3


ball = Projectile(10, 3, 45)
print(ball)
   
