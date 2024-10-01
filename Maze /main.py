import time
import re
def mazewalking(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):
    #使用dfs，方向優先順序上(up)、右(right)、下(down)、左(left)
    #對的路線=2，已走且錯=-1，不確定的路=2
    while position_row!=ending_row or position_col!=ending_col:
        time.sleep(1)
        print("現在的位置是[{}][{}]".format(position_row,position_col))
        directioncount=howmanydirection(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)##確認有幾個方向可以走
        if directioncount == 0:
            (position_row,position_col)=zerodirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)##只有0個方向
        elif directioncount == 1:
            (position_row,position_col)=onedirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)##只有1個方向
        else:
            ##2種方向選擇
            (position_row,position_col)=moredirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)##有多個方向
    maze[ending_row][ending_col]=3
    time.sleep(1)
    print('正確路線是3。')
    print('曾經走過，但是錯的是4')
    printmaze(maze)
    print("到終點")##function 剩下的資料，return等等(最後寫)



def howmanydirection(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##確認有多少個方向可以走
    directioncount=0##確認有多少個方向可以走
    if position_row> 0:
        if maze[position_row-1][position_col]==0 or maze[position_row-1][position_col]=='0':
            directioncount=directioncount+1
    if position_col+1 < maze_len:
        if maze[position_row][position_col+1]==0 or maze[position_row][position_col+1]=='0' :
            directioncount=directioncount+1
    if position_row+1 < maze_len:
        if maze[position_row+1][position_col]==0 or maze[position_row+1][position_col]=='0' :
            directioncount=directioncount+1
    if position_col > 0:
        if maze[position_row][position_col-1]==0 or maze[position_row][position_col-1]=='0' :
            directioncount=directioncount+1
    return directioncount   
def findpath(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##選擇方向函式，並把方向選擇結果給renew()
    direct=0##右=1;下=2;左=3;上=4
    if position_col+1 < maze_len:
        if maze[position_row][position_col+1]==3 or maze[position_row][position_col+1]=='0' :
            direct=1##右
    if direct==0:
        if position_row+1 < maze_len:
            if maze[position_row+1][position_col]==3 or maze[position_row+1][position_col]=='0':
                direct=2##下
    if direct==0:
        if position_col > 0:
            if maze[position_row][position_col-1]==3 or maze[position_row][position_col-1]=='0' :
                direct=3##左
    if direct==0:
        if position_row > 0:
            if maze[position_row-1][position_col]==3 or maze[position_row-1][position_col]=='0' :
                direct=4##上
    return direct
##功能函式
def choosedirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##選擇方向函式，並把方向選擇結果給renew()
    direct=0##右=1;下=2;左=3;上=4
    if position_col+1 < maze_len:
        if maze[position_row][position_col+1]==0 or maze[position_row][position_col+1]=='0' :
            direct=1##右
    if direct==0:
        if position_row+1 < maze_len:
            if maze[position_row+1][position_col]==0 or maze[position_row+1][position_col]=='0':
                direct=2##下
    if direct==0:
        if position_col > 0:
            if maze[position_row][position_col-1]==0 or maze[position_row][position_col-1]=='0' :
                direct=3##左
    if direct==0:
        if position_row > 0:
            if maze[position_row-1][position_col]==0 or maze[position_row-1][position_col]=='0' :
                direct=4##上
    return direct

def renew(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##藉由choosedirect()給的方向選擇更新當前位置
    if direct==1:
        position_col=position_col+1
    elif direct==2:
        position_row=position_row+1
    elif direct==3:
        position_col=position_col-1
    elif direct==4:
        position_row=position_row-1
    return (position_row,position_col)

def goback(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##當走到底時，回頭
    while True:
        if position_row+1 < maze_len:
            if maze[position_row+1][position_col]==0 :
                break
        if position_col+1 < maze_len:
            if maze[position_row][position_col+1]==0 :
                break
        if position_row > 0:
            if maze[position_row-1][position_col]==0 :
                break
        if position_col > 0:
            if maze[position_row][position_col-1]==0 :
                break
        ##上面用來判斷當前位置有沒有回到岔路，若有則跳離
        maze[position_row][position_col]=4##錯路
        n=0##用來判斷是否已經走下一步了
        if position_row+1 < maze_len:
            if maze[position_row+1][position_col]==3 :
                position_row=position_row+1
                n=1
        if n==0:
            if position_col+1 < maze_len:
                if maze[position_row][position_col+1]==3 :
                    position_col=position_col+1
                    n=1
        if n==0:
            if position_row > 0:
                if maze[position_row-1][position_col]==3 :
                    position_row=position_row-1
                    n=1
        if n==0:
            if position_col > 0:
                if maze[position_row][position_col-1]==3 :
                    position_col=position_col-1
                    n=1
    return(position_row,position_col) 
##           
def onedirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##一個方向
    maze[position_row][position_col]=3#確定
    direct=choosedirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    print(f"direct是{direct} ")
    (position_row,position_col)=renew(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    printmaze(maze)
    return (position_row,position_col)

def moredirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##多個方向
    maze[position_row][position_col]=3#確定
    direct=choosedirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    (position_row,position_col)=renew(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    printmaze(maze)
    return (position_row,position_col)  

def zerodirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len):##0個方向，到底了
    maze[position_row][position_col]=4#錯
    (position_row,position_col)=goback(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    print(f"現在是maze[{position_row}][{position_col}] ")
    direct=choosedirect(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    (position_row,position_col)=renew(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
    printmaze(maze)
    return (position_row,position_col)   

def printmaze(maze):
    print('迷宮是:')
    for i in range(len(maze)):
        for j in range(len(maze[i])):  
            if isinstance(maze[i][j], str):
                print(f"'{maze[i][j]}'", end=" ")
            else:
                print(" ", end="")
                print(maze[i][j], end=" ")
                print(" ", end="")
        print(' ')
#####

#主程式

#####
print("請輸入迷宮檔案的路徑，「請記得輸入檔名以及後面輸入.txt」")
file_path =input("範例如下D:\\vs_code_file\python\cycu_datastructure\hw6_maze\簡單版_10x10_迷宮.txt")

with open(file_path, 'r') as file:
    lines = file.readlines()

lines = lines[1:]  
maze = []

for line in lines:
    line_cleaned = line.strip().strip('[ ]\n,')
    if not line_cleaned:  
        continue
    row = []
    for x in line_cleaned.split(','):
        x = x.strip()
        if x == "'0'":  
            row.append('0')  
        elif x == "1]])":  
            row.append('1]])')
        else:
            try:
                row.append(int(x))  
            except ValueError:  
                continue
    maze.append(row)
maze_len = len(maze)#紀錄maze行數
maze[maze_len-1][maze_len-1]=1

# print(maze)
time.sleep(1)

# print(maze_len)
printmaze(maze)
count=0#紀錄是否有位置已被標示為起點，即第一個搜尋到的'0'為起點，第二個為終點
for i in range(0,maze_len,1):
    for j in range(0,maze_len,1):
        if maze[i][j]=='0':
            if count==0:
                starting_row=i
                starting_col=j
                count=1
            else:
                ending_row=i
                ending_col=j
print(f"起點是maze[{starting_row}][{starting_col}] ")
print(f"終點是maze[{ending_row}][{ending_col}]")

##建立現在位置
position_row=starting_row
position_col=starting_col
##

#建立找終點過程所需變數
direct=0
#
mazewalking(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)
position_row=starting_row
position_col=starting_col

while position_row!=ending_row or position_col!=ending_col:
    print(f"({position_row},{position_col})->", end="")
    maze[position_row][position_col]=2
    direct=findpath(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)##為3的路，是結果
    (position_row,position_col)=renew(maze,starting_row,starting_col,ending_row,ending_col,position_row,position_col,direct,maze_len)

print(f"({position_row},{position_col}) 到終點")
