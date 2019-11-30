  def minimax():

    List=[]
    
    values=input("Enter 5 integral values: ").split()
    
    for i in values:
         List.append(i)
        
    summ=0
    j=0
    List2=[]
    
    for no in List:
        summ+=int(no)
    print("\n")
    
    while j<5:
        
        value=summ
        value=summ-int(List[j])
        List2.append(value)
        print("The sum of the 4 values excluding "+ str(List[j])+" is: ",value)
        j+=1
        
    print("\n")    
    print(min(List2),max(List2))
    
minimax()









        
