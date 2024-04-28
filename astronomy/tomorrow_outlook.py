import ephem
import datetime

# Create an observer (in this case, we're observing from a specific location)
observer = ephem.Observer()
observer.lat = '51.5074'  # Latitude of the observer (e.g., London)
observer.lon = '-0.1278'  # Longitude of the observer (e.g., London)
observer.elevation = 0  # Elevation of the observer (sea level)

# Set the observer's date to tomorrow
tomorrow = ephem.localtime(ephem.now()) + datetime.timedelta(days=1)
observer.date = tomorrow

# Compute sunrise and sunset
sunrise = ephem.localtime(observer.previous_rising(ephem.Sun()))
sunset = ephem.localtime(observer.next_setting(ephem.Sun()))

# Compute moonrise and moonset
moonrise = ephem.localtime(observer.previous_rising(ephem.Moon()))
moonset = ephem.localtime(observer.next_setting(ephem.Moon()))

# Compute moon illumination
moon = ephem.Moon()
moon.compute(observer)
illumination = moon.moon_phase

# Compute visible planets
planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
visible_planets = [p for p in planets if getattr(ephem, p)(observer).alt > 0]

# Compute visible constellations
constellations = ['Andromeda', 'Aquarius', 'Aries', 'Cancer', 'Capricornus', 'Cygnus', 'Gemini', 'Leo', 'Libra', 'Orion', 'Pegasus', 'Pisces', 'Sagittarius', 'Scorpius', 'Taurus', 'Virgo']
visible_constellations = [c for c in constellations if getattr(ephem, c)(observer).alt > 0]

# Print summary
print("Astronomical Summary for", tomorrow.strftime("%Y-%m-%d"))
print("Sunrise:", sunrise.strftime("%H:%M:%S"))
print("Sunset:", sunset.strftime("%H:%M:%S"))
print("Moonrise:", moonrise.strftime("%H:%M:%S"))
print("Moonset:", moonset.strftime("%H:%M:%S"))
print("Moon Illumination (Phase):", round(illumination, 2))
print("Visible Planets:", ', '.join(visible_planets))
print("Visible Constellations:", ', '.join(visible_constellations))
