city_distances = {
"Bansko": 97,
"Brussels": 1701,
"Alexandria": 1403,
"Nice": 1307,
"Szeged": 469,
"Dublin": 2479,
"Palermo": 987,
"Moscow": 1779,
"Oslo": 2098,
"London": 2019,
"Madrid": 2259,
}

sofia_distance= 0
for city, distance in city_distances.items():
    if distance< 1500:
        sofia_distance=distance
        print(f"{city}: {sofia_distance} km") 