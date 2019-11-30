def email_valid():
    
    email=str(input("Enter email: "))
    import sys

    c=0
    check=0
    lname=""
    
     
    for word in email:
          if word=="@":
           c+=1
          if c>=2:
              
           print("Email is invalid")
           sys.exit()
           
          else:
           ()
           
          
    if c==1:
        lname,string= email.split("@", 1)
        
    print(lname)

    if len(lname)>64:
        check=1
        
 
    if lname[0]=='.' or lname[-1]=='.':
        check=1
    

    for words in lname:                                                  
        x=ord(str(words))     
                                                     
        if(x==34 or x==40 or x==41 or x==62 or x==64 or x>=91 and x<=93):
             check=1
             
        else:
             ()
            
    count=0      
    for s in string:
           if s==".":
             count+=1
           if count>=2:
             check=1
             


    if count==1:
          dname,ename=string.split(".",1)
          


    print(dname)
    print(ename)      

              
          
    if (dname.isdigit()==True):
          check=1
          


    
    for l in dname:
         if l=="-":
           check=1
    
         if l[0]=="-":
           check=0  
         
    if dname[-1]=="-":
           check=0

          
    if dname.isalnum()==False:
          check=1 

    if dname.isalpha()==False:
          check=1
            
              
    if len(ename)>3:
            check=1
          
    print("\n")
    if check==1:

           print("The email is invalid")

    else:

           print("Email is valid")
           
              
email_valid()                
