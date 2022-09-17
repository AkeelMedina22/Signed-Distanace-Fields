import numpy as np
import matplotlib.pyplot as plt
from Light import Light
from Sphere import Sphere

background = [0.0, 0.0, 0.0]

width = 800
height = 800

# max_depth = 1

camera = np.array([0, 0, 1])
ratio = float(width) / height
screen = (-1, 1 / ratio, 1, -1 / ratio) # left, top, right, bottom

light = Light(position=np.array([5, 5, 5]), ambient=np.array([1, 1, 1]), diffuse=np.array([1, 1, 1]), specular=np.array([1, 1, 1]))

objects = [Sphere(center=np.array([-0.2, 0, -1]), radius=0.7, ambient=np.array([0.5, 0.5, 0.5]), diffuse=np.array([0.7, 0, 0]), specular=np.array([1, 1, 1]), shininess=100, reflection=0.5),
           Sphere(center=np.array([0.1, 0.3, 0]), radius=0.3, ambient=np.array([0.8, 0.2, 0.0]), diffuse=np.array([0.7, 0, 0]), specular=np.array([1, 1, 1]), shininess=100, reflection=0.5),
           Sphere(center=np.array([-0.3, 0, 0]), radius=0.2, ambient=np.array([0.1, 0.2, 0.8]), diffuse=np.array([0.7, 0, 0]), specular=np.array([1, 1, 1]), shininess=100, reflection=0.5)]

radius = [i.radius for i in objects]
centers = [i.center for i in objects]

def normalize(vector):
    return vector / np.linalg.norm(vector)

def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis

def sphere_sdf(p, r):
    return np.linalg.norm(p) - r

# def ray_march(pos, raydir):

#     details = []

#     for i in objects:
#         temp_pos = pos
#         step = 0
#         r = i.radius
#         d = sphere_sdf(i.center-temp_pos, r)

#         while (abs(d) > 0.001 and step < 50):
#             temp_pos = temp_pos + raydir*d
#             d = sphere_sdf(i.center-temp_pos, r)
#             step += 1
        
#         details.append([step<50, temp_pos, d, i])

#     for i in details:

#         if i[0] == True:
#             return i[1:]

#     return False

def ray_march(pos, raydir):

    step = 0
    index = 0
    d = [sphere_sdf(centers[i]-pos, radius[i]) for i in range(len(objects))]

    while not any([False if abs(i) > 0.0005 else True for i in d]) and step < 80:

        index = np.argmin(d)
        pos = pos + raydir*d[index]
        d = [sphere_sdf(centers[i]-pos, radius[i]) for i in range(len(objects))]
        step += 1

    index = np.argmin(d)

    if step < 80:
        return [pos, d[index], objects[index]]

    return False


image = np.zeros((height, width, 3))
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):

        # screen is on origin
        pixel = np.array([x, y, 0])
        origin = camera

        color = np.array(background)

        # check sdf
        direction = normalize(pixel - origin)
        sdf_result = ray_march(origin, direction)

        if sdf_result:
            color = sdf_result[2].ambient

            
        image[i, j] = color

    print("%d/%d" % (i + 1, height))

plt.imsave('image3.png', image)
print("Image Saved!")






# objects = [
#     { 'center': np.array([-0.2, 0, -1]), 'radius': 0.7, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
#     { 'center': np.array([0.1, -0.3, 0]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0.1]), 'diffuse': np.array([0.7, 0, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
#     { 'center': np.array([-0.3, 0, 0]), 'radius': 0.15, 'ambient': np.array([0, 0.1, 0]), 'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
#     { 'center': np.array([0, -9000, 0]), 'radius': 9000 - 0.7, 'ambient': np.array([0.1, 0.1, 0.1]), 'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 }
# ]