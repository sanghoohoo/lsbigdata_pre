import pandas as pd
import numpy as np
df=pd.DataFrame({
    'sex':['M','F',np.nan,'M','F'],
    'score':[5,4,3,4,np.nan]
})
df

pd.isna(df)
pd.isna(df).sum()
df_nomiss=df.dropna(subset=['score','sex'])
df_nomiss
df_nomiss2=df.dropna()
df_nomiss2

exam=pd.read_csv('data/exam.csv')
exam.loc[[2,7,14],['math']]=np.nan
exam
exam['math'].mean()
exam['math']=exam['math'].fillna(55)
exam
exam['math'].isna().sum()

mpg=pd.read_csv('mpg.csv')
mpg.loc[[64,123,130,152,211],'hwy']=np.nan
mpg.isna().sum()
mpg.dropna().groupby('drv').agg(mean_hwy=('hwy','mean'))

df=pd.DataFrame({
    'sex':[1,2,1,3,2,1],
    'score':[5,4,3,4,2,6]
})
df
df['sex'].value_counts().sort_index()
df['score'].value_counts().sort_index()
df['sex']=np.where(df['sex']==3,np.nan,df['sex'])
df
df['score']=np.where(df['score']==6,np.nan,df['score'])
df
df.dropna(subset=['sex','score']).groupby('sex').agg(mean_score=('score','mean'))

mpg=pd.read_csv('data/mpg.csv')
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(data=mpg,y='hwy')
plt.show()
pct25=mpg['hwy'].quantile(.25)
pct25
pct75=mpg['hwy'].quantile(.75)
pct75
iqr=pct75-pct25
iqr
pct25-1.5*iqr
pct75+1.5*iqr
mpg['hwy']=np.where((mpg['hwy']<4.5)|(mpg['hwy']>40.5),np.nan,mpg['hwy'])
mpg['hwy'].isna().sum()
mpg.dropna(subset='hwy').groupby('drv').agg(mean_hwy=('hwy','mean'))

mpg.loc[[9,13,57,92],'drv']='k'
mpg.loc[[28,42,128,202],'cty']=[3,4,39,42]
mpg['drv'].value_counts().sort_index()
mpg['drv']=np.where(mpg['drv'].isin(['4','f','r']),mpg['drv'],np.nan)
mpg['drv'].value_counts().sort_values()
plt.clf()
sns.boxplot(data=mpg,y='cty')
plt.show()
per25=mpg['cty'].quantile(.25)
per75=mpg['cty'].quantile(.75)
per25
per75
iqr=per75-per25
iqr
per25-iqr*1.5
per75+iqr*1.5
mpg['cty']=np.where((mpg['cty']<6.5)|(mpg['cty']>26.5),np.nan,mpg['cty'])
mpg['cty'].isna().sum()
plt.clf()
sns.boxplot(data=mpg,y='cty')
plt.show()
mpg.dropna(subset=['drv','hwy']).groupby('drv').agg(mean_cty=('cty','mean'))
