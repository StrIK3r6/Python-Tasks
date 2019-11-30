def passorfail():
    
    m=int(input("Input the no of students: "))
    print("\n")
    my_dict=dict()
    p=[]
    
    for i in range(0,m):

        avg=0
        summ=0
        marks=[]
        check=0
        
        name=str(input("Enter the name of the " +str(i+1)+" student: "))
        n=int(input("Input the no of subjects: "))
        print("\n")
        
        for j in range(0,n):
        
            mark=int(input("Enter the marks out of 100 for the "+str(j+1)+" subject: "))
            if mark<=40:
                check=1
                 
            marks.append(mark)
            
        print("\n")
        
        
        for mark in marks:
              summ+=mark
              
        avg=summ/n
        
        if check==0:    
            my_dict[name]=[avg]
        else:
            p.append(name)

    print("\n")  
    newlist=sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
    print("The rank list of students along with avg. marks, who passed is: \n")
    print(newlist,"\n")    
    

    print("\n")   
    print("Students who failed in one or more sub. are: \n")
    print(p,"\n")
    
passorfail()
    
    
    
    
