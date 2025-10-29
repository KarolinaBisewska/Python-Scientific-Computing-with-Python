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
        
    def __calculate_displacement(self):
        v = self.__speed
        θ = self.__angle
        h = self.__height
        g = GRAVITATIONAL_ACCELERATION

        v_sin = v * math.sin(θ)
        v2_sin2 = (v ** 2) * (math.sin(θ) ** 2)
        inner_sqrt = math.sqrt(v2_sin2 + 2 * g * h)
        time_factor = v_sin + inner_sqrt
        d = v * math.cos(θ) * time_factor / g
        return d
