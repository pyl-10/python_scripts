import pandas as pd
from pandas import Series, DataFrame

# x1 = Series([1, 2, 3, 4])
# x2 = Series(data=[1, 2, 3, 4], index=["a", "b", "c", "d"])
# print(x1)
# print(x2)

# data = {"Chinese": [66, 94, 92, 90, 80], "English": [43, 23, 43, 68, 29], "Math": [90, None, 89, 87, 76]}
# df1 = DataFrame(data)
# df2 = DataFrame(data, index=["zhangfei", "guanyu", "zhaoyun", "huangzhong", "dianwei"], columns=["English", "Chinese", "Math"])
# print(df1)
# print(df2)

# 删除不必要的列或行
# df3 = df2.drop(columns=["Chinese"], index=["zhangfei"])
# print(df3)

# 重命名 行的名字
# df2.rename(columns={"Chinese": "YuWen", "English": "Yingyu"}, inplace=True)
# print(df2)

# 去重复的值
# df2 = df2.drop_duplicates()

# 更改数据格式
# df2["Chinese"].astype("str") # 把chinese字段的值改为str类型
# df2["Chinese"].astype(np.int64)

# 数据间的空格
# df2["Chinese"] = df2["Chinese"].map(str.strip) # 左右两边的空格
# df2["Chinese"] = df2["Chinese"].map(str.lstrip) # 左边空格
# df2["Chinese"] = df2["Chinese"].map(str.rstrip) # 右边空格

# df2["Chinese"] = df2["Chinese"].str.strip("$")  # 去除数据中的特殊符号

# 全部大写
# df2.columns = df2.columns.str.upper()
# 全部小写
# df2.columns = df2.columns.str.lower()
# 首字母大写
# df2.columns = df2.columns.str.title()

# 查找空值字段
# print(df2.isnull())
# print(df2.isnull().any()) # 查找哪一列存在空值

# 大写转化
# df2["Math"] = df2["Math"].apply(str.upper)

# def double_df(x):
#     return 2*x
# df2[u"Math"] = df2[u"Math"].apply(double_df)
# print(df2)

# 新增两列，new1列是语文英语成绩之和的m倍，new2列是语文和英语成绩之和的n倍
# def plus(df, n, m):
#     df["new1"] = (df[u"Chinese"] + df[u"English"]) * m
#     df["new2"] = (df[u"Chinese"] + df[u"English"]) * n
#     return df
# axis=1表示按照以列为轴进行操作，axis=0表示按照以行为轴进行操作
# df1 = df1.apply(plus, axis=1, args=(2, 3, ))
# print(df1)

# 统计函数
# df1 = DataFrame({"name": ["ZhangFei", "GuanYu", "a", "b", "c"], "data1": range(5)})
# print(df1.describe())

# 连接两个DataFrame 类似连接数据表
# df1 = DataFrame({"name": ["ZhangFei", "GuanYu", "a", "b", "c"], "data1": range(5)})
# df2 = DataFrame({"name": ["ZhangFei", "GuanYu", "A", "B", "C"], "data2": range(5)})
# df3 = pd.merge(df1, df2, on="name")
# df3 = pd.merge(df1, df2, how="inner")
# df3 = pd.merge(df1, df2, how="left")
# df3 = pd.merge(df1, df2, how="right")
# df3 = pd.merge(df1, df2, how="outer")
# print(df1)
# print(df2)
# print(df3)

# 使用pandas操作sql
# from pandasql import sqldf, load_meat, load_births
# df2 = DataFrame({"name": ["ZhangFei", "GuanYu", "A", "B", "C"], "data2": range(5)})
# pysqldf = lambda sql: sqldf(sql, globals())
# sql = "select * from df2 where name = 'ZhangFei'"
# print(pysqldf(sql))

data = {"语文": [66, 95, 95, 90, 80, 80], "英语": [65, 85, 92, 88, 90, 90], "数学": [None, 98, 96, 77, 90, 90]}
# df4 = DataFrame(data)
df5 = DataFrame(data, index=["张飞", "关羽", "赵云", "黄忠", "典韦", "典韦"])
print(df5)
# 去重复的值
df5 = df5.drop_duplicates()
# 用 0 替换 空值
df5 = df5.fillna(0)
print(df5)
def sum(df):
    df[u"总分"] = (df[u"语文"] + df[u"数学"] + df[u"英语"])
    return df
newDF = df5.apply(sum, axis=1)
print(newDF)

# 对年龄中的缺失值使用平均年龄进行填充替换
df["Age"].fillna(df["Age"].mean(), inplace=True)

# value_counts获取最高频次的数据，然后再进行缺失数据的替换
age_maxf = train_features["Age"].value_counts().index[0]
train_features["Age"].fillna(age_maxf, inplace=True)

# 删除全空的行
df5.dropna(how="all", inplace=True)

# 单位转换，将 磅 lbs 转化为 千克 kgs
# 获取weight数据列中单位为lbs的数据
rows_with_lbs = df["weight"].str.contains("lbs").fillna(False)
print(df[rows_with_lbs])
# 将lbs转换为kgs, 2.2lbs=1kgs
for i, lbs_row in df[rows_with_lbs].iterrows():
    # 截取从头开始到倒数第三个字符之前，即去掉lbs
    weight = int(float(lbs_row["weight"][:-3])/2.2)
    df.at[i, "weight"] = "{}kgs".format(weight)

# 删除非 ASCII 字符
df["first_name"].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
df["last_name"].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)

# 切分名字，删除源数据列
df[["f_name", "l_name"]] = df["name"].str.split(expand=True)
df.drop("name", axis=1, inplace=True)

# 删除重复数据行
df5.drop_duplicates([])


