class constructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = constructor("John", 26)

print(p1.name)
print(p1.age)


class constructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p2 = constructor("Smith" ,40)
print(p2)
