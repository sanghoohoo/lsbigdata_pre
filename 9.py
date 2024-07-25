import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


raw_welfare=pd.read_spss('data/Koweps_hpwc14_2019_beta2.sav')
welfare=raw_welfare.copy()
welfare
welfare.shape
welfare.info()
welfare.describe()
welfare=welfare.rename(
    columns={
        'h14_g3':'sex',
        'h14_g4':'birth',
        'h14_g10':'marriage_type',
        'h14_g11':'religion',
        'p1402_8aq1':'income',
        'h14_eco9':'code_job',
        'h14_reg7':'code_region',
})

welfare['sex'].dtypes
welfare['sex'].value_counts()
welfare['sex']=np.where(welfare['sex']==1,'male','female')
welfare['sex'].value_counts()
sns.countplot(data=welfare,x='sex',hue='sex')
plt.show()
plt.clf()

welfare['income'].dtypes
welfare['income'].describe()
sns.histplot(data=welfare, x='income')
plt.show()
plt.clf()
welfare['income'].isna().sum()

sex_income=welfare.dropna(subset='income')\
    .groupby('sex',as_index=False).agg(mean_income=('income','mean'))
sex_income

sns.barplot(data=sex_income, x='sex', y='mean_income', hue='sex')
plt.show()
plt.clf()

#9-3
welfare['birth'].dtypes
welfare['birth'].describe()
welfare['birth'].isna().sum()
welfare=welfare.assign(age=2019-welfare['birth']+1)
welfare['age'].describe()
sns.histplot(data=welfare,x='age')
plt.show()
plt.clf()

age_income=welfare.dropna(subset='income')\
    .groupby('age').agg(mean_income=('income','mean'))
age_income.head(15)

sns.lineplot(data=age_income, x='age', y='mean_income')
plt.show()
plt.clf()

welfare['age'].head()
welfare=welfare.assign(ageg=np.where(welfare['age']<30,'young',
                            np.where(welfare['age']<=59,'middle','old')))
welfare['ageg'].value_counts()
sns.countplot(data=welfare,x='ageg',hue='ageg')
plt.show()
plt.clf()

ageg_income=welfare.dropna(subset='income')\
    .groupby('ageg',as_index=False).agg(mean_income=('income','mean'))
ageg_income
sns.barplot(data=ageg_income,x='ageg',y='mean_income',hue='ageg',
    order=['young','middle','old'])
plt.show()
plt.clf()

sex_income=welfare.dropna(subset='income')\
                  .groupby(['ageg','sex'], as_index=False)\
                  .agg(mean_income=('income','mean'))
sex_income

sns.barplot(data=sex_income, x='ageg', y='mean_income',
hue='sex', order=['young','middle','old'])

plt.show()
plt.clf()

sex_age=welfare.dropna(subset='income')\
               .groupby(['age','sex'], as_index=False)\
               .agg(mean_income=('income','mean'))
sex_age.head()

sns.lineplot(data=sex_age, x='age', y='mean_income', hue='sex')
plt.show()
plt.clf()

welfare['code_job'].dtypes
welfare['code_job'].value_counts()

list_job=pd.read_excel('data/Koweps_Codebook_2019.xlsx', sheet_name='직종코드')
list_job.head()

list_job.shape

welfare=welfare.merge(list_job, how='left', on='code_job')
welfare.dropna(subset='code_job')[['code_job','job']].head()

job_income=welfare.dropna(subset=['job','income'])\
                  .groupby('job', as_index=False)\
                  .agg(mean_income=('income','mean'))
job_income.head()

top10=job_income.sort_values('mean_income',ascending=False).head(10)
top10

plt.rcParams.update({'font.family':'Malgun Gothic'})
sns.barplot(data=top10, y='job', x='mean_income', hue='job')
plt.show()
plt.clf()

bottom10=job_income.sort_values('mean_income').head(10)
bottom10

sns.barplot(data=bottom10, y='job', x='mean_income', hue='job')\
    .set(xlim=[0,800])
plt.show()
plt.clf()

