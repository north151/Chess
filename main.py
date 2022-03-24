from initBoard import begin,initBoard
from rule import Judge
import os 
import copy

class Now():
    x1,y1=0,0
    x2,y2=0,0
    dead=0
    run_chess=0
    flag="红"
    def __init__(self):
        self.dead=0
  
    

class Chess():
    no = 0	     # no 空格													  		
    r1,b1 = 1,-1  # 1 兵卒
    r2,b2 = 2,-2  # 2 炮
    r3,b3 = 3,-3  # 3 車
    r4,b4 = 4,-4  # 4 馬
    r5,b5 = 5,-5  # 5 相象
    r6,b6 = 6,-6  # 6 士仕 
    r7,b7 = 7,-7  # 7 帅将
    def __init__(self):
        self.no = 0
     



def draw_borad():
    os.system("cls")
    print("")
    print("      0  1  2  3  4  5  6  7  8 ")
    print("     ---------------------------")
    for i in range(len(borad)):
        if(i==5):
            print("")  
            
        print(" ",i,"|",end=(""))
        for j in range(len(borad[0])):
            if(borad[i][j]>=0):
                print("",borad[i][j],end=(" "))
            else:
                print(borad[i][j],end=(" "))
        print("|")
    print("     ---------------------------")
    print("请严格按要求输入,例如: 9,2 ,输入h,h棋,输入b,b悔棋")




def choose_chess(now,chess,borad,note):
    x1,y1 = input("输入选中棋子 x y:\n").split(",")
    if(x1=="h" and y1=="h"):
        return True,False
    if(x1=="b" and y1=="b"):
        return False,True
    x1,y1 = int(x1),int(y1)
    
    '''
    1.选中棋子不能越界
    2.选中棋子必须是己方
    '''
    #红旗
    if(now.flag == "红"):
        while(x1<0 or x1>9 or y1<0 or y1>8 or borad[x1][y1]<=0):      
           x1,y1 = input("请选中红棋,输入 x y:\n").split(",")
           if(x1=="h" and y1=="h"):
               return True,False
           if(x1=="b" and y1=="b"):
               return False,True
           x1,y1 = int(x1),int(y1)
           
    #黑旗      
    elif(now.flag == "黑"):
        while(x1<0 or x1>9 or y1<0 or y1>8 or borad[x1][y1]>=0):
           x1,y1 = input("请选中黑棋,输入选 x y:\n").split(",")
           if(x1=="h" and y1=="h"):
               return True,False
           if(x1=="b" and y1=="b"):
               return False,True
           x1,y1 = int(x1),int(y1)
 
    
    #记录将要拿起的棋子
    now.run_chess=borad[x1][y1]
    #拿起棋子
    borad[x1][y1]=chess.no
    #记录起子位置
    now.x1,now.y1=x1,y1
    
    rule=Judge()
    
    
    return False,False
    
    
    
    
def drap_chess(game,dead,now,chess,borad,note):
    
    x2,y2 = input("输入落子位置 x y:\n").split(",")
    x2,y2 = int(x2),int(y2)
    
    
    
    '''
    1.落子不能越界
    2.落子不能吃己方
    3.落子落在原地,重新选择
    '''
    #红旗落子
    if(now.flag == "红"):
        while(x2<0 or x2>9 or y2<0 or y2>8 or borad[x2][y2]>0): 
           x2,y2 = input("请重新落子,输入 x y:\n").split(",")
           x2,y2 = int(x2),int(y2)
           
    #黑旗落子      
    elif(now.flag == "黑"):
        while(x2<0 or x2>9 or y2<0 or y2>8 or borad[x2][y2]<0):
           x2,y2 = input("请重新落子,输入选 x y:\n").split(",")
           x2,y2 = int(x2),int(y2)
    
    
 
    #记录将要被吃的棋子
    now.dead=borad[x2][y2]
    dead.append(borad[x2][y2])
    #落下棋子
    borad[x2][y2] = now.run_chess
    #记录落子位置
    now.x2,now.y2=x2,y2
    
    
    #落在了原地
    if(now.x1==now.x2 and now.y1==now.y2):
        return
    else:
        game.append(copy.copy(now))
        
    #更换执棋手
    if(now.flag=="红"):
        now.flag="黑"
    elif(now.flag=="黑"):
        now.flag="红"
        
    
def read(game):
    for now in game:
        print(note[str(now.run_chess)],"吃掉",note[str(now.dead)],"位置:",(now.x1,now.y1),"-->",(now.x2,now.y2))


    



if __name__ == '__main__':
    

    # 注册登录


    # 开始
    borad=begin()    
    draw_borad()
    
    chess=Chess()
    end=False
    back=False
    now=Now()
    game=[]
    dead=[]
    note={
         "0":"空子", "-7":"黑将",  "7":"红帅",
        "-1":"黑卒", "-2":"黑炮", "-3":"黑車", 
        "-4":"黑馬", "-5":"黑象", "-6":"黑仕", 
         "1":"红兵",  "2":"红炮",  "3":"红車",  
         "4":"红馬",  "5":"红相",  "6":"红士",   
          }






    if_enter = "No"
    while(if_enter != "yes"):
        if_enter = input("输入yes进入游戏:\n")
    
    
    
    # 初始化棋盘
    initBoard(borad)  
    draw_borad()

    '''
    1.选中棋子
    '''
    while(True):
        
        end,back = choose_chess(now,chess,borad,note)
        
        #和棋
        if(end==True):
            print(now.flag,"方和棋")
            break
        
        #悔棋
        while(back==True and len(game)>0):
            last=game[-1]
            game=game[:-1]
            borad[last.x2][last.y2]=last.dead
            borad[last.x1][last.y1]=last.run_chess
            
            draw_borad()
            print("悔棋")
            read(game)
            
            back=False
            end,back=choose_chess(now, chess, borad, note)
            
            
        back=False
            
            
            
        drap_chess(game,dead,now,chess,borad,note)
        draw_borad()
        
        print("  >>>>>>>>>>起子:",note[str(now.run_chess)])
        print("  >>>>>>>>>>移动:",(now.x1,now.y1),"-->",(now.x2,now.y2))
        print("  >>>>>>>>>>吃掉:",note[str(now.dead)])
        
        
        
        if(-7 in dead or 7 in  dead):
            end=True
            

    
    
    read(game)
    
