# def moveTower(height, fromPole, toPole, withPole):
#     if height > 1:
#         moveTower(height - 1, fromPole, withPole, toPole)
#         moveDisk(fromPole, toPole)
#         moveTower(height - 1, withPole, toPole, fromPole)

# def moveDisk(fp, tp):
#     print("moving disk from %d to %d\n" % (fp, tp))

def move(n,a,b,c):
    if n == 1:      #递归的收敛条件,当n为1,时,执行移动的操作
        print('move:',a,'-->',c)   #打印 move 为字符串,a和c是参数
        return
    move(n-1,a,c,b)    #先把n-1个盘子,从a移动到b
    move(1,a,b,c)      #再将剩下的1个盘子,从a移动到c
    move(n-1,b,a,c)    #柱子b上面有n-1个盘子,再将盘子从b,借助a,移动到c

