import pandas as pd
import numpy as np
import json

path = './data/movie_detail_2018.csv' # use your path
print("正在对", path, '分数分布')

pd.set_option('display.max_rows',10)
# pd.set_option('display.max_columns',100)

def getScore(file):
    df = pd.read_csv(file,error_bad_lines=False,sep=',')

    df_comedy = df[df['type'].apply(str).str.contains("喜剧") == True]
    df_fiction = df[df['type'].apply(str).str.contains("奇幻|科幻") == True]
    df_love = df[df['type'].apply(str).str.contains("爱情") == True]
    df_horror = df[df['type'].apply(str).str.contains("悬疑|惊悚|冒险|恐怖") == True]
    df_fight = df[df['type'].apply(str).str.contains("动作|战争") == True]
    df_cartoon = df[df['type'].apply(str).str.contains("动画") == True]

    print("============\n")
    ranges = [0,1,2,3,4,5,6,7,8,9,10]
    print(df.groupby(pd.cut(df.score,ranges)).count())
    print("所有数据分布:  ", df.groupby(pd.cut(df.score,ranges)).count()['index'].tolist())
    print("============\n")
    print("喜剧数据分布:  ", df_comedy.groupby(pd.cut(df_comedy.score,ranges)).count()['index'].tolist())
    print("============\n")
    print("科幻奇幻数据分布:  ", df_fiction.groupby(pd.cut(df_fiction.score,ranges)).count()['index'].tolist())
    print("============\n")
    print("爱情数据分布:  ", df_love.groupby(pd.cut(df_love.score,ranges)).count()['index'].tolist())
    print("============\n")
    print("悬疑惊悚数据分布:  ", df_horror.groupby(pd.cut(df_horror.score,ranges)).count()['index'].tolist())
    print("============\n")
    print("动作数据分布:  ", df_fight.groupby(pd.cut(df_fight.score,ranges)).count()['index'].tolist())
    print("============\n")
    print("动画数据分布:  ", df_cartoon.groupby(pd.cut(df_cartoon.score,ranges)).count()['index'].tolist())

if __name__ == '__main__':
    getScore(path)