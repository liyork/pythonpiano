#coding=utf-8
import pandas as pd

# 学生成绩表
df_grade = pd.read_excel("学生成绩表.xlsx") 
df_grade.head()

# 学生信息表
df_sinfo = pd.read_excel("学生信息表.xlsx") 
df_sinfo.head()

# 只筛选第二个表的少量的列
df_sinfo = df_sinfo[["学号", "姓名", "性别"]]
df_sinfo.head()

# join
df_merge = pd.merge(left=df_grade, right=df_sinfo, left_on="学号", right_on="学号")
df_merge.head()

# 将columns变成python的列表形式
new_columns = df_merge.columns.to_list()

# 按逆序insert，会将"姓名"/"性别"放到"学号"的后面
for name in ["姓名", "性别"][::-1]:
    new_columns.remove(name)
    new_columns.insert(new_columns.index("学号")+1, name)


df_merge = df_merge.reindex(columns=new_columns)
df_merge.head()

df_merge.to_excel("合并后的数据表.xlsx", index=False)
