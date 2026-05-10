import matplotlib.pyplot as plt
import numpy as np

#this line ignores warnings generated when NumPy detects an overflow
#because of how big the numbers will get
np.warnings.filterwarnings("ignore")

def complexMatrix(xmin, xmax, ymin, ymax, pixel_density):
    #generates inital set of cadidate values for mandelbrot set
    #returns 2d array of complex numbers
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def isStable(c, num_iterations):
    #runs the matrix through the mandelbrot set formula
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    #the entire mandelbrot set can fit in a circle with a radius of 2 units
    #this line saves a lot of useless calculations
    #and returns values belonging to the mandelbrot set
    return abs(z) <= 2

def getMembers(c, num_iterations):
    #returns a 1d array of complex numbers that belong to the mandelbrot set
    mask = isStable(c, num_iterations)
    return c[mask]

#plotting the mandelbrot set

#this line prepares the array of complex numbers
c = complexMatrix(-2, 0.5, -1.5, 1.5, pixel_density = 512)

#this line gets the values that belong to the mandelbrot set
#members = getMembers(c, num_iterations = 20)

#plt.scatter(members.real, members.imag, color = "black", marker = " ", s = 1)
plt.imshow(isStable(c, num_iterations = 20), cmpa = "binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()

'''def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c

def mandelbrot(candidate):
    return sequence(z=0, c=candidate)

def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)'''