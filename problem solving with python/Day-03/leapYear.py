# find the leap year 
#method 01
year = int (input('Check The Leap Year : '))
""" if year % 400 == 0 and year % 100 == 0:
    print( year, 'is Leap Year');
elif year % 4 == 0 and year % 100 !=0:
    print(year, 'is Leap Year');
else:
    print(year, 'is Not Leap Year')    """

#methods 02
if(year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, 'is Leap Year');
else:
    print(year, 'is Not Leap Year')
    