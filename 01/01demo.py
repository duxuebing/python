import xlrd
import xlwt
from pathlib import Path, PurePath
# 导入excel和文件操作库

# 指定要合并excel的路径
src_path = '/Users/apple/Desktop/python_productivity-main/文章1代码/调查问卷'
# 指定合并完成的路径
dst_file = '/Users/apple/Desktop/python_productivity-main/文章1代码/result/结果.xls'

# 取得该目录下所有的xlsx格式文件
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xls')]
print(files)
# 准备一个列表存放读取结果
content = []

# 对每一个文件进行重复处理
for file in files:
    # 用文件名作为每个用户的标识
    username = file.stem # 获取文件名
    data = xlrd.open_workbook(file)  #打开文件
    table = data.sheets()[0]
    # 取得每一项的结果
    answer1 = table.cell_value(rowx=4, colx=4)  # 返回对应位置单元格中的数据
    answer2 = table.cell_value(rowx=10, colx=4)
    temp = f'{username},{answer1},{answer2}'
    # 合并为一行先存储起来
    content.append(temp.split(','))  # append() 方法用于在列表末尾添加新的对象。
    print(temp)
    # 输出
    # 韩梅梅,D,B
    # 李雷,D,C

# 准备写入文件的表头
table_header = ['员工姓名', '第一题', '第二题']

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果 2")

# 写入表头
row = 0
col = 0
for cell_header in table_header:
    xlsheet.write(row, col, cell_header)
    col += 1

# 向下移动一行
row += 1
# 取出每一行内容
for line in content:
    col = 0
    # 取出每个单元格内容
    for cell in line:
        # 写入内容
        xlsheet.write(row, col, cell)
        # 向右移动一个单元格
        col += 1
    # 向下移动一行
    row += 1
# 保存最终结果
workbook.save(dst_file)