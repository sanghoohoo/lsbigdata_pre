import pandas as pd
df=pd.read_csv('data/news_comment_BTS.csv', encoding = 'UTF-8')
df
df.info()

df['reply']=df['reply'].str.replace('[^가-힣]',' ',regex=True)
df['reply']

import konlpy
kkma = konlpy.tag.Kkma()

nouns = df['reply'].apply(kkma.nouns)
nouns

nouns = nouns.explode()

df_word = pd.DataFrame({'word' : nouns})

df_word['count']=df_word['word'].str.len()

df_word=df_word.query('count >= 2')
df_word

df_word = df_word.groupby('word', as_index=False)\
                 .agg(n = ('word', 'count'))\
                 .sort_values('n', ascending=False)
df_word

top20 = df_word.head(20)
top20

plt.rcParams.update({'figure.figsize' : [6.5, 6]})
sns.barplot(data=top20, y='word', x='n', hue='word')
plt.yticks(fontsize=7)
plt.show()
plt.clf()

dic_word = df_word.set_index('word').to_dict()['n']

wc = WordCloud(random_state = 1234,
               font_path = font,
               width = 400,
               height = 400,
               background_color = 'white',
               mask = img)
               
img_wordcloud = wc.generate_from_frequencies(dic_word)

plt.figure(figsize = (10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()
plt.clf()
