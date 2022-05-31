# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
r=input("enter rate")
r=float(r)
if h<=40:
    
    pay=h*r
    print(pay)
elif h>40:
     r=r
     pay=h*r
     print(pay)   
