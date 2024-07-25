import pandas as pd
exam=pd.read_csv('data/exam.csv')
exam
exam.query('nclass==1')
exam.query('nclass==2')
exam.query('nclass !=1')
exam.query('nclass !=3')
exam.query('math>50')
exam.query('math<50')
exam.query('english>=50')
exam.query('english<=80')
exam.query('nclass==1&math>=50')
exam.query('nclass==2&english>=80')
exam.query('english<90&science<50')
exam.query('nclass==1|nclass==3|nclass==5')
exam.query('nclass in [1,3,5]')
nclass1=exam.query('nclass==1')
nclass2=exam.query('nclass==2')
nclass1['math'].mean()
nclass2['math'].mean()

df=pd.DataFrame({'sex':['F','M','F','M'],
                 'country':['Korea','China','Japan','USA']})
df
df.query("sex=='M' & country=='China'")
df.query('sex=="F" & country=="Korea"')
var=3
exam.query('nclass==@var')

csv
csv_low=csv.query('displ<=4')['hwy']
csv_high=csv.query('displ>=5')['hwy']
csv_high.mean()
csv_low.mean()

csv_audi_cty=csv.query('manufacturer=="audi"')['cty']
csv_toyota_cty=csv.query('manufacturer=="toyota"')['cty']
csv_audi_cty.mean()
csv_toyota_cty.mean()

csv_cfh=csv.query('manufacturer in ["chevrolet","ford","honda"]')['hwy']
csv_cfh.mean()

exam['math']
exam['english']
exam[['nclass','math','english']]

exam.drop(columns='math')
exam.drop(columns=['math','english'])
exam.query('nclass==1')['english']
exam.query('math>=50')[['id','math']]
exam.query('math>=50')[['id','math']].head()
exam.query('math>=50')[['id','math']].head(10)

mpg=pd.read_csv('data/mpg.csv')
mpg_new=mpg[['category','cty']]
mpg_new
mpg_new.query('category=="suv"')['cty'].mean()
mpg_new.query('category=="compact"')['cty'].mean()

exam.sort_values('math')
exam.sort_values('math',ascending=False)
exam.sort_values(['nclass','math'])
exam.sort_values(['nclass','math'],ascending=[True,False])

pd.read_csv('data/mpg.csv')
csv=pd.read_csv('data/mpg.csv')
csv_audi=csv.query("manufacturer=='audi'")
csv_audi.sort_values('hwy',ascending=False).head()

exam.assign(total=exam['math']+exam['english']+exam['science'])
exam.assign(
  total=exam['math']+exam['english']+exam['science'],
  mean=(exam['math']+exam['english']+exam['science'])/3)
  
import numpy as np
exam.assign(test=np.where(exam['science']>=60,'pass','fail'))  

exam.assign(total=exam['math']+exam['english']+exam['science'])\
 .sort_values('total')
 
long_name=pd.read_csv('data/exam.csv')
long_name.assign(new= lambda x: x['math']+x['english']+x['science'])

exam.assign(total=lambda x: x['math']+x['english']+x['science'],
            mean= lambda x: x['total']/3)
            
mpg_new=mpg.copy()
mpg_new=mpg_new.assign(total=mpg_new['cty']+mpg_new['hwy'])
mpg_new=mpg_new.assign(mean=(mpg_new['total'])/2)
mpg_new.sort_values('mean',ascending=False).head(3)

mpg.assign(total=mpg_new['cty']+mpg_new['hwy'],
           mean=lambda x: x['total']/2).sort_values('mean',ascending=False).head(3)

exam.agg(mean_math=('math','mean'))
mean_math

exam.groupby('nclass').agg(mean_math=('math','mean'))

exam.groupby('nclass').agg(
    mean_math=('math','mean'),
    sum_math=('math','sum'),
    median_math=('math','median'),
    n=('nclass','count'))
mpg.groupby(['manufacturer','drv']).agg(mean_cty=('cty','mean'))
mpg.query('manufacturer=="audi"').groupby(['drv']).agg(n=('drv','count'))
mpg.query('manufacturer=="chevrolet"').groupby(['drv']).agg(n=('drv','count'))
mpg['drv'].value_counts()

mpg.query('category=="suv"')\
    .assign(total=(mpg['hwy']+mpg['cty'])/2)\
    .groupby('manufacturer')\
    .agg(mean_tot=('total','mean'))\
    .sort_values('mean_tot',ascending=False)\
    .head()
    
test1=pd.DataFrame({
    'id':[1,2,3,4,5],
    'midterm':[60,80,70,90,85]})
test2=pd.DataFrame({
    'id':[1,2,3,4,5],
    'midterm':[70,83,65,95,80]})
test1
test2
total=pd.merge(test1,test2,how='left',on='id')
total
name=pd.DataFrame({
    'nclass':[1,2,3,4,5],
    'teacher':['kim','lee','park','choi','jung']
})
name
exam_new=pd.merge(exam,name,how='left',on='nclass')
exam_new

group_a=pd.DataFrame({
    'id':[1,2,3,4,5],
    'test':[60,80,70,90,85]})
group_b=pd.DataFrame({
    'id':[6,7,8,9,10],
    'test':[70,83,65,95,80]})
group_a
group_b
group_all=pd.concat([group_a,group_b])
group_all

fuel=pd.DataFrame({
    'fl':['c','d','e','p','r'],
    'price_fl':[2.35,2.38,2.11,2.76,2.22]
})
fuel
mpg
mpg_new=pd.merge(mpg,fuel,how='left',on='fl')
mpg_new.head()

mdw=pd.read_csv('data/midwest.csv')
mdw['popadults']
mdw['per_uage']=(1-mdw['popadults']/mdw['poptotal'])*100
mdw
mdw.sort_values('per_uage',ascending=False).head()
mdw.assign(amo_uage=\
    np.where(mdw['per_uage']>=40,'large',
    np.where(mdw['per_uage']>=30,'middle','small')))['amo_uage'].value_counts()


