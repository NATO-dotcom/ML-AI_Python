x=int(input("enter x:"))
y=int(input("enter y:"))
operation=input("enter the operation(+,-,/,*):")
if operation=='+':
   result=x+y
   #f stands for formatted string 
   print(f"{x}+{y}={result}")
elif operation=='-':
   result=x-y
   print(f"{x}-{y}={result}")
elif operation=='*':
   result=x*y
   print(f"{x}*{y}={result}")
elif operation=='/':
    if y!=0:
      result=x/y
      print(f"{x}/{y}={result}")
    else:
      print("error:division by zero is not allowed.")
else:
    print("invalid operation")