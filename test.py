"""
N:月饼种类
D:最大需求量
number:月饼库存
price：月饼总售价
"""
# N, D = list(map(int, input().split()))
# number = list(map(float, input().split()))
# price = list(map(float, input().split())) 
# # 每种月饼的单价
# rate = { i: price[i] / number[i] for i in range(N) }
# # 对月饼的单价进行排序
# order = sorted(rate, key=lambda i: rate[i], reverse=True)
# # 总收益3 
# money = 0
# for i in order:
#     if D >= number[i]:
#         money += price[i]
#         D -= number[i]
#     else:
#         money += D * rate[i]
#         break
# print("%.2f" % money)
# lst = input().split()
# k,m = int(lst[0]),int(lst[1])
# num = list(map(float,input().split()))
# price = list(map(float,input().split()))
# price_s = [[price[i]/num[i],i] for i in range(k)]
# price_s.sort(reverse=1)
 
# money = 0
# sum_yb = 0
# for p,inx in price_s:
#     sum_yb += num[inx]
#     if sum_yb <= m:
#         money += price[inx]
#     else:
#         money += p* (num[inx]-(sum_yb-m))
#         break
# print("%.2f"%money)3 

a=int(input())
b=int(a**0.5)
strat=0  #记录连续乘积串的首数字
len=1 # 记录连续乘积串的长度
maxlen=0
# 只需要知道 首数字 和 长度   就可以输出求出的连续乘积串  提高了算法效率
for i in range(2,b+1):
    if a%i==0:
        x=i
        for k in range(i+1,b+2):
            x=x*k
            if a%x==0 and x<=a:
                len+=1
            else:
                 break
        if len>maxlen: #内层for结束循环后，判断当前序列长度，如果大于最大长度，更新maxlen
            maxlen=len
            strat=i
        len=1      #每次内层循环结束后，都要使len=1
if maxlen==0:      #质数或0
    print("%d\n%d"%(1,a))
else:
    print("%d\n%d"%(maxlen,strat),end="")
    l=1
    while l<maxlen:
        print("*%d"%(strat+l),end="")
        l+=1