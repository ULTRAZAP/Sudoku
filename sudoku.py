import random
nums=('1','2','3','4','5','6','7','8','9')#numbers
#BOX
b1=['*','*','*','*','*','*','*','*','*']
b2=['*','*','*','*','*','*','*','*','*']
b3=['*','*','*','*','*','*','*','*','*']
b4=['*','*','*','*','*','*','*','*','*']
b5=['*','*','*','*','*','*','*','*','*']
b6=['*','*','*','*','*','*','*','*','*']
b7=['*','*','*','*','*','*','*','*','*']
b8=['*','*','*','*','*','*','*','*','*']
b9=['*','*','*','*','*','*','*','*','*']
boxes=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
#boxes to check
box1=(b2,b3,b4,b7)
box2=(b1,b3,b5,b8)
box3=(b1,b2,b6,b9)
box4=(b1,b7,b5,b6)
box5=(b2,b8,b4,b6)
box6=(b3,b9,b4,b5)
box7=(b1,b4,b8,b9)
box8=(b7,b9,b5,b2)
box9=(b7,b8,b3,b6)
allbx=(box1,box2,box3,box4,box5,box6,box7,box8,box9)
#CHECK INDEX
chk1=(0,1,2)
chk2=(3,4,5)
chk3=(6,7,8)
chk4=(0,3,6)
chk5=(1,4,7)
chk6=(2,5,8)

check0=(chk1,chk4)
check1=(chk1,chk5)
check2=(chk1,chk6)
check3=(chk2,chk4)
check4=(chk2,chk5)
check5=(chk2,chk6)
check6=(chk3,chk4)
check7=(chk3,chk5)
check8=(chk3,chk6)
#logicstatements
statments=True
#LOGIC
for c in range(64):
    a=random.randint(0,8)#random box to insert number in
    b=random.randint(0,8)#random number to insert
    count=0
    for d in range(len(boxes)):
        count+=boxes[d].count('*')#counting total '*'
    if count>49:#checks so total '*' doesnt reduce below 49
        count=0
        count=boxes[a].count('*')#counting '*' in each box
        if count>4:#checks so '*' in box doesnt reduce below 4
            if nums[b] not in boxes[a]:# so numbers dont repeat
                for i in range(9):#loop for inserting numbers in all boxes
                    insrtbx=random.randint(0,8)
                    if boxes[a][insrtbx]=='*':#checks so a number doesnt replace a number
                        for chkbx in range(9):
                            if boxes.index(boxes[a])==0:
                                for bxallbx in box1:
                                    if insrtbx in check0[0] and insrtbx in check0[1]:
                                        for chkrw in chk1:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk4:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==1:
                                for bxallbx in box1:
                                    if insrtbx in check1[0] and insrtbx in check1[1]:
                                        for chkrw in chk1:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk5:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==2:
                                for bxallbx in box1:
                                    if insrtbx in check2[0] and insrtbx in check2[1]:
                                        for chkrw in chk1:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk6:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==3:
                                for bxallbx in box1:
                                    if insrtbx in check3[0] and insrtbx in check3[1]:
                                        for chkrw in chk2:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk4:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==4:
                                for bxallbx in box1:
                                    if insrtbx in check4[0] and insrtbx in check4[1]:
                                        for chkrw in chk2:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk5:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==5:
                                for bxallbx in box1:
                                    if insrtbx in check5[0] and insrtbx in check5[1]:
                                        for chkrw in chk2:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk6:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==6:
                                for bxallbx in box1:
                                    if insrtbx in check6[0] and insrtbx in check6[1]:
                                        for chkrw in chk3:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk4:
                                            if bxallbx[chkrw]==nums[b]:
                                               b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==7:
                                for bxallbx in box1:
                                    if insrtbx in check7[0] and insrtbx in check7[1]:
                                        for chkrw in chk3:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk5:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                                    
                            if boxes.index(boxes[a])==8:
                                for bxallbx in box1:
                                    if insrtbx in check8[0] and insrtbx in check8[1]:
                                        for chkrw in chk3:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                        for chkrw in chk6:
                                            if bxallbx[chkrw]==nums[b]:
                                                b=random.randint(0,8)
                                    boxes[a][insrtbx]=nums[b]
                        break
                    
#method for printing SUDOKU
def sudoku():
    print("",b1[0],b1[1],b1[2],"",b2[0],b2[1],b2[2],"",b3[0],b3[1],b3[2])
    print("",b1[3],b1[4],b1[5],"",b2[3],b2[4],b2[5],"",b3[3],b3[4],b3[5])
    print("",b1[6],b1[7],b1[8],"",b2[6],b2[7],b2[8],"",b3[6],b3[7],b3[8],"\n")
    print("",b4[0],b4[1],b4[2],"",b5[0],b5[1],b5[2],"",b6[0],b6[1],b6[2])
    print("",b4[3],b4[4],b4[5],"",b5[3],b5[4],b5[5],"",b6[3],b6[4],b6[5])
    print("",b4[6],b4[7],b4[8],"",b5[6],b5[7],b5[8],"",b6[6],b6[7],b6[8],"\n")
    print("",b7[0],b7[1],b7[2],"",b8[0],b8[1],b8[2],"",b9[0],b9[1],b9[2])
    print("",b7[3],b7[4],b7[5],"",b8[3],b8[4],b8[5],"",b9[3],b9[4],b9[5])
    print("",b7[6],b7[7],b7[8],"",b8[6],b8[7],b8[8],"",b9[6],b9[7],b9[8])

sudoku()
"""
b1 b1 b1 |b2 b2 b2 |b3 b3 b3
b1 b1 b1 |b2 b2 b2 |b3 b3 b3
b1 b1 b1 |b2 b2 b2 |b3 b3 b3

b4 b4 b4 |b5 b5 b5 |b6 b6 b6
b4 b4 b4 |b5 b5 b5 |b6 b6 b6
b4 b4 b4 |b5 b5 b5 |b6 b6 b6

b7 b7 b7 |b8 b8 b8 |b9 b9 b9
b7 b7 b7 |b8 b8 b8 |b9 b9 b9
b7 b7 b7 |b8 b8 b8 |b9 b9 b9
"""
