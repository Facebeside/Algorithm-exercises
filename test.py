## 用于草稿的脚本
# zip()
# a = [1,2,3]
# b = [4,5,6]
# zipped = zip(a,b)
# print(zipped)
# print(list(zipped))

# nums = ['flower', 'flow', 'fight']
# print('----------------')
# print(list(zip(*nums)))   # zip(*nums)用于解压
# print('----------------')
# for i in zip(*nums):
#     print(i)

# set()
x = set('runoob')
y = set('google')
print('--------')
print('x:', x)
print('y:', y)

print('交集：', x&y)
print('并集：', x|y)
print('差集：', x-y)