job_male=welfare.dropna(subset='job')\
                .query('sex=="male"')\
                .groupby('job',as_index=False)\
                .agg(n=('job','count'))\
                .sort_values('n',ascending=False)\
                .head(10)
job_male

job_female=welfare.dropna(subset='job')\
                  .query('sex=="female"')\
                  .groupby('job',as_index=False)\
                  .agg(n=('job','count'))\
                  .sort_values('n',ascending=False)\
                  .head(10)
job_female

sns.barplot(data=job_male, y='job', x='n', hue='job').set(xlim=[0,500])
plt.show()
plt.clf()

sns.barplot(data=job_female, y='job', x='n', hue='job').set(xlim=[0,500])
plt.show()
plt.clf()

welfare['religion'].dtypes
welfare['religion'].value_counts()
welfare['religion']=np.where(welfare['religion']==1,'yes','no')
welfare['religion'].value_counts()
sns.countplot(data=welfare, x='religion', hue='religion')
plt.show()
plt.clf()

welfare['marriage_type'].dtypes
welfare['marriage_type'].value_counts()
welfare['marriage']=np.where(welfare['marriage_type']==1,'marriage',
                    np.where(welfare['marriage_type']==3,'divorce','etc'))
                    
n_divorce=welfare.groupby('marriage', as_index=False)\
                 .agg(n=('marriage','count'))
n_divorce

sns.barplot(data=n_divorce, x='marriage', y='n', hue='marriage')
plt.show()
plt.clf()

rel_div=welfare.query('marriage !="etc"')\
               .groupby('religion',as_index=False)['marriage']\
               .value_counts(normalize=True)
rel_div

rel_div=rel_div.query('marriage=="divorce"')\
               .assign(proportion=rel_div['proportion']*100)\
               .round(1)
rel_div

sns.barplot(data=rel_div, x='religion', y='proportion', hue='religion')
plt.show()
plt.clf()

age_div=welfare.query('marriage != "etc"')\
               .groupby('ageg', as_index=False)['marriage']\
               .value_counts(normalize=True)
age_div

welfare.query('marriage !="etc"')\
       .groupby('ageg', as_index=False)['marriage']\
       .value_counts()
       
age_div= age_div.query('ageg != "young" & marriage=="divorce"')\
                .assign(proportion = age_div['proportion']*100)\
                .round(1)
age_div

sns.barplot(data=age_div, x='ageg', y='proportion', hue='ageg')
plt.show()
plt.clf()

age_rel_div=welfare.query('marriage != "etc" & ageg != "young"')\
                   .groupby(['ageg', 'religion'], as_index=False)['marriage']\
                   .value_counts(normalize=True)
age_rel_div                   

age_rel_div= age_rel_div.query('marriage == "divorce"')\
                        .assign(proportion=age_rel_div['proportion']*100)\
                        .round(1)
age_rel_div

sns.barplot(data=age_rel_div, x='ageg', y='proportion', hue= 'religion')
plt.show()
plt.clf()

welfare['code_region'].dtypes
welfare['code_region'].value_counts()

list_region= pd.DataFrame({'code_region' : [1,2,3,4,5,6,7],
                           'region' : ['서울','수도권(인천/경기)',
                                         '부산/경남/울산','대구/경북',
                                         '대전/충남','강원/충북',
                                         '광주/전남/전북/제주도']})
list_region

welfare = welfare.merge(list_region, how = 'left', on = 'code_region')
welfare[['code_region','region']].head()

region_ageg= welfare.groupby('region', as_index=False)['ageg']\
                    .value_counts(normalize = True)
region_ageg

region_ageg=region_ageg.assign(proportion=region_ageg['proportion']*100).round(1)
region_ageg

sns.barplot(data=region_ageg, y='region', x='proportion', hue='ageg')
plt.show()
plt.clf()

pivot_df=region_ageg[['region','ageg','proportion']].pivot(index='region',
                                                           columns='ageg',
                                                           values='proportion')
pivot_df

pivot_df.plot.barh(stacked=True)
plt.show()
plt.clf()

reorder_df=pivot_df.sort_values('old')[['young','middle','old']]
reorder_df

reorder_df.plot.barh(stacked=True)
plt.show()
plt.clf()
