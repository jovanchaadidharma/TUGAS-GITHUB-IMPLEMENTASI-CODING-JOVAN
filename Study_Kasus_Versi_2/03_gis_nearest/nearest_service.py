"""Cari pos layanan terdekat menggunakan jarak Haversine."""
from math import radians, sin, cos, asin, sqrt

services = {
    "Pos A": (-3.800, 102.260),
    "Pos B": (-3.825, 102.285),
    "Pos C": (-3.845, 102.245),
}
requests = {
    "Titik permintaan 1": (-3.808, 102.263),
    "Titik permintaan 2": (-3.839, 102.251),
    "Titik permintaan 3": (-3.821, 102.279),
}

def haversine_km(a, b):
    lat1, lon1 = a
    lat2, lon2 = b
    lat1, lat2 = radians(lat1), radians(lat2)
    dlat, dlon = lat2 - lat1, radians(lon2 - lon1)
    h = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    return 6371 * 2 * asin(sqrt(h))

for request_name, coordinate in requests.items():
    distances = [(name, haversine_km(coordinate, service_coord))
                 for name, service_coord in services.items()]
    name, distance = min(distances, key=lambda item: item[1])
    print(f"{request_name} -> {name} ({distance:.2f} km garis-besar)")
