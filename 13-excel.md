# Excel Operation

用openpyxl

```python
work_sheet = work_book[sheet_name]
v = work_sheet.cell(x,y).value
work_sheet.cell(x,y).value = written_value
work_book.save("path")
```

记得save就好，不然没有实际写到硬盘上。

具体操作可以看这篇文章：https://blog.csdn.net/weixin_41546513/article/details/109555832

自己的一个练习可以看这个：https://gitee.com/vsbug/Classroom_Project/blob/master/main.py
