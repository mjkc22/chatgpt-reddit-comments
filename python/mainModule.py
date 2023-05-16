import time

pi = 3.141592

def number_input():
    output = input("반지름 입력하세요 : ")
    return float(output)

def get_circumference(radious):
    return 2 * pi * radious

def get_circle_area(radious):
    return pi * radious ** 2

r = number_input()

print('반지름 {:g}인 원의 둘레 :'.format(r), '{:.2f}'.format(get_circumference(r)))
print('반지름 {:g}인 원의 넓이 :'.format(r), '{:.2f}'.format(get_circle_area(r)))

time.sleep(10)
