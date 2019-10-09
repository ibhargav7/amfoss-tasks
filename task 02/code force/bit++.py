x=int(input("number of statements: "))
y=input()
x=0
for i in range (x):
 if y[1:] =="++":
    x=x+1

 elif y[0:2] =="--":
    x=x-1
print (x)