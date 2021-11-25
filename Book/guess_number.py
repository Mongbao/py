import random

num=random.randint(1,20)
print (num)
print('I an thinking of a number between 1 and 20')

for i in range(1,7):
    print('Take a guess')
    guess=int(input())
    if guess<num:
        print('Your guess is too low')
    elif guess>num:
        print('Your guess is too high')
    else:
        break
if guess == num:
    print('Good jog! You guess my number in ' + str(i) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(num))