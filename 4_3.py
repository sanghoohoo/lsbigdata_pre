import pandas as pd
df_exam=pd.read_excel('data/excel_exam.xlsx')
df_exam

sum(df_exam['english'])/20
sum(df_exam['science'])/20

x=[1,2,3,4,5]
len(x)

df=pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
df
len(df)

len(df_exam)
sum(df_exam['english'])/len(df_exam)
sum(df_exam['science'])/len(df_exam)


df_csv_exam=pd.read_csv('data/exam.csv')
df_csv_exam

df_midterm=pd.DataFrame({'english':[90,80,60,70],
                         'math'   :[50,60,100,20],
                         'nclass' :[1,1,2,2]})
df_midterm
df_midterm.to_csv('output_newdata.csv')
