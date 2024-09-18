"""
这个脚本用于将三个Excel表格的数据根据'id'和'year'列进行合并。
合并后的数据将保存到一个新的Excel文件中。

步骤：
1. 读取三个Excel文件到DataFrame。
2. 将多级列名展平（如果有）。
3. 根据'id'和'year'将'table2'和'table3'的数据合并到'table1'中。
4. 保存合并后的结果到新的Excel文件。

依赖：
- pandas
"""

import pandas as pd

# 读取Excel文件
table1 = pd.read_excel('C:/Users/avawa/Desktop/table1.xlsx')
table2 = pd.read_excel('C:/Users/avawa/Desktop/table2.xlsx')
table3 = pd.read_excel('C:/Users/avawa/Desktop/table3.xlsx')

# 将多级列名展平（如果有）
if isinstance(table2.columns, pd.MultiIndex):
    table2.columns = ['_'.join(map(str, col)).strip('_') for col in table2.columns.values]
if isinstance(table3.columns, pd.MultiIndex):
    table3.columns = ['_'.join(map(str, col)).strip('_') for col in table3.columns.values]

# 合并table1和table2
merged_table = pd.merge(table1, table2, how='left', on=['id', 'year'])

# 合并merged_table和table3
merged_table = pd.merge(merged_table, table3, how='left', on=['id', 'year'])

# 选择需要的列
result = merged_table[['id', 'year'] + [col for col in merged_table.columns if col not in ['id', 'year']]]

# 保存结果到新的CSV文件
result.to_csv('C:/Users/avawa/Desktop/merged_table.csv', index=False)
