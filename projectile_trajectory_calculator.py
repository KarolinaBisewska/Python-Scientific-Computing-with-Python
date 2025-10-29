import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    def __init__(self, speed, height, angle):
        self.__angle = math.radians(angle)
        self.__speed = speed
        self.__height = height
