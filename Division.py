class Number:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value

a = Number(20)
b = Number(5)

print(a / b)