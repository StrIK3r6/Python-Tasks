matrix = []
i=0
j=0
row = int(input("Enter the number of rows:")) 
col = int(input("Enter the number of columns:"))

  
def matrix_build():

 print("The matrix is: \n") 
  
 
 for i in range(row):           
    m =[] 
    for j in range(col):
         import random
         m.append(random.randint(1,101)) 
    matrix.append(m) 
  

 for i in range(row): 
    for j in range(col): 
        print(matrix[i][j], end = " ") 
    print()
    
 print("\n") 
    
def maxsum():
    
    d=dict()
    
    
    for i in range(row):
     summ=0   
     for j in range(col): 
       summ+=matrix[i][j]  
     print("The sum of "+str(i+1)+" row is: ",summ)
     
     d[i+1]=[summ]

    print("\n")
    d=sorted(d.items(),key=lambda x:x[1], reverse=True)
    print(d)
    print("\n")      

    x=input("Enter the row no u see first in the list")
        
    print("entry at row: ",x)
    print("Exit at row: ",x)

    
        

    
   



matrix_build()
maxsum()
   
