a=int(input("enter a number= "))
rev=0
while a>0:
    r=a%10
    print(r,end="")
    #rev=rev*10+r
    a=int(a/10)
   