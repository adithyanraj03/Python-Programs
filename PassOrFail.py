#print pass or fail
a=int(input ('Enter 1st Subject Marks :'))
b=int(input ('Enter 2nd Subject Marks :'))
c=int(input ('Enter 3rd Subject Marks :'))
d=int(input ('Enter 4th Subject Marks :'))
e=int(input ('Enter 5th Subject Marks :'))
avg=(a+b+c+d+e)/5
if (a>100):
    print ('Error in 1st Subject Marks')
elif (b>100):
    print ('Error 2nd Subject Marks')
elif (a>100):
    print ('Error 3rd Subject Marks')
elif (a>100):
    print ('Error 4th Subject Marks')
elif (a>100):
    print ('Error 5th Subject Marks')
elif (avg>=50):
    print ('Passed')
else:
    print ('Failed')
    
