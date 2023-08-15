class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # getter 
    @property
    def x(self):
        return self._x
    
    # setter for x
    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError("Value must be an int or float.")
        self._x = new_x

    # getter for y 
    @property
    def y(self):
        return self._y
    
    # setter for y 
    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError("New value must be an int or float.")
        self._y = new_y

    def __str__(self):
        return f"y-cor is {self._y} and x-cor is {self._x}"

p = Point(4, 8)


# flight class
class Flight:
    def __init__(self, capacity):
        self._capacity = capacity
        self._passangers = []
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def passangers(self):
        return self._passangers 
    
    def add_passanger(self, name):
        if not self.open_seats():
            return False 
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)


f = Flight(4)
people = ["a", "b", "c", "d", "e"]

for person in people:
    if f.add_passanger(person):
        print(f"{person} added succesfully.")
    else:
        print(f"No avail seats for {person}.")

# decorators 
def announce(f):
    def wrapper():
        print(f"About to run function {f.__name__}")
        f()
        print(f"Done running {f.__name__}")
    return wrapper


@announce
def hello():
    print("Hello World!")

people = [
    {"name": "Harry", "house": "Gyffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

print(sorted(people, key=lambda f: f['name']))
