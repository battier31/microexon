import math


#  null function
def nop():
    pass


# indeed , return multi response is tuple type
def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi/6)
print(x, y)


# default parameter
# default param must point to invariable object
def power(x, n=2, m=7):
    s = 1
    while n > 0:
        n = n -1
        s = s*x
    return s + m


print(power(2))
print(power(2, 9))
print(power(2, m=1))


# variable param , indeed is tuple
def calc(*mun):
    sum = 0
    for i in mun:
        sum = sum + i * i
    return sum


print(calc(1, 2, 3, 4, 5, 6))
nums = [1, 2, 3]
print(calc(*nums))


# keywords param , indeed is dict
def person(name, age, **map):
    print('name:', name, 'age:', age, 'other', map)


person('Bob', 24, city='Beijing', job='Engineer', zipcode='123456')
extra = {'city': 'beijing', 'job': 'engineer'}
person('Bob', 24, **extra)


# recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(10))


# tail recursion
def fact_iter(num, result):
    if num == 1:
        return result
    return fact_iter(num - 1, num * result)


print(fact_iter(10, 1))







