import pandas as pd
import jieba.analyse
from stylecloud import gen_stylecloud

# 读取文件
pd_data = pd.read_csv('methods2.txt')

# 读取内容
text = pd_data

# 切割分词
wordlist = jieba.lcut_for_search(''.join(text))
result = ' '.join(wordlist)

# 设置停用词
stop_words = ['什么', '然而', '可以', '巴黎', '全球', '使用', '协定', '加强', '提高', '通过', '方式 ', '我们', '方式', '利用', '应对', '生活']
ciyun_words = ''

for word in result:
    if word not in stop_words:
        ciyun_words += word

gen_stylecloud(text=result,
               size=2048,
               icon_name='fas fa-leaf',
               font_path='msyh.ttc',
               background_color='white',
               output_name='wordCloud.jpg',
               custom_stopwords=stop_words
               )

