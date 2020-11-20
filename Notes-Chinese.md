# Notes

## 09-类

## 10-文件和异常

### 10.1-open_and_read

这是打开文件的入门操作。

    with open(filename) as file_object:
        lines = file_object.read()
        ## do what u want 

函数open()接受文件名，然后在当前目录下查找查找指定的文件。  
函数open()返回一个表示文件的对象。

关键字with在不再需要访问文件后将其关闭。  
Python自会在合适的时候自动将其关闭。

你也可以调用open()和close()来打开和关闭文件，

### 10.2-read_by_line

使用 read() 函数，会把一整个file的内容都读入到一个string里。  
逐行读取没有对应的函数，而是通过for循环来实现：

    with open(filename) as file_object:
        for line in file_object:
            # do what u want

这样的话，每个line的末尾还是会有一个**换行符**，  
可以通过 rstripe() 函数在输出的时候处理掉
