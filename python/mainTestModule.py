import userModule as test
import time

r = test.number_input()

print(f'반지름 {r:g}인 원의 둘레 : {test.get_circumference(r):7.2f}')
print(f'반지름 {r:g}인 원의 넓이 : {test.get_circle_area(r):7.2f}')

time.sleep(10)
