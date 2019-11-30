

lengths = []
r = 0
    
def triangle_chopsticks():
 
 x=int(input("NO. of test cases: "))
 a=int(input("The lengths of stick a: "))
 b=int(input("length of stick b: "))
 r=int(input("input value of r: "))
 y=int(input("No. of sticks in jar: "))


 if y<r or y==r:
   print("Input value greater than r: ")
   y=int(input("No. of sticks in jar: "))

 lengths = []
 count = 1

 while count <= y:
   feed = int(input("please input length of stick "))
   lengths.append(feed)
   count+=1

 if count==y+1:
   print ("all", r,"inputs taken, thank you")
   print ("the lengths are   ",lengths)
 

 print("The totl no.of tringles that can be formed are: ",count) 


 if count>r:
    print("Natsu wins")
 else: 
    print("Grey wins")

triangle_chopsticks()










































    
