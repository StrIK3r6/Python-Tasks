def student_records():
    records_dict=dict()
    x=int(input("The no of records u want to enter: "))

    i=[]
    e=1
    while e<=x:
        key=str(input("Enter the name: "))
        i.append(key)
        e+=1

    j=[]
    b=1
    while b<=x:
        value=int(input("Enter the marks"))
        j.append(value)
        b+=1          
    j=sorted(j,reverse=True)              


    dictionary=dict(zip(i,j))
    print(dictionary)
                  
student_records()    
