import numpy as np

class Light:

    def __init__(self, position=np.array([0,0,0]), ambient=np.array([0,0,0]), diffuse=np.array([0,0,0]), specular=np.array([0,0,0])):
        self.position=position
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular