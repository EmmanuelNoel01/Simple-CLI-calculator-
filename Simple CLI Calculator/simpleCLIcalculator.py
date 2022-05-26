a=int(input("Enter first number:  "))
b=input("Enter action you want to perform +,*,/,-,%:  ")
c=int(input("Enter second number:  "))


if(b=="+"):
    print (a+c);
    
elif(b=="*"):
    print (a*c);  
    
elif(b=="/"):
    print (a/c);   

elif(b=="-"):
    print (a-c);
elif(b=="%"):
    print (a%c);    
else:
    print("Symbol doesn't exist. Sorry!") 