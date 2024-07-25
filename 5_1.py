import pandas as pd
exam=pd.read_csv('data/exam.csv')
exam
exam.head()
exam.head(10)
exam.tail()
exam.tail(10)
exam.shape
exam.info()
exam.describe()

mpg=pd.read_csv('data/mpg.csv')
mpg
mpg.head()
mpg.tail()
mpg.shape
mpg.info()
mpg.describe()
mpg.describe(include='all')

type(df)
