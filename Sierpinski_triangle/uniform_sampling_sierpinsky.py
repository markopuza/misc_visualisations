from random import randint
import matplotlib.pyplot as plt

def sample(precision=25):
    '''
        Samples from a uniform distribution over a Sierpinski triangle
        with vertices (0,0), (1,0), (1/2, sqrt(3)/2).

        The point is first sampled in barycentric coordinates,
        converted afterwards into Cartesian coordinates.

        returns: (x, y) - Cartesian coordinates
    '''
    x = y = 0
    for i in range(1, precision):
        # helper random variables
        X = randint(1, 3)
        Y1, Y2 = int(X==1), int(X==2)

        x += (Y1 + Y2/2) / (1 << i)
        y += Y2 / (1 << i+1)
    return x, 3 ** 0.5 * y

def sierpinski(n_points):
    '''
        Plots [n_points] samples from the Sierpinski triangle.
    '''
    plt.clf()
    samples = [sample() for _ in range(n_points)]
    plt.axis([-0.05, 1.05, -0.05, 1])
    plt.plot(*zip(*samples), ',', color='black')
    plt.show()


if __name__ == '__main__':
    print('Enter number of samples:')
    sierpinski(int(input()))
