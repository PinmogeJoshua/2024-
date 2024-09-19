import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel('C:/Users/avawa/Desktop/file1.xlsx')

# 读取第二个Excel文件
df2 = pd.read_excel('C:/Users/avawa/Desktop/file2.xlsx')

# 处理df2的'id'列中的NaN值，将其填充为一个默认值（例如0），然后转换为整数类型
df2['id'] = df2['id'].fillna(0).astype(int)

# 打印df1和df2的列名和前几行数据
print("df1 columns:", df1.columns)
print("df1 head:\n", df1.head())
print("df2 columns:", df2.columns)
print("df2 head:\n", df2.head())

# 合并两个DataFrame，按'id'和'year'列匹配
merged_df = pd.merge(df1, df2, on=['id', 'year'], how='left')

# 删除合并后的DataFrame中的'id'和'year'列
merged_df = merged_df.drop(columns=['id', 'year'])

# 将合并后的DataFrame写入新的Excel文件
merged_df.to_excel('merged_file.xlsx', index=False)
