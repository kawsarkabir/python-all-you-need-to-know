a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if a<b and a<c:
    print('smallest number is:',a)
elif b<c and b<a:
    print('smallest number is:',b)
else:
    print('smallest number is:',c)
    