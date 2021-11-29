"""def sep(arr):
   a=len(arr) 
   i=0
   while i<a:
        if i==0:
            print(arr[i],end='')
        elif i+1==a:
            print(' and ' + arr[i],end='')
        else:
            print(', ' + arr[i],end='')

        i+=1

spam=['apples','bananas','tofu','cats']
sep(spam)
"""

import random
heads=0
tails=0
b=0
c=0
for i in range(1,100):
    a=random.randint(0,1)
    if a==c:
        b+=1
    else :
        if b>=6:
            if a==0:
                heads+=1
            else :
                tails+=1
        c=a
        b=0
print (heads,tails)

