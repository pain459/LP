import ephem
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create an observer
observer = ephem.Observer()
observer.lat = '51.5074'  # Latitude of the observer (e.g., London)
observer.lon = '-0.1278'  # Longitude of the observer (e.g., London)
observer.elevation = 0  # Elevation of the observer (sea level)

# Set the date and time for the simulation
observer.date = ephem.now()

# Define solar system objects
sun = ephem.Sun()
mercury = ephem.Mercury()
venus = ephem.Venus()
earth = ephem.Sun()  # Approximate Earth's position using the Sun object
mars = ephem.Mars()
jupiter = ephem.Jupiter()
saturn = ephem.Saturn()

# Compute positions
sun.compute(observer)
mercury.compute(observer)
venus.compute(observer)
earth.compute(observer)
mars.compute(observer)
jupiter.compute(observer)
saturn.compute(observer)

# Additional objects
moon = ephem.Moon()

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot Sun
ax.scatter(0, 0, 0, color='yellow', label='Sun')

# Plot planets
for planet in [mercury, venus, earth, mars, jupiter, saturn]:
    x = planet.g_ra
    y = planet.g_dec
    z = np.sin(np.radians(planet.alt)) * 100  # Scale altitude for better visibility
    ax.scatter(x, y, z, label=planet.name)

# Compute and plot moon's position around Mars
mars_observer = ephem.Observer()
mars_observer.date = observer.date
mars_observer.lat = observer.lat
mars_observer.lon = observer.lon
phobos = ephem.Moon(mars_observer)
phobos.compute(mars_observer)
x = phobos.g_ra
y = phobos.g_dec
z = np.sin(np.radians(phobos.alt)) * 100  # Scale altitude for better visibility
ax.scatter(x, y, z, label="Phobos")

deimos = ephem.Moon(mars_observer)
deimos.compute(mars_observer)
x = deimos.g_ra
y = deimos.g_dec
z = np.sin(np.radians(deimos.alt)) * 100  # Scale altitude for better visibility
ax.scatter(x, y, z, label="Deimos")

# Set labels
ax.set_xlabel('RA')
ax.set_ylabel('DEC')
ax.set_zlabel('Altitude')
ax.set_title('Solar System Simulator')
ax.legend()

plt.show()
