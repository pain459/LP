import ephem

# Create an observer (in this case, we're observing from Earth)
observer = ephem.Observer()
observer.lat = '0'  # Latitude of the observer (equator)
observer.lon = '0'  # Longitude of the observer (Greenwich)
observer.elevation = 0  # Elevation of the observer (sea level)

# Create a Moon object
moon = ephem.Moon()

# Set the observer's date to the current date and time
observer.date = ephem.now()

# Compute the position of the Moon
moon.compute(observer)

# Calculate the velocity of the Moon
speed_moon_ms = moon.hlon * ephem.earth_radius * 1000  # Convert from radians/hour to meters/second

# Print the result
print("The speed of the Moon while revolving around the Earth is approximately", round(speed_moon_ms, 2), "m/s.")
