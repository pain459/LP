capitals = {
    'France' : 'Paris',
    'Germany' : 'Berlin',
}

# nesting a list in a dictionary

travel_log = {
    'France': ['Paris', 'Lillie', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart'],
}

travel_log2 = {
    'France': {'cities_visited': ['Paris', 'Lillie', 'Dijon'],'total_visits': 12},
}

print(travel_log2['France']['cities_visited'])

# nesting dictionary inside a list.

travel_log3 = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lillie', 'Dijon'],
        'total_visits': 12
    },
    {
        'country': 'France',
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    },
]

print(travel_log3[0]['cities_visited'][1])