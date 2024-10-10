#using a function, create a program that calculates the volume of a cylinder
import math
height = int(input(f"Enter the height of the cylinder"))
radius = int(input(f"Enter the radius of the cylinder"))
pie =math.pi
volume = pie*(radius**2)*height
print(volume)