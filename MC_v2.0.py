def pr():
    if b==1:
        print('M '*m,'C '*c,'--Boat------------------------------- ','M '*(n-m),'C '*(n-c))
    else:
        print('M '*m,'C '*c,'-------------------------------Boat-- ','M '*(n-m),'C '*(n-c))
def invalid():
    if nm>bs or nc>bs or nm<0 or nc<0 or (nm+nc)>bs:
        print('invalid move,enter again')
        return 1
    if b==1:
        if nm>m or nc>c:
            print('invalid move,enter again')
            return 1
    elif b==0:
        if nm>(n-m) or nc>(n-c):
            print('invalid move,enter again')
            return 1
    return 0
print('Welcome to Missionaries and Cannibals game')
print('Let us start')
m=c=n=int(input('enter no.of Missionaries and Cannibals: '))
bs=int(input('enter boat size: '))
b=1
pr()
while(1):
    if b==1:
        print('enter no.of Missionaries you want to move')
        nm=int(input())
        print('enter no.of Cannibals')
        nc=int(input())
        while(invalid()):
            print('enter no.of Missionaries you want to move')
            nm=int(input())
            print('enter no.of Cannibals')
            nc=int(input())
        m-=nm
        c-=nc
        b=0
        pr()
        if c>m and m!=0:
            print('GAME OVER')
            break
        elif (n-c)>(n-m) and (n-m)!=0:
            print('GAME OVER')
            break
        if m==0 and c==0:
            print('YOU WON!!')
            break
    elif b==0:
        print('enter no.of Missionaries you want to move')
        nm=int(input())
        print('enter no.of Cannibals')
        nc=int(input())
        while(invalid()):
            print('enter no.of Missionaries you want to move')
            nm=int(input())
            print('enter no.of Cannibals')
            nc=int(input())
        m+=nm
        c+=nc
        b=1
        pr()
        if c>m and m!=0:
            print('GAME OVER')
            break
        elif (n-c)>(n-m) and (n-m)!=0:
            print('GAME OVER')
            break