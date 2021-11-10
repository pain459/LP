from time import sleep
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuese = calc_hypotenuese(a, b)
            if is_int(hypotenuese):
                triples.append((a, b, int(hypotenuese)))
    return triples

def calc_hypotenuese(a, b):
    return (a**2 + b**2) ** .5

def is_int(n):
    return n.is_integer()

#sleep(.6)
triples = calc_triples(1000)