import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 산점도도
mpg=pd.read_csv('data/mpg.csv')
mpg
sns.scatterplot(data=mpg, x='displ', y='hwy')
plt.show()
plt.clf()

sns.scatterplot(data=mpg, x='displ', y='hwy').set(xlim=[3,6],ylim=[10,30])
plt.show()
plt.clf()

sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
plt.show()
plt.clf()

sns.scatterplot(data=mpg, x='cty', y='hwy')
plt.show()
plt.clf()

mdw=pd.read_csv('data/midwest.csv')
sns.scatterplot(data=mdw, x='poptotal', y='popasian').set(xlim=[0,500000],ylim=[0,10000])
plt.show()
plt.clf()

# 막대 그래프
df_mpg=mpg.groupby('drv').agg(mean_hwy=('hwy','mean'))
df_mpg
df_mpg=mpg.groupby('drv',as_index=False).agg(mean_hwy=('hwy','mean'))
df_mpg
df_mpg=df_mpg.sort_values('mean_hwy',ascending=False)

sns.barplot(data=df_mpg, x='drv', y='mean_hwy', hue='drv')
plt.show()
plt.clf()

df_mpg=mpg.groupby('drv',as_index=False).agg(n=('drv','count'))
df_mpg

sns.barplot(data=df_mpg, x='drv', y='n', hue='drv')
plt.show()
plt.clf()

sns.countplot(data=mpg, x='drv', hue='drv', order=['4', 'f', 'r'])
plt.show()
plt.clf()

mpg['drv'].unique()
df_mpg['drv'].unique()

mpg['drv'].value_counts().index
sns.countplot(data=mpg, x='drv', hue='drv', order=mpg['drv'].value_counts().index)
plt.show()
plt.clf()

mpg
mpg_suv=mpg.query('category=="suv"')
suv_cty=mpg_suv.groupby('manufacturer',as_index= False)\
    .agg(cty_mean=('cty','mean'))
suv_cty
suv_cty5=suv_cty.sort_values('cty_mean',ascending=False).head(5)
suv_cty5
sns.barplot(data=suv_cty5, x='manufacturer', y='cty_mean', hue='manufacturer')
plt.show()
plt.clf()

mpg_cat=mpg.groupby('category',as_index=False).agg(n=('category','count'))\
    .sort_values('n',ascending=False)
sns.barplot(data=mpg_cat, x='category', y='n', hue='category')
plt.show()
plt.clf()

# 선그래프
economics=pd.read_csv('data/economics.csv')
economics.head()
sns.lineplot(data=economics, x='date', y='unemploy')
plt.show()
plt.clf()

economics['date2']=pd.to_datetime(economics['date'])
economics.info()

economics[['date','date2']]
economics['date2'].dt.year
economics['date2'].dt.month
economics['date2'].dt.day
economics['year']=economics['date2'].dt.year
economics.head()
sns.lineplot(data=economics, x='year', y='unemploy', errorbar=None)
plt.show()
plt.clf()

sns.lineplot(data=economics, x='year', y='psavert', errorbar=None)
plt.show()
plt.clf()

economics['month']=economics['date2'].dt.month
economics
eco_2014=economics.query('year==2014')
eco_2014
sns.lineplot(data=eco_2014, x='month', y='psavert', errorbar=None)
plt.show()
plt.clf()

#상자 그림
sns.boxplot(data=mpg, x='drv', y='hwy')
plt.show()
plt.clf()

mpg_small=mpg.query('category in["compact","subcompact","suv"]')
sns.boxplot(data=mpg_small, x='category', y='cty', hue='category')
plt.show()
plt.clf()
