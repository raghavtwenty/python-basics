import random
print ('welcome to hand cricket')
print ('man vs machine')
b=1
c=2
f=0
f1=0
a=int(input('do you want want to bat(1)/bowl(2) ?'))
if a==b:
    print ('you are batting. enter the number from 1 to 5')
    if a==b:
        d=int(input('enter your score'))
        e=random.randrange(1,6)
        print('machine score',e)
        if (d!=e):
            f=f+d
            print ('now your score is',f)
        else:
            print ('you are out!')
            print ("your final score",f,'now you are bowling')
            j=int(input('bowl'))
            i=random.randrange(1,6)
            print ("machine score",i)
            if (j!=i):
                    f1=f1+i
                    print ('machine score is',f1)
            else:
                   print ('machine is out!')
                   print ("machine final score",f1)    
        if f>f1:
            print (' you won the match')
        elif f<f1:
            print ('machine won the match')
        elif f==f1:
            print ('match draw')
        
            
