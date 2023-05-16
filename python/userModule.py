pi = 3.141592

def number_input():
    output = input("반지름 입력하세요 : ")
    return float(output)

def get_circumference(radious):
    return 2 * pi * radious

def get_circle_area(radious):
    return pi * radious ** 2
