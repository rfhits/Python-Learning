with open('pi_digits.txt') as file_object: 
    contents = file_object.read() 
print(contents)

# 函数open() 接受一个参数：要打开的文件的名称。
# Python在当前执行的文件所在的目录中查找指定的文件。
# 在这个示例中，当前运行的是file_reader.py，
# 因此Python在file_reader.py所在的目录中 查找pi_digits.txt。

# 函数open()返回一个表示文件的对象。
# 在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象；
# Python将这个对象存储在我们将 在后面使用的变量中。 
# 关键字with在不再需要访问文件后将其关闭。
# 
# 
# 在这个程序中，注意到我们调用了open()，但没有调用close()；你也可以调用open()和close()来打开和关闭文件，
# 但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调 用close()，你会发现需要使用文件时它已关关闭闭  （无法访问），这会导致更多的错误。
# 
# 并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可 让Python去确定：你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。 
# 并将其作为一个长长的字符串存储在变量contents中。