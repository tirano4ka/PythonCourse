n = 36
k = 5                     
a = 1                    
b = 1                  
for m in range(1,n-1):
      c = b + a*k   
      a = b             
      b = c            
print(b)
