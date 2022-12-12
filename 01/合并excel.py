from pathlib import Path, PurePath  #pathlib 模块 -- 面向对象的文件系统路径。

# 指定要合并excel的路径
src_path = '/Users/apple/Desktop/python_productivity-main/文章1代码/调查问卷'

# 取得该目录下所有的xlsx格式文件
# 获取 src_path 变量指向的路径下所有的文件，使用一个 if 语句用于条件判断，只提取.xlsx 结尾的文件
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xls')]  # Path.iterdir() 当路径指向一个目录时，产生该路径下的对象的路径。
print(files)