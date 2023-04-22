#created by raghav on 28 jan 2020
aa=int(input('press(1) for phy,cs,math OR press (2) for english ,math: '))
if aa==1:
 a=float(input('enter  pa1 mark: '))
 b=float(input('enter  pa2 mark: '))
 c=float(input('enter half yearly  mark: '))
 d=a/4
 e=b/4
 f=c/7
 g=f*3
 j=d+e+g
 print ('your mark out of 50: ',j)
 i=10
 k=5
 l=c-i
 n=l/2
 o=n+j
 p=o+k
 print ('you mark out of 100: ',p)
 if p<33:
  print ('you are fail')
 elif p>34:
  print ('you are pass')
elif aa==2:
 a=float(input('enter  pa1 mark: '))
 b=float(input('enter  pa2 mark: '))
 c=float(input('enter half yearly  mark: '))
 d=a/4
 e=b/4
 f=c/7
 g=f*3
 j=d+e+g
 print ('your mark out of 50: ',j)
 i=10
 k=5
 l=c-i
 n=l/2
 o=n+j
 p=o+k
 print ('you mark out of 100: ',p)
 if p<33:
  print ('you are fail')
 elif p>34:
  print ('you are pass')


