n=int(input("enter the range"))
print(" prime number upto",n,"are")
i=2;
for i in range(1,n+1):
    if(i>1):
       for j in range(2,i,(i//2)+1):
         if(i%j==0):
           break  
         else:
           print(i,end=" ")