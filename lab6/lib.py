import math

def uravnenie(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = round((-b + math.sqrt(discriminant)) / (2*a), 2)
        x2 = round((-b - math.sqrt(discriminant)) / (2*a), 2)
        return f"Корни уравнения: x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Уравнение имеет единственный корень: x = {x}"
    else:
        return "Уравнение не имеет вещественных корней"