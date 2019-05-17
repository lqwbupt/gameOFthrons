import pandas as pd

df_new = pd.read_csv('test.csv')
writer = pd.ExcelWriter('test.xlsx')
df_new.to_excel(writer, index = False)
writer.save()