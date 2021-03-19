
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):  # sınıfi otomatik sisler
        print("Nesne silindi")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __repr__(self):
        print("repr")
        return f"x: {self.x} -- y: {self.y}"

    # def __str__(self):
    #     print("str")
    #     return f"x: {self.x} -- y: {self.y}"

    def __call__(self, *args, **kwargs):
        print("who is calling me?")


if __name__ == '__main__':
    # p = Person("Semiha", 25)

    v_1 = Vector(10, 20)
    print(f"call: {v_1()}")

    v_2 = Vector(60, 80)
    v_3 = v_1 + v_2
    print(f"add: {v_3}")

    v_3 = v_1 - v_2
    print(f"sub: {v_3}")

    v_3 = v_1 * v_2
    print(f"mul: {v_3}")