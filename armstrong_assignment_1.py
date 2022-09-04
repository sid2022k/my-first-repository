num=input('enter any no: ')
k=1
sum=0
n=len(num)
check=0
for l in num:
    if(l=='.'):
        print('enter non-decimal no')
        check=1
if (check==0):
    if(int(num)>=0):
        for i in num:
            for j in range(0,n):
                k=k*int(i)
            sum=sum+k
            k=1
        if(sum==int(num)):
            print('Armstrong no')
        else:
             print('NOT Armstrong')
    else:
        print('enter non negative no')


