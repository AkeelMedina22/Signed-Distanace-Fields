import numpy as np

class Sphere:

    def __init__(self, center=np.array([0,0,0]), radius=0, ambient=np.array([0,0,0]), diffuse=np.array([0,0,0]), specular=np.array([0,0,0]), shininess=0, reflection=0):
        self.center=center
        self.radius=radius
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
        self.shininess=shininess
        self.reflection=reflection