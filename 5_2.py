df_raw=pd.DataFrame({'var1':[1,2,3], 'var2':[2,3,2]})
df_raw
df_new=df_raw.copy()
df_new
df_new=df_new.rename(columns={'var2' : 'v2'})
df_new

df_mpg=pd.read_csv('data/mpg.csv')
df_mpg
df_mpg_new=df_mpg.copy()
df_mpg_new
df_mpg_new=df_mpg_new.rename(columns={'cty':'city', 'hwy':'highway'})
df_mpg_new.head()
