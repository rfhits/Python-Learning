# Python常用

## pip

### 查看pip版本

pip -V

### 查看已经安装的包

pip list

## 列表

### 列表的解析

[expr for iter_var in list if cond_expr]
按我个人理解哈：

[func(i) for i in list if filter(i)]
三个关键：expression、for-in、if

### 字符串数组转int数组

[int(i) for i in s]
### 利用字典转换key_list

这就是利用了列表的解析

dct = {'a':3, 'b':3,'c':5,'d':3}
key_list = ['c', 'd', 'a', 'b', 'd']
val_list = [dct[k] for k in key_list]
val_list = [5, 3, 3, 3, 3]
