from geopy import distance

l = (51.509865,-0.118092)
p = (48.864716, 2.349014)

print(distance.distance(l, p).km)