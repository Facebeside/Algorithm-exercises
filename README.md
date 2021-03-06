# Algorithm-exercises

---

算法练习笔记，全部来自[LeetCode](https://leetcode-cn.com/)
最近入手了一本《python数据结构与算法分析》，相关实例在相应的文件夹中。

**update201911/11**




LeetCode序号 | 代码地址
-------- | -------------
200 | [岛屿数量](https://github.com/Facebeside/Algorithm-exercises/blob/master/200-%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.md)
543 | [二叉树的直径](https://github.com/Facebeside/Algorithm-exercises/tree/master/%E4%BA%8C%E5%8F%89%E6%A0%91)
53 | [最大子序和](https://github.com/Facebeside/Algorithm-exercises/blob/master/easy/%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C/maxSubArray.md)


## python学习笔记
---

### 内置函数及用法

#### zip()函数

用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后**返回由这些元组组成的列表**。

>python2中返回的是元组列表，python3中为了减少内存，返回的是一个对象。如果需要返回列表，需要手动list()转换。 

##### 语法

```python
zip([iterable, ...])  # iterable:一个或多个迭代器
```

##### 实例

```python
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
print('----------------')
print(zipped)
print(list(zipped))

nums = ['flower', 'flow', 'fight']
print('----------------')
print(list(zip(*nums)))   # zip(*nums)用于解压
print('----------------')
for i in zip(*nums):
    print(i)

----------------
<zip object at 0x00000203FBF75848>
[(1, 4), (2, 5), (3, 6)]
----------------
[('f', 'f', 'f'), ('l', 'l', 'i'), ('o', 'o', 'g'), ('w', 'w', 'h')]
----------------
('f', 'f', 'f')
('l', 'l', 'i')
('o', 'o', 'g')
('w', 'w', 'h')
```

#### set()函数

创建一个无序不重复元素集，可进行关系测试，删除重复元素，计算交集、差集、并集。返回新的集合对象。

##### 语法

```python
set([iterable])  # iterable:可迭代对象
```

##### 实例

```python
x = set('runoob')
y = set('google')
print('--------')
print('x:', x)
print('y:', y)
print('交集：', x&y)
print('并集：', x|y)
print('差集：', x-y)

--------
x: {'r', 'u', 'n', 'b', 'o'}
y: {'o', 'e', 'l', 'g'}
交集： {'o'}
并集： {'r', 'e', 'b', 'g', 'n', 'o', 'u', 'l'}
差集： {'r', 'u', 'b', 'n'}