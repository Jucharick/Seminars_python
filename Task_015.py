# Квадратное уравнение
# 32 * x**2 + 4 * x - 6 = 0
# (32, 4, -6)
# алгоритм должен принимать любое квадратное уравнение


# ax2 + bx + c = 0 
# D = b2 − 4ac 
# если D < 0, корней нет;
# если D = 0, есть один корень;
# если D > 0, есть два различных корня.
# x1 = (-b + D**0,5)/2*a
# x2 = (-b - D**0,5)/2*a

equation = '6 * x ** 2 + 4 * x - 3 = 0'
def create_koef(equation: str) -> tuple:
    new_koef = []
    nq = equation.replace(' ', '').replace('=0', ''). replace('+', ' ').replace('-', ' -').split()
    print(nq)

    for item in nq:
        if item.startswith('x'):
            new_koef.append(1)
        elif item.startswith('-x'):
            new_koef.append(-1)
        else:
            new_koef.append(int(item.split('*')[0]))
    return new_koef
create_koef(equation)

def solution(koef: list):
    a, b, c = koef
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b + disc**0.5)/(2*a)
        x2 = (-b - disc**0.5)/(2*a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = -b/(2*a)
        return round(x, 2)
    else:
        return (None)

print(solution(create_koef(equation)))
