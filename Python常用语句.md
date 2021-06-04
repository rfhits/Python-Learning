# Python常用

## pip

### 查看pip版本

pip -V

### 查看已经安装的包

pip list

## IO

### 保留小数

```python
round(x, 2)
round(x)
```

默认保留到整数，注意`round()`不是真正的四舍五入，包括`.2f`等方法，都不是真正的“四舍五入”。

### +法

在Java里，输出可以用`+`号连接，因为`str + int= str`强转类型转换的存在。

在Python中，如果用`,`分割，输出会多一个空格

解决方法是直接强转为`str`再输出。

```python
print(str(rate*100) + "%")
```

### ASCII

函数`chr`和`ord`。

`chr(65)`就是`'A'`，`ord("A")`就是`65`。

```python
print(chr(65))
print(ord("A"))
```

## list

### index()

index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

index()方法语法：

```
list.index(x[, start[, end]])
```

获取第一个最简单了，`list.index(x)`

请确保元素`x`在list中，否则会报错。

### sort()

`list.sort()`默认升序排列

要自定排序方法，可以用lambda表达式

```python
lst = [(2, 1, 3), (1, 2, 3), (4, 3, 2)]
lst.sort(key = lambda x: x[0], reverse = False )
```

`list.sort(key = function, reverse = boolean)`

本意是接受一个function，这个function的参数是list这个“可迭代对象”中的对象，返回一个数作为比较的依据。

```python
lst = [(2, 1, 3), (1, 2, 3), (4, 3, 2)]
def index2(item):
    return item[2]
lst.sort(key = index2, reverse = False )
```

一定一定要把`key = xxx, reverse = xxx` 写上。

多依据排序装载自[此](https://blog.csdn.net/y12345678904/article/details/77507552)。

对tuple进行排序，先按照第一个元素升序，如果第一个元素相同，再按照第二个元素降序排列。

L = [(12, 12), (34, 13), (32, 15), (12, 24), (32, 64), (32, 11)]
L.sort(key=lambda x: (x[0], -x[1]))
print(L)


### 列表的解析

`[expr for iter_var in list if cond_expr]`

按我个人理解哈：

`[func(i) for i in list if filter(i)]`

三个关键：expression、for-in、if

### 合并

1. `+`
2. listA.extend(listB)

### list[n * 0]

可以利用list的解析生成一个含有n个0的list

`lst = [0 for i in range(n)]`

### 字符串数组转int数组

[int(i) for i in s]

### 利用字典转换key_list

这就是利用了列表的解析

```python
dct = {'a':3, 'b':3,'c':5,'d':3}
key_list = ['c', 'd', 'a', 'b', 'd']
val_list = [dct[k] for k in key_list]
val_list = [5, 3, 3, 3, 3]
```

## string

### count

统计字符串中子串出现的次数。可以指定查找的起点和终点。

```python
str.count(substr, start, end)
```

## datetime

```python
from datetime import *
start = date(yyyy, mm, dd)
end = date(yyyy, mm, dd)
```

date有属性`date.year date.month date.day`和方法`date.weekday()`

### 已知日期输出星期几

```python
d = date(yyyy, mm, dd)
print(d.weekday())
```
