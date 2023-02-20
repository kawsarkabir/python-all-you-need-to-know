""" for i in range (1, 6):
    for j in range (1, 6):
        print(i*j, end = ' ')
    print()    
     """
""" for row in range(3):
    for col in range(row + 1):
      print('*' , end = ' ')
    print() """

for row in range(7):
    for col in range(row + 1):
        print(chr(97+row), end= ' ')
    print()
    