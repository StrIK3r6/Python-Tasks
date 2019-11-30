def cipher():
    
    str=input("enter a cipher : ")
    i=0
    
    while(i<len(str)):
     ascii=ord(str[i])
     if i%2==0:
        if ascii<=108 and ascii>=97 :
        #print(str[i])
            print(chr((ord(str[i])+13)),end="")
        elif ascii>108 and ascii<=122:
        #print(str[2])
            print(chr(97+12-(122-(ord(str[i])))),end="")
        elif ascii>=65 and ascii<=76:
            print((chr((ord(str[i])+13))),end="")
        elif ascii>76 and ascii<=90 :
            print((chr(97+12-(122-(ord(str[i]))))),end="")
        else:
            print((str[i]),end="")
     else:
        print(str[i],end="")
     i=i+1
          
cipher()    
