def tribonacci():
    n=int(input("Enter the no of test cases: "))
    j=1
    i=1
    a=0
    b=0
    c=1
    counter=0

    while(n>=i):
      s=int(input("the no of divisors: \n"))
      while(1):
        j=1
        summ=a+b+c
        a=b
        b=c
        c=summ
        counter=0
     
        while(j<=summ):
           
           if(summ%j==0):
              counter+=1
           j=j+1
          
        if(counter>s):
          print(summ)
          break

      i=i+1

tribonacci()
