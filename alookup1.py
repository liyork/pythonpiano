#coding=utf-8

import openpyxl
import pandas as pd
df1 = pd.DataFrame(pd.read_excel('table1.xlsx',sheet_name = 'Sheet1'))
df2 = pd.DataFrame(pd.read_excel('table2.xlsx',sheet_name = 'Sheet1'))

#只在table1添加分数列，不添加排名列
result = pd.merge(df1,df2.loc[:,['学号','分数']],how='left',on = '学号')

writer = pd.ExcelWriter('result.xlsx')
result.to_excel(writer,index=False)
writer.save()
