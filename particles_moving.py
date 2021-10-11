# # 3D PARTICLE COLLISION SIMULATION
#
# # TODO: ONE PARTICLE MOVEMENT
# #  WALL BOUNDARY COLLISION - ANGLE REBOUND CALCULATION. Finished the boundary.
# #  FORCE IN PARTICLE COLLISION CALCULATION
# #  POINT-SIZE RELATION TO PARTICLE SIZE - AND COLLISION IMPACT
# #  F=MA, SPEED OF PARTICLE MOVEMENT - DIFFERENT ANIMATION FUNCS?
from random import randint
import matplotlib.pyplot as plt


class Particle:
    def __init__(self, xmin, ymin, zmin, xmax, ymax, zmax):
        self.pos_bounds = {
            'x': {'min': xmin, 'max': xmax}, 'y': {'min': ymin, 'max': ymax}, 'z': {'min': zmin, 'max': zmax}
        }
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0
        self.current_pos = [self.current_x, self.current_y, self.current_z]

    def move(self):
        move_vector = [randint(-5, 5), randint(-5, 5), randint(-5, 5)]

        if self.current_x + move_vector[0] < self.pos_bounds['x']['min']:
            move_vector[0] = 0
        elif self.current_x + move_vector[0] > self.pos_bounds['x']['max']:
            move_vector[0] = 0
        if self.current_y + move_vector[1] < self.pos_bounds['y']['min']:
            move_vector[1] = 0
        elif self.current_y + move_vector[1] > self.pos_bounds['y']['max']:
            move_vector[1] = 0
        if self.current_z + move_vector[2] < self.pos_bounds['z']['min']:
            move_vector[2] = 0
        elif self.current_z + move_vector[2] > self.pos_bounds['z']['max']:
            move_vector[2] = 0

        self.current_x += move_vector[0]
        self.current_y += move_vector[1]
        self.current_z += move_vector[2]
        self.current_pos = [self.current_x, self.current_y, self.current_z]


from random import randint


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Set the axis limits so they aren't recalculated each frame.
    xmin, ymin, zmin, xmax, ymax, zmax = 0, 0, 0, 20, 20, 20
    ax.set_facecolor((0,0,0))
    ax.set_zlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_xlim(0, 20)

    scatterframe = None

    particles = [Particle(xmin, ymin, zmin, xmax, ymax, zmax) for i in range(50)]
    colors = [[randint(0,255)/255,randint(0,255)/255,randint(0,255)/255] for i in range(50)]
    sizes = [randint(20,100) for i in range(50)]
    previous_positions = []

    while True:
        # If a scatterplot is already drawn, remove it before drawing a new one.
        if scatterframe:
            ax.collections.remove(scatterframe)

        # Plot the new scatterplot and pause briefly before continuing.
        xs, ys, zs = [], [], []
        for ps in particles:
            xs.append(ps.current_x)
            ys.append(ps.current_y)
            zs.append(ps.current_z)
        scatterframe = ax.scatter3D(xs, ys, zs, s=sizes, c=colors)
        plt.pause(0.025)
        for p in particles:
            p.move()


if __name__ == '__main__':
    main()
