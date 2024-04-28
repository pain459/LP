import ephem
import datetime
from geopy.geocoders import Nominatim

# Initialize geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Get location name from user
location_name = input("Enter the location: ")

# Get latitude and longitude
location = geolocator.geocode(location_name)

if location:
    latitude = str(location.latitude)
    longitude = str(location.longitude)
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    # Create an observer for the given location
    observer = ephem.Observer()
    observer.lat = latitude
    observer.lon = longitude
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

    # # Compute visible planets
    # planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
    # visible_planets = [p for p in planets if getattr(ephem, p)().compute(observer).alt > 0]

    # # Compute visible constellations
    # constellations = ['Andromeda', 'Aquarius', 'Aries', 'Cancer', 'Capricornus', 'Cygnus', 'Gemini', 'Leo', 'Libra', 'Orion', 'Pegasus', 'Pisces', 'Sagittarius', 'Scorpius', 'Taurus', 'Virgo']
    # visible_constellations = [c for c in constellations if getattr(ephem, c)().compute(observer).alt > 0]

    # Print summary
    print("\nAstronomical Summary for", tomorrow.strftime("%Y-%m-%d"))
    print("Sunrise:", sunrise.strftime("%H:%M:%S"))
    print("Sunset:", sunset.strftime("%H:%M:%S"))
    print("Moonrise:", moonrise.strftime("%H:%M:%S"))
    print("Moonset:", moonset.strftime("%H:%M:%S"))
    print("Moon Illumination (Phase):", round(illumination, 2))
    # print("Visible Planets:", ', '.join(visible_planets))
    # print("Visible Constellations:", ', '.join(visible_constellations))
else:
    print("Location not found.")
