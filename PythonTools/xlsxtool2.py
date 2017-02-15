import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
#确认列和没列填充的开始字符
col1=[
    ['客户名称','某某某的kehu'],
    ['客户编号','num'],
    ['客户地址','address'],
    ['客户备注','notice'],
    ['客户状态','status'],
    ['客户分级','level']
]


a=0
while (a<len(col1)):
    i = 0
    worksheet.write(0, a, col1[a][0])
    while (i<100):
        worksheet.write(i+1,a,col1[a][1]+str(i))  #+str(i)
        i=i+1
    a=a+1

# Widen the first column to make the text clearer.
#worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})

# Write some simple text.
#worksheet.write('A1', 'Hello')

# Text with formatting.
#worksheet.write('A2', 'World迭代', bold)


# Write some numbers, with row/column notation.
#worksheet.write(2, 2, 123)
#worksheet.write(3, 2, 123.456)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')


workbook.close()
