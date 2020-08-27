import pandas as pd
import numpy as np
import json

path = './data/movie_detail_2018.csv' # use your path
print("正在对", path, '分数分布')

pd.set_option('display.max_rows',10)
# pd.set_option('display.max_columns',100)

def getScore(file):
    df = pd.read_csv(file,error_bad_lines=False,sep=',')

    # df_comedy = df[df['type'].apply(str).str.contains("喜剧") == True]
    print("============\n")
    ranges = ['中国大陆', '港澳台', '美国', '印度', '韩国', '日本', '意大利', '法国', '英国', '德国']
    print("不同国家间数量对比为: ", [len(df[df['country'].apply(str).str.contains("中国大陆")]),
    len(df[df['country'].apply(str).str.contains("台湾|香港|澳门")]),
    len(df[df['country'].apply(str).str.contains("美国")]),
    len(df[df['country'].apply(str).str.contains("印度")]),
    len(df[df['country'].apply(str).str.contains("韩国")]),
    len(df[df['country'].apply(str).str.contains("日本")]),
    len(df[df['country'].apply(str).str.contains("意大利")]),
    len(df[df['country'].apply(str).str.contains("法国")]),
    len(df[df['country'].apply(str).str.contains("英国")]),
    len(df[df['country'].apply(str).str.contains("德国")])])
    # print(len(df[df['country'].apply(str).str.contains("中国大陆")]))

if __name__ == '__main__':
    getScore(path)