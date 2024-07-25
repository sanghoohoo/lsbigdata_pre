import pandas as pd
import numpy as np

df=pd.read_csv('data/project_team1.csv')
before_name=[]
after_name=[]
lst_mean12_19=[]

df

for i in range(12, 23):
    before_name.append('20' + str(i))
    before_name.append('20' + str(i)+'.1')
    before_name.append('20' + str(i)+'.2')
    before_name.append('20' + str(i)+'.3')
    before_name.append('20' + str(i)+'.4')
    before_name.append('20' + str(i)+'.5')
    before_name.append('20' + str(i)+'.6')
    after_name.append((str(i)+'_1519'))
    after_name.append((str(i)+'_2024'))
    after_name.append((str(i)+'_2529'))
    after_name.append((str(i)+'_3034'))
    after_name.append((str(i)+'_3539'))
    after_name.append((str(i)+'_4044'))
    after_name.append(str(i) +"_4549")
    after_name.append
    
before_name
after_name    

br=df.copy()
br.drop(0, inplace=True) 
br.reset_index(drop=True, inplace=True)
br

for i in range(0, len(before_name)):
    br.rename(columns = {before_name[i] : after_name[i]}, inplace = True)
    
br.head()

br[after_name] = br[after_name].apply(pd.to_numeric)

type(br["12_1519"][6])

br=br.assign(
    mean20 = (br['20_2024']+br['20_2529']+br['20_3034'])/3,
    mean21 = (br['21_2024']+br['21_2529']+br['21_3034'])/3,
    mean22 = (br['22_2024']+br['22_2529']+br['22_3034'])/3)
    
br.head()

for i in range(0, 56, 7):
  lst_mean12_19.append\
  ((br[after_name[i + 1]] + br[after_name[i + 2]] + br[after_name[i + 3]]) / 3)

lst_mean12_19

br2 = br.iloc[[0]]
type(br2["21_2024"][0])
br2 = br2.iloc[:, 57:78] 
br2
br2 = br2.transpose()
br2
br2 = br2.rename(columns = {0 : 'birth_rate'})
br2 = br2.reset_index().rename(columns={'index': 'year'})
br2

br2['number'] = np.where(br2['year']\
        .isin(['20_2024', '20_2529', '20_3034', '21_2024', '21_2529',
                '21_3034', '22_2024', '22_2529', '22_3034']), 1, 2)
br2

br2_youth_rate = br2.query('number == 1')['birth_rate'].mean()
br2_non_youth_rate = br2.query('number == 2')['birth_rate'].mean()
br2_youth_rate
br2_non_youth_rate

br3= br.iloc[:, 1:21] ## 12-14년도 데이터 추출
br3 = br3.iloc[[0]]
br3 = br3.transpose()

br3 = br3.rename(columns = {0 : 'birth_rate'})
br3 = br3.reset_index().rename(columns={'index': 'year'})
br3['number'] = np.where(br3['year']\
                  .isin(['12_2024', '12_2529', '12_3034', '13_2024', '13_2529', '13_3034', '14_2024', '14_2529', '14_3034']), 1, 2)


br3_youth_rate = br3.query('number == 1')['birth_rate'].mean()
br3_non_youth_rate = br3.query('number == 2')['birth_rate'].mean()

print('청년: ', br3_youth_rate)
print('비청년: ', br3_non_youth_rate)

import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame({
    'Age Group': ['12_14Youth', '20_22Youth', '12_14Non-Youth', '20_22Non-Youth'],
    'Mean Birth Rate': [br3_youth_rate, br2_youth_rate, br3_non_youth_rate, br2_non_youth_rate],
    'Youth': ['Youth', 'Youth', 'Non-Youth', 'Non-Youth']
})

sns.barplot(x='Age Group', y='Mean Birth Rate', hue='Youth', data=data)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Mean Birth Rate', fontsize=12)
plt.title('12-14/20-22 Mean Birth Rate Comparison', fontsize=15)
plt.show()
plt.clf()

plt.rcParams.update({'font.family' : 'Malgun Gothic'})
new = br[['시군구별', 'mean20']].sort_values("mean20", ascending=False)
plt.figure(figsize=(7, 3))
sns.barplot(data=new, x='시군구별', y='mean20')
plt.xticks(rotation=45, fontsize=5)  
plt.xlabel('시군구별', fontsize=12)
plt.ylabel('Mean Birth Rate 2020', fontsize=12)
plt.title('Mean Birth Rate  2020년도 시군구별 ', fontsize=15)
plt.show()

new = br[['시군구별', 'mean21']].sort_values("mean21", ascending=False)
plt.figure(figsize=(7, 3))
sns.barplot(data=new, x='시군구별', y='mean21')
plt.xticks(rotation=45, fontsize=5)  
plt.xlabel('시군구별', fontsize=12)
plt.ylabel('Mean Birth Rate 2021', fontsize=12)
plt.title('Mean Birth Rate  2021년도 시군구별 ', fontsize=15)
plt.show()

new = br[['시군구별', 'mean22']].sort_values("mean22", ascending=False)
plt.figure(figsize=(7, 3))
sns.barplot(data=new, x='시군구별', y='mean22')
plt.xticks(rotation=45, fontsize=5)  
plt.xlabel('시군구별', fontsize=12)
plt.ylabel('Mean Birth Rate 2022', fontsize=12)
plt.title('Mean Birth Rate  2022년도 시군구별 ', fontsize=15)
plt.show()
