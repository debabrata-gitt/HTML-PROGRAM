class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

a = Number(30)
b = Number(10)

print(a - b)