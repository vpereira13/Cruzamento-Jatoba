import secrets
from Entities.Location import Location
from data.settings import Xi, Xf, Yi, Yf


def generate_random_location():
    location = Location()
    location.set_x(Xi + secrets.randbelow(Xf - Xi))
    location.set_y(Yi + secrets.randbelow(Yf - Yi))

    return location
