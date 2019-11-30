def askkey():

    x=str(input("Enter the first string: "))
    y=str(input("Enter the second string: "))

    value=0
    value1=0


    for word in x:
        value+=ord(word)
        
    for word1 in y:
        value1+=ord(word1)

        
    if value==value1:
        print("The given strings are equal")
    else:
        print("The given strings are not equal")
        

askkey()
        
