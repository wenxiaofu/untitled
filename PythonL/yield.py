#迭代器还没有搞明白怎么用
cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna", "Amsterdam", "Den Haag"]
for location in cities:
    print("location: " + location)
capitals = { "France":"Paris", "Netherlands":"Amsterdam", "Germany":"Berlin", "Switzerland":"Bern", "Austria":"Vienna"}
for country in capitals:
    print("The capital city of " + country + " is " + capitals[country])
def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
city = city_generator()
print(next(city))
for test in city_generator():
    print(test)
