import xlwt
from xlutils.copy import copy

dst_file = '/Users/apple/Desktop/python_productivity-main/mycode/file/test.xls'

workbook = xlwt.Workbook(encoding='utf-8') # 创建新的workbook（其实就是创建新的excel）
xlsheet = workbook.add_sheet("Sheet5")  # 创建新的sheet表

# 写入内容,假设取出的内容是value
xlsheet.write(0, 0, ['duxuebing 5'])

# 保存文件
workbook.save(dst_file)

