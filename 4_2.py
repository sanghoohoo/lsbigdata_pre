import pandas as pd
df=pd.DataFrame({'name'    : ['김지훈','이유진','박동현','김민지'],
                 'english' : [90,80,60,70],
                 'math'    : [50,60,100,20]})
df
df['english']
sum(df['english'])/4
sum(df['math'])/4

fruit_data=pd.DataFrame({'제품' : ['사과','딸기','수박'],
                         '가격' : [1800,1500,3000],
                         '판매량' : [24,38,13]})
                        
fruit_data
