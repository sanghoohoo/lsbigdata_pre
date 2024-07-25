moon = open('data/speech_moon.txt', encoding = 'UTF-8').read()
moon

import re
moon=re.sub('[^가-힣]',' ', moon)
moon

import konlpy
hannanum = konlpy.tag.Hannanum()

hannanum.nouns('대한민국의 영토는 한반도와 그 부속도서로 한다')

nouns=hannanum.nouns(moon)
nouns

import pandas as pd
df_word = pd.DataFrame({'word' : nouns})
df_word
df_word['count']=df_word['word'].str.len()
df_word
df_word=df_word.query('count>=2')
df_word.sort_values('count')
df_word=df_word.groupby('word',as_index=False)\
               .agg(n=('word','count'))\
               .sort_values('n',ascending=False)
df_word

top20 = df_word.head(20)
top20

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family' : 'Malgun Gothic',
                     'figure.dpi' : '120',
                     'figure.figsize' : [6.5, 6]})
                     
sns.barplot(data=top20, y='word', x='n')
plt.show()
plt.clf()

font='DoHyeon-Regular.ttf'
dic_word = df_word.set_index('word').to_dict()['n']
dic_word

from wordcloud import WordCloud
wc = WordCloud(random_state = 1234,
               font_path = font,
               width = 400,
               height = 400,
               background_color = 'white')
               
img_wordcloud = wc.generate_from_frequencies(dic_word)

plt.figure(figsize = (10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()
plt.clf()

import PIL
icon = PIL.Image.open('data/cloud.png')
import numpy as np
img = PIL.Image.new('RGB', icon.size, (255, 255, 255))
img.paste(icon, icon)
img= np.array(img)
wc = WordCloud(random_state = 1234,
               font_path = font,
               width = 400,
               height = 400,
               background_color = 'white',
               mask = img,
               colormap = 'inferno')
               
img_wordcloud = wc.generate_from_frequencies(dic_word)

plt.figure(figsize = (10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()
plt.clf()
