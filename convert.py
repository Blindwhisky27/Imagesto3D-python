import numpy as np
from PIL import Image
from stl import mesh


def convert(images):
    max_size = (1000, 1000)
    max_height = 10
    im = Image.open(images).convert('L')
    im.thumbnail(max_size)
    image_np = np.array(im)
    max_pix = image_np.max()

    (cols, rows) = im.size
    vertices = np.zeros((rows, cols, 3))

    for x in range(cols):
        for y in range(rows):
            pixel_intensity = image_np[y][x]
            z = pixel_intensity * max_height / max_pix
            vertices[y][x] = (x, y, z)
    faces = []
    for x in range(cols - 1):
        for y in range(rows - 1):
            vertices1 = vertices[y][x]
            vertices2 = vertices[y + 1][x]
            vertices3 = vertices[y + 1][x + 1]
            face1 = np.array([vertices1, vertices2, vertices3])
            faces.append(face1)

            vertices1 = vertices[y][x]
            vertices2 = vertices[y][x + 1]
            vertices3 = vertices[y + 1][x + 1]

            face2 = np.array([vertices1, vertices2, vertices3])
            faces.append(face2)
    face_mp = np.array(faces)

    surface = mesh.Mesh(np.zeros(face_mp.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            surface.vectors[i][j] = face_mp[i][j]

    print("Images converted")
    print("Model saved as STL in " + "car models/car.stl")
    surface.save("car models/car.stl")
