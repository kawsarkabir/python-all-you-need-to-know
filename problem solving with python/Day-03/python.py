import math 
def my_area(radius):
    area = math.pi * radius ** 2
    return area
radius = float(input('Enter th'))
area = my_area(radius)
print(area)