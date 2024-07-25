df=pd.DataFrame({'var1':[4,3,8], 'var2':[2,6,1]})
df
df['var_sum']=df['var1']+df['var2']
df
df['var_mean']=(df['var1']+df['var2'])/2
df
mpg=pd.read_csv('data/mpg.csv')
mpg
mpg['total']=(mpg['cty']+mpg['hwy'])/2
mpg.head()
sum(mpg['total'])/len(mpg)
mpg['total'].mean()

import matplotlib.pyplot as plt
mpg['total'].describe()
mpg['total'].plot.hist()
plt.show()

import numpy as np
mpg['test']=np.where(mpg['total']>=20, 'pass','fail')
mpg.head()

mpg['test'].value_counts()
count_test=mpg['test'].value_counts()
count_test.plot.bar(rot=0)
plt.show()

mpg['grade']=np.where(mpg['total']>=30,'A',
             np.where(mpg['total']>=20,'B','C'))
mpg.head()                      

count_grade=mpg['grade'].value_counts().sort_index()
count_grade
count_grade.plot.bar(rot=0)
plt.show()

mpg['grade2']=np.where(mpg['total']>=30,'A',
              np.where(mpg['total']>=25,'B',
              np.where(mpg['total']>=20,'C','D')))
mpg.head()

mpg['size']=np.where((mpg['category']=='compact')|
                    (mpg['category']=='subcompact')|
                    (mpg['category']=='2seater'),
                    'small','large')
mpg.head()
mpg['size'].value_counts()

mpg['size']=np.where(mpg['category'].isin(['compact','subcompact','2seater']),
                     'small','large')
mpg['size'].value_counts()

mdw=pd.read_csv('data/midwest.csv')
mdw
mdw.describe()
mdw=mdw.rename(columns={'poptotal':'total', 'popasian':'asian'})
mdw
mdw['portion']=mdw['asian']/mdw['total']*100
mdw
mdw['portion'].plot.hist()
plt.clf()
plt.show()
mdw['portion_amt']=np.where(mdw['portion']>mdw['portion'].mean(),'large','small')
mdw.head()
count_amt=mdw['portion_amt'].value_counts()
count_amt.plot.bar(rot=0)
plt.show()
