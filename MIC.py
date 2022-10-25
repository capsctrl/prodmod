import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

#Definisjon av funksjoner
def dist(point1, point2):
    return np.sqrt(abs(point1[0]-point2[0])**2+abs(point1[1]-point2[1])**2)

def radius(center, points):
    radiuses = []
    for point in points:
        radiuses.append(dist(point, center))
    return min(radiuses)

#Definisjon av målingspunkter
points = np.array([[30.082, 0.078],
[21.276, 21.307],
[0.071, 30.096],
[-21.147, 21.298],
[-29.921, 0.083],
[-21.121, -21.148],
[0.079, -29.916],
[21.440, -21.131]])

#Her finner vi Voronoi-diagrammet
vor = Voronoi(points)

#Her finner vi hvilken av Voronoi-nodene som gir størst innskrevet sirkel
minRadius = np.inf
center = None 
for vertex in vor.vertices:
    vertexRadius = radius(vertex, points)
    if vertexRadius < minRadius:
        minRadius = vertexRadius
        center = vertex

print(f"Center is: {center};  Diameter is: {minRadius * 2}")

#Her finner vi rundheten
dsts = []
for point in points:
    dsts.append(dist(point, center))

print(f"Roundness is: {abs(minRadius-max(dsts))} mm")


#Plotting av voronoi-diagrammet og sentrum i største inskrevne sirkel
fig = voronoi_plot_2d(vor)
plt.plot(center[0], center[1], marker="o", color="red")

plt.show()



