ttt={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
l=[]
flag=0
def box(ttt):
    print("\t\t\t",end=' ')
    print(ttt['1']+' | '+ttt['2']+' | '+ttt['3'])
    print("\t\t\t---+---+--")
    print("\t\t\t",end=' ')
    print(ttt['4']+' | '+ttt['5']+' | '+ttt['6'])
    print("\t\t\t---+---+--")
    print("\t\t\t",end=' ')
    print(ttt['7']+' | '+ttt['8']+' | '+ttt['9'])

box(ttt)
print("Game rules:")
print("There will be two palyers and each players will be given chances one by one.")
print("Enter digits from 1-9 for the boxes of tic-tac-toe.")
print("The boxes are named as : 1-2-3\\n 4-5-6\\n 7-8-9")

for i in range(9):
#    print(i)
    print("Its player",end=' ')
    print((i%2)+1,end=' ')
    print("turn")
    print("Enter the number")
    a=input()
    if (a!='1' and a!='2' and a!='3' and a!='4' and a!='5' and a!='6' and a!='7' and a!='8' and a!='9'):
        while (a!='1' and a!='2' and a!='3' and a!='4' and a!='5' and a!='6' and a!='7' and a!='8' and a!='9'):
            print("Wrong input, enter again")
            a=input()
            
    if a in l:
        while a in l:
            print("This box is already filled, try another number")
            a=input()
#        i=i-1
#        print(i)
    if a not in l:
        l.append(a)
        if (i%2==0):
            ttt[a]='X'
        else:
            ttt[a]='O'

    box(ttt)
    if (i>=4):
        if (ttt['1']==ttt['2'] and ttt['1']==ttt['3'] and ttt['1']!=' ' and ttt['2']!=' ' and ttt['3']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['4']==ttt['5'] and ttt['4']==ttt['6'] and ttt['4']!=' ' and ttt['5']!=' ' and ttt['6']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['7']==ttt['8'] and ttt['7']==ttt['9'] and ttt['7']!=' ' and ttt['8']!=' ' and ttt['9']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['1']==ttt['4'] and ttt['1']==ttt['7'] and ttt['1']!=' ' and ttt['4']!=' ' and ttt['7']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['2']==ttt['5'] and ttt['2']==ttt['8'] and ttt['2']!=' ' and ttt['5']!=' ' and ttt['8']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['3']==ttt['6'] and ttt['3']==ttt['9'] and ttt['3']!=' ' and ttt['6']!=' ' and ttt['9']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['1']==ttt['5'] and ttt['1']==ttt['9'] and ttt['1']!=' ' and ttt['5']!=' ' and ttt['9']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif(ttt['3']==ttt['5'] and ttt['3']==ttt['7'] and ttt['3']!=' ' and ttt['5']!=' ' and ttt['7']!=' '):
            print("Congratulations! player",end=' ')
            print((i%2)+1,end=' ')
            print("won.")
            flag=1
            break
        elif (i<8):
            continue
#        box(ttt)
    if i==8:
        if flag==0:
            print("Game over! Nobody won")
        break
