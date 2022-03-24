

def Judge(borad,x,y,now):
    last=[]    
    #红兵  
    if(now.run_chess=="r1"):
        #前
        if(x-1>=0 and borad[x-1][y]<=0):
            last.append((x-1,y))
        #左
        if(y-1>=0 and borad[x][y-1]<=0):
            last.append((x,y-1))
        #右
        if(y+1<=8 and borad[x][y+1]<=0):
            last.append((x,y+1))
        return last    
     
    #红炮
    if(now.run_chess=="r2"):
        pass
        return last
    
    
    #红車
    if(now.run_chess=="r3"):
        pass
        return last
    
    #红馬
    if(now.run_chess=="r4"):
        '''
        1.不撇脚
        2.不越界
        3.目的地为空或敌方棋子
        
        '''
        #前左
        if(x-1>=0 and borad[x-1][y]==0 and x-2>=0 and y-1>=0 and borad[x-2][y-1]<=0):
            last.append((x-2,y-1))
        #前右
        if(x-1>=0 and borad[x-1][y]==0 and x-2>=0 and y+1<=8 and borad[x-2][y+1]<=0):
            last.append((x-2,y+1))
        #后左
        if(x+1<=9 and borad[x+1][y]==0 and x+2<=9 and y-1>=0 and borad[x+2][y-1]<=0):
            last.append((x+2,y-1))
        #后右
        if(x+1<=9 and borad[x+1][y]==0 and x+2<=9 and y+1<=8 and borad[x+2][y+1]<=0):
            last.append((x+2,y+1))
        
        #左前
        if(y-1>=0 and borad[x][y-1]==0 and x-1>=0 and y-2>=0 and borad[x-1][y-2]<=0):
            last.append((x-1,y-2))
        #左后
        if(y-1>=0 and borad[x][y-1]==0 and x+1<=9 and y-2>=0 and borad[x+1][y-2]<=0):
            last.append((x+1,y-2))
        #右前
        if(y+1<=8 and borad[x][y+1]==0 and x-1>=0 and y+2>=0 and borad[x-1][y+2]<=0):
            last.append((x-1,y+2))
        #右后
        if(y+1<=8 and borad[x][y+1]==0 and x+1<=9 and y+2<=8 and borad[x+1][y+2]<=0):
            last.append((x-1,y-2))
        
        return last
    
    
    #红相
    if(now.run_chess=="r5"):
        '''
        1.不过河
        2.目的地为空或敌方棋子
        '''
        #前左
        if(x-2>=5 and y-2>=0 and borad[x-2][y-2]<=0):
            last.append((x-2,y-2))
        #前右
        if(x-2>=5 and y+2<=8 and borad[x-2][y+2]<=0):
            last.append((x-2,y+2))
        #后左
        if(x+2<=9 and y-2>=0 and borad[x+2][y-2]<=0):
            last.append((x+2,y-2))
        #右后
        if(x+2<=9 and y+2<=8 and borad[x+2][y+2]<=0):
            last.append((x+2,y+2))
        return last
    
    
    #红士
    if(now.run_chess=="r6"):
        '''
        1.不出范围
        2.目的地为空或敌方棋子
        '''
        #前左
        if(x-1>=7 and y-1>=3 and borad[x-1][y-1]<=0):
            last.append((x-1,y-1))
        #前右
        if(x-1>=7 and y+1<=5 and borad[x-1][y+1]<=0):
            last.append((x-1,y+1))
        #后左
        if(x+1<=9 and y-1>=3 and borad[x+1][y-1]<=0):
            last.append((x+1,y-1))
        #右后
        if(x+1<=9 and y+1<=5 and borad[x+1][y+1]<=0):
            last.append((x+1,y+1))
        return last
    
    
    #红帅
    if(now.run_chess=="r7"):
        '''
        1.不出范围
        2.目的地为空或敌方棋子
        '''
        #前
        if(x-1>=7 and borad[x-1][y]<=0):
            last.append((x-1,y))
        #后
        if(x+1<=9 and borad[x+1][y]<=0):
            last.append((x+1,y))
        #左
        if(y-1>=3 and borad[x][y-1]<=0):
            last.append((x,y-1))
        #右
        if(y+1<=5 and borad[x][y+1]<=0):
            last.append((x,y+1))
        return last
    
    
    #黑卒
    if(now.run_chess=="b1"):
        last=[]
        #后
        if(x+1<=9 and borad[x+1][y]>=0):
            last.append((x+1,y))
        #左
        if(y-1>=0 and borad[x][y-1]>=0):
            last.append((x,y-1))
        #右
        if(y+1<=8 and borad[x][y+1]>=0):
            last.append((x,y+1))
      
        return last
   
    
    #黑炮
    if(now.run_chess=="b2"):
        last=[]
        pass
        return last
     
        
    #黑車
    if(now.run_chess=="b3"):
        last=[]
        pass
        return last


    #黑馬
    def b4(self,borad,x,y):
        last=[]
        #前左
        if(x-1>=0 and borad[x-1][y]==0 and x-2>=0 and y-1>=0 and borad[x-2][y-1]>=0):
            last.append((x-2,y-1))
        #前右
        if(x-1>=0 and borad[x-1][y]==0 and x-2>=0 and y+1<=8 and borad[x-2][y+1]>=0):
            last.append((x-2,y+1))
        #后左
        if(x+1<=9 and borad[x+1][y]==0 and x+2<=9 and y-1>=0 and borad[x+2][y-1]>=0):
            last.append((x+2,y-1))
        #后右
        if(x+1<=9 and borad[x+1][y]==0 and x+2<=9 and y+1<=8 and borad[x+2][y+1]>=0):
            last.append((x+2,y+1))
        
        #左前
        if(y-1>=0 and borad[x][y-1]==0 and x-1>=0 and y-2>=0 and borad[x-1][y-2]>=0):
            last.append((x-1,y-2))
        #左后
        if(y-1>=0 and borad[x][y-1]==0 and x+1<=9 and y-2>=0 and borad[x+1][y-2]>=0):
            last.append((x+1,y-2))
        #右前
        if(y+1<=8 and borad[x][y+1]==0 and x-1>=0 and y+2>=0 and borad[x-1][y+2]>=0):
            last.append((x-1,y+2))
        #右后
        if(y+1<=8 and borad[x][y+1]==0 and x+1<=9 and y+2<=8 and borad[x+1][y+2]>=0):
            last.append((x-1,y-2))

        return last


    #黑象
    def b5(self,borad,x,y):
        '''
        1.不过河
        2.目的地为空或敌方棋子
        '''
        last=[]
        #前左
        if(x-2>=0 and y-2>=0 and borad[x-2][y-2]>=0):
            last.append((x-2,y-2))
        #前右
        if(x-2>=0 and y+2<=8 and borad[x-2][y+2]>=0):
            last.append((x-2,y+2))
        #后左
        if(x+2<=4 and y-2>=0 and borad[x+2][y-2]>=0):
            last.append((x+2,y-2))
        #右后
        if(x+2<=4 and y+2<=8 and borad[x+2][y+2]>=0):
            last.append((x+2,y+2))
        return last


    #黑仕
    def b6(self,borad,x,y):
        '''
        1.不出范围
        2.目的地为空或敌方棋子
        '''
        last=[]
        #前左
        if(x-1>=0 and y-1>=3 and borad[x-1][y-1]>=0):
            last.append((x-1,y-1))
        #前右
        if(x-1>=0 and y+1<=5 and borad[x-1][y+1]>=0):
            last.append((x-1,y+1))
        #后左
        if(x+1<=2 and y-1>=3 and borad[x+1][y-1]>=0):
            last.append((x+1,y-1))
        #右后
        if(x+1<=2 and y+1<=5 and borad[x+1][y+1]>=0):
            last.append((x+1,y+1))
        return last


    #黑将
    def b7(self,borad,x,y):
        '''
        1.不出范围
        2.目的地为空或敌方棋子
        '''
        last=[]
        #前
        if(x-1>=0 and borad[x-1][y]<=0):
            last.append((x-1,y))
        #后
        if(x+1<=2 and borad[x+1][y]<=0):
            last.append((x+1,y))
        #左
        if(y-1>=3 and borad[x][y-1]<=0):
            last.append((x,y-1))
        #右
        if(y+1<=5 and borad[x][y+1]<=0):
            last.append((x,y+1))
        return last
    
    
    
    
    
    