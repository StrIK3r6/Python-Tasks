def image_count():
    
 x=int(input("State the no. of files u want to enter: "))
 f=open("secret_images.txt","w")
    
 
 for i in range(x):
    string = str(input("Enter the file type: \n"))
    string = string + "\n" 
    f.write(string)

 c=0
 g=0
 b=0
 i=0
 j=0

    
 f = open ("secret_images.txt", "r")
 
 # for j in range(0,x):
 # print (f.readline())


 for j in range(0,x):
    filename = f.readline()
    print (filename.split(".")[-1])
    ftype=str(filename.split(".")[-1])
    print(ftype)
  
    if filename.split(".")[-1]=="bmp":
        c+=1
    elif filename.split(".")[-1]=="jpeg":
        g+=1
    elif filename.split(".")[-1]=="png":                                                                                                                                                      
        b+=1
    else:
        print("file type invald")
 print("No of jpeg files are: ",g)
 print("No of bmp files are: ",c)
 print("No of png files are: ",b)
 
  
 f.close() 


image_count() 
 
