
# pointer
a = 'abc'
b = a
a = 'xyz'
print(b)

# list and tuple


# if else
ageStr = input('birth: ')
age = int(ageStr)
if age >= 18:
    print('your age is',age)
    print('adult')
else :
    print('your age is', age)
    print('teenager')


# for and while
sum = 0
for x in range(101) :
    sum = sum + x
print(sum)

n = 0
while n < 90 :
    n = n +1
    if n%2 == 0 :
        continue
    print(n)


# dict and set
map = {'key1': 'value1'}
map['key2'] = 'value2'
map.pop('key1')
for key in map.keys():
    print(map.get(key))















