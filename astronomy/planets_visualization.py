import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric, CartesianRepresentation
from astropy import units as u

# Define the time range for the simulation
start_time = Time("2024-01-01")
end_time = Time("2025-01-01")
times = start_time + np.linspace(0, 365, 1000) * u.day

# Calculate the positions of the planets
with solar_system_ephemeris.set('builtin'):
    sun_pos = get_body_barycentric('sun', times)
    mercury_pos = get_body_barycentric('mercury', times)
    venus_pos = get_body_barycentric('venus', times)
    earth_pos = get_body_barycentric('earth', times)
    mars_pos = get_body_barycentric('mars', times)
    jupiter_pos = get_body_barycentric('jupiter', times)
    saturn_pos = get_body_barycentric('saturn', times)
    uranus_pos = get_body_barycentric('uranus', times)
    neptune_pos = get_body_barycentric('neptune', times)

# Plot the orbits
plt.figure(figsize=(10, 8))
plt.plot(sun_pos.x, sun_pos.y, label='Sun', color='yellow', linestyle='None', marker='o')
plt.plot(mercury_pos.x, mercury_pos.y, label='Mercury', linestyle='-', color='gray')
plt.plot(venus_pos.x, venus_pos.y, label='Venus', linestyle='-', color='orange')
plt.plot(earth_pos.x, earth_pos.y, label='Earth', linestyle='-', color='blue')
plt.plot(mars_pos.x, mars_pos.y, label='Mars', linestyle='-', color='red')
plt.plot(jupiter_pos.x, jupiter_pos.y, label='Jupiter', linestyle='-', color='brown')
plt.plot(saturn_pos.x, saturn_pos.y, label='Saturn', linestyle='-', color='goldenrod')
plt.plot(uranus_pos.x, uranus_pos.y, label='Uranus', linestyle='-', color='lightblue')
plt.plot(neptune_pos.x, neptune_pos.y, label='Neptune', linestyle='-', color='darkblue')

# Set plot limits and labels
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title('Orbits of Planets in the Solar System (2024)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()
