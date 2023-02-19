# intro loop  in python 
# type of looping
#1.for loop 
#2. while loop
# 3.nested loop

# for loop
for i in range(20):
    print('Nasa is Hacking By HTML')

# even number find ussing for loop
""" num = list(range(0, 20, 3 ))
print(num); """

x = list(range(10, 0, -2))
print(x)


""" 
range function step
1. start, end, step
2. list ()
"""

""" a = 'Hello World'
for letter in a:
    print(letter) """

bag = ['alu','piyaz' , 'rosun', 'moris' , 89, 9, -9]
for item in bag:
    print(item);

lst = [1, 2, 3,4,5,6,7,8,9]
for i in lst:
    if i<= 10:
        print(i);


# 3 and 5 dara divition number ber korte cassi 
for i in range(20):
    if i%3 == 0 and i%5 ==0:
        print(i)


# sumation 
sum = 0;
for i in range(1, 11):
    sum = sum + i
    print(sum)