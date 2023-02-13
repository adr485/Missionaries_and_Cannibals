def pr():
    if b==1:
        print('M '*m,'C '*c,'--Boat------------------------------- ','M '*(3-m),'C '*(3-c))
    else:
        print('M '*m,'C '*c,'-------------------------------Boat-- ','M '*(3-m),'C '*(3-c))
def invalid():
    if nm>2 or nc>2 or nm<0 or nc<0 or (nm+nc)>2:
        print('invalid move,enter again')
        return 1
    if b==1:
        if nm>m or nc>c or(nm==0 and nc==0):
            print('invalid move,enter again')
            return 1
    elif b==0:
        if nm>(3-m) or nc>(3-c) or(nm==0 and nc==0):
            print('invalid move,enter again')
            return 1
    return 0
print('Welcome to Missionaries and Cannibals game')
print('Let us start')
m=c=3
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
        elif (3-c)>(3-m) and (3-m)!=0:
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
        elif (3-c)>(3-m) and (3-m)!=0:
            print('GAME OVER')
            break
