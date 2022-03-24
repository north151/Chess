

from enum import Enum

no = 0	     # no 空格													  		
r1,b1 = 1,-1  # 1 兵卒
r2,b2 = 2,-2  # 2 炮
r3,b3 = 3,-3  # 3 車
r4,b4 = 4,-4  # 4 馬
r5,b5 = 5,-5  # 5 相象
r6,b6 = 6,-6  # 6 士仕 
r7,b7 = 7,-7  # 7 帅将



def begin():
    borad=[
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
        [no,no,no,no,no,no,no,no,no],
    ]
    return borad

def initBoard(borad):
    borad[0] = [b3,b4,b5,b6,b7,b6,b5,b4,b3]
    borad[1] = [no,no,no,no,no,no,no,no,no]
    borad[2] = [no,b2,no,no,no,no,no,b2,no]
    borad[3] = [b1,no,b1,no,b1,no,b1,no,b1]
    borad[4] = [no,no,no,no,no,no,no,no,no]
    borad[5] = [no,no,no,no,no,no,no,no,no]
    borad[6] = [r1,no,r1,no,r1,no,r1,no,r1]
    borad[7] = [no,r2,no,no,no,no,no,r2,no]
    borad[8] = [no,no,no,no,no,no,no,no,no]
    borad[9] = [r3,r4,r5,r6,r7,r6,r5,r4,r3]
