import xlrd

file = '/Users/apple/Desktop/python_productivity-main/mycode/file/test.xls'

data = xlrd.open_workbook(file) #打开文件
table = data.sheets()[0]  #通过索引顺序获取，例如：0是第一个sheet，1是第二个sheet
value = table.cell_value(rowx=4, colx=4) # 返回对应位置单元格中的数据，Sheet.cell_value(row, column, new_value=None)，row：从0开始的行索引 column：从0开始的列索引
print(value)