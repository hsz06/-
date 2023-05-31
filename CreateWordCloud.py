import pandas as pd
import jieba.analyse
import wordcloud
import pandas as pd
import csv
import jieba
import matplotlib.pyplot as plt
from stylecloud import gen_stylecloud

# 读取文件
with open("methods2.txt",'r',encoding='utf') as f:
    pd_data = f.read()

# 读取内容
text = pd_data
# 添加停用词
stopwords_filefath = 'stopword_normal.txt'
sw = [line.strip() for line in open(stopwords_filefath, 'r',encoding='utf-8').readlines()]
sw_u=[x for x in sw]

#collocations=False:解决词云关键字重复多次的问题
wc = wordcloud.WordCloud(background_color='white', font_path='simhei.ttf',stopwords=sw_u,collocations=False,
                         max_words=300, margin=0,min_font_size=2,max_font_size=100,random_state = 42,scale=2,
                         width=1400, height=1000)
wc.generate_from_text(pd_data )
plt.rcParams['figure.figsize'] = (12.6, 9.0) # 设置figure_size尺寸
plt.rcParams['figure.dpi'] = 250
plt.imshow(wc)
plt.axis('off')
plt.savefig('措施.jpg')
plt.show()

