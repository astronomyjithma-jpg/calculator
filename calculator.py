print("                                      python calculator                                ")
print("if you need to := (+ = 1)/(- = 2)/(* = 3)/(/ = 4)")
x = int(input("enter your number:"))
y = int(input("enter your maths symbol:"))
z= int(input ("enter your second number:"))
j = 0
if y == 1 :
   j=x+z
elif y == 2 :
    j=x-z
elif y == 3 :
    j=x*z
elif y == 4 :
    j=x/z
else:
    print("invalid symbol")
print("answer",j)