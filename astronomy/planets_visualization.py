import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric
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

# Create a new figure with a dark background
plt.figure(figsize=(10, 8), facecolor='black')

# Plot the orbits with custom markers and colors
plt.plot(sun_pos.x.to_value(u.AU), sun_pos.y.to_value(u.AU), label='Sun', color='yellow', linestyle='None', marker='o', markersize=12)
plt.plot(mercury_pos.x.to_value(u.AU), mercury_pos.y.to_value(u.AU), label='Mercury', linestyle='-', color='gray', alpha=0.8, linewidth=1)
plt.plot(venus_pos.x.to_value(u.AU), venus_pos.y.to_value(u.AU), label='Venus', linestyle='-', color='orange', alpha=0.8, linewidth=1)
plt.plot(earth_pos.x.to_value(u.AU), earth_pos.y.to_value(u.AU), label='Earth', linestyle='-', color='cyan', alpha=0.8, linewidth=1)
plt.plot(mars_pos.x.to_value(u.AU), mars_pos.y.to_value(u.AU), label='Mars', linestyle='-', color='red', alpha=0.8, linewidth=1)
plt.plot(jupiter_pos.x.to_value(u.AU), jupiter_pos.y.to_value(u.AU), label='Jupiter', linestyle='-', color='tan', alpha=0.8, linewidth=1)
plt.plot(saturn_pos.x.to_value(u.AU), saturn_pos.y.to_value(u.AU), label='Saturn', linestyle='-', color='gold', alpha=0.8, linewidth=1)
plt.plot(uranus_pos.x.to_value(u.AU), uranus_pos.y.to_value(u.AU), label='Uranus', linestyle='-', color='lightblue', alpha=0.8, linewidth=1)
plt.plot(neptune_pos.x.to_value(u.AU), neptune_pos.y.to_value(u.AU), label='Neptune', linestyle='-', color='darkblue', alpha=0.8, linewidth=1)

# Set plot limits and labels
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.xlabel('X (AU)', color='white')
plt.ylabel('Y (AU)', color='white')
plt.title('Orbits of Planets in the Solar System (2024)', color='white')

# Set background color and grid
plt.gca().set_facecolor('black')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Add a legend with white text
plt.legend(loc='upper left', fontsize='medium', facecolor='black', edgecolor='white', labelcolor='white')

# Add text annotations for planets
plt.text(mercury_pos.x[-1].to_value(u.AU), mercury_pos.y[-1].to_value(u.AU), 'Mercury', color='gray', fontsize='small', ha='right', va='center')
plt.text(venus_pos.x[-1].to_value(u.AU), venus_pos.y[-1].to_value(u.AU), 'Venus', color='orange', fontsize='small', ha='right', va='center')
plt.text(earth_pos.x[-1].to_value(u.AU), earth_pos.y[-1].to_value(u.AU), 'Earth', color='cyan', fontsize='small', ha='right', va='center')
plt.text(mars_pos.x[-1].to_value(u.AU), mars_pos.y[-1].to_value(u.AU), 'Mars', color='red', fontsize='small', ha='right', va='center')
plt.text(jupiter_pos.x[-1].to_value(u.AU), jupiter_pos.y[-1].to_value(u.AU), 'Jupiter', color='tan', fontsize='small', ha='right', va='center')
plt.text(saturn_pos.x[-1].to_value(u.AU), saturn_pos.y[-1].to_value(u.AU), 'Saturn', color='gold', fontsize='small', ha='right', va='center')
plt.text(uranus_pos.x[-1].to_value(u.AU), uranus_pos.y[-1].to_value(u.AU), 'Uranus', color='lightblue', fontsize='small', ha='right', va='center')
plt.text(neptune_pos.x[-1].to_value(u.AU), neptune_pos.y[-1].to_value(u.AU), 'Neptune', color='darkblue', fontsize='small', ha='right', va='center')

# Hide axes
plt.xticks(color='white')
plt.yticks(color='white')

# Equal aspect ratio
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
