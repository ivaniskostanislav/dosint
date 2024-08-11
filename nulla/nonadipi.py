class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def __gt__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.volume() > other.volume()

    def __repr__(self):
        return f"Box({self.width}, {self.height}, {self.depth})"

# Example usage
box1 = Box(3, 4, 5)
box2 = Box(2, 6, 5)

print(f"Volume of box1: {box1.volume()}")
print(f"Volume of box2: {box2.volume()}")

if box1 > box2:
    print(f"{box1} is larger than {box2}")
else:
    print(f"{box1} is not larger than {box2}")
