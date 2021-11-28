
#函數collatz()，傳入number參數。
#如果number是偶數印出number//2,並返回數值。
#如果number是奇數印出3*number+1並返回數值。
def collatz(num):
    if num%2 == 0:
        print('num//2= '+str(num/2))
    else:
        print('3*num+1= '+str(3*num+1))        

for i in range(5):
    try:
        num=input()
        collatz(int(num))
    except ValueError:
        print('error')
