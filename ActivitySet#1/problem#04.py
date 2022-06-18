hrs = input("Enter Hours:")
h = float(hrs)
r=input("enter rate")
r=float(r)
if h<=40:
    
    pay=h*r
    print(pay)
elif h>40:
     h=h-40
     pay=(40*r)+h*r*1.5
     print("pay:",pay)   