print('WELCOME')
print("------")

#instruction 
print("add=+")
print("sub=-")
print("multiply=*")
print("division=/")

print("_____________")

#opration
a=int(input("Enter your first Number="))
x=(input("Oprator="))
b=int(input("Enter your Second Number="))



if x== '+' :
    result= a+b

if x== '-':
    result= a-b

if x== '*':
    result=a*b

if x== "/":
    result=a/b

#result
print("Result=",result)

print()

print("!!!Made with Love!!!")