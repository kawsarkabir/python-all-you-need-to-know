""" === problem solving 02===
Take three integer input form user and find the largest number between using if-elif-else statement 
"""
x = int (input('Enter the num1: '));
y = int (input('Enter the num2: '));
z = int (input('Enter the num3: '));
if x > y and x > z:
    print(x,'is Largest Number')
elif y > x and y > z:
    print(y,'is largest number')    
else:
    print(z,'is largest number')