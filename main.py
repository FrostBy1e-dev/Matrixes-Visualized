import matplotlib.pyplot as plt
from itertools import product, combinations
import numpy as np

# Define a function to draw a cube at position pos = [x, y, z]
def draw_cube(ax, pos, color):
    # Generate the vertices of the cube
    r = [-0.5 + pos[0], 0.5 + pos[0]]
    s = [-0.5 + pos[1], 0.5 + pos[1]]
    t = [-0.5 + pos[2], 0.5 + pos[2]]
    vertices = list(product(r, s, t))
    # Generate the edges of the cube
    edges = [
        (vertices[0], vertices[1]), (vertices[1], vertices[3]), (vertices[3], vertices[2]), (vertices[2], vertices[0]),
        (vertices[4], vertices[5]), (vertices[5], vertices[7]), (vertices[7], vertices[6]), (vertices[6], vertices[4]),
        (vertices[0], vertices[4]), (vertices[1], vertices[5]), (vertices[2], vertices[6]), (vertices[3], vertices[7])
    ]
    for edge in edges:
        ax.plot3D(*zip(*edge), color=color)

# Apply a geometric transformation to the cube
def transform_cube(ax, matrix, color, pos=(0, 0, 0)):
    # Create a grid of points within the cube
    x, y, z = np.meshgrid(range(2), range(2), range(2))
    cube = np.vstack((x.flatten(), y.flatten(), z.flatten())).T

    # Apply the transformation matrix to the cube points
    cube_transformed = np.dot(cube - 0.5, matrix) + 0.5 + np.array(pos)

    # Draw the transformed cube
    draw_cube(ax, pos, color)
    for point in cube_transformed:
        draw_cube(ax, point, color)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the transformation matrix (rotation, scaling, etc.)
transformation_matrix = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 1]])

# Plot the original and transformed cubes with different colors
colors = ['red', 'green', 'blue', 'orange', 'purple']
for i, color in enumerate(colors):
    transform_cube(ax, transformation_matrix, color, pos=(i, 0, 0))

# Set the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the aspect ratio
ax.set_box_aspect([1,1,1])

# Show the plot
plt.show()
