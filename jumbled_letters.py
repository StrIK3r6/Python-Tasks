def jumbled_letters():
    x=int(input("Input the no of cases: "))

    count=1
    i=0
    line=[]
    result=[]
    res=[]
    k=0
    j=0
    
    
    while count <= x:
     s = str(input("please input the string: "))
     s=s.replace(' ','')
     line.append(s)  
     count+=1

    while i<x:
        
     string=""
     strings=""
     y=int(len(line[i]))
     for word in line[i]:
      
      if j<y:          
        if j%2==0:        
          string=string+word
          string=string.replace(' ','')
          print(string," string")
                    
        else:
          strings=strings+word
          strings=strings.replace(' ','')
          print(strings," strings")
          
          
      j+=1

     result.append(string)
     res.append(strings)
     print(result,"  result")
     print(res," res")
         
     i+=1

    for l in range(0,x):
      stringa=""  
      res[l]=(res[l])[::-1]
      stringa= result[l]+res[l]
      print(stringa)          

jumbled_letters()
