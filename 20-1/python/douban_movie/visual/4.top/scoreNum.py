import pandas as pd
import numpy as np
import json

path = './data/movie_2010_2020.csv' # use your path
print("正在对", path, '分数分布')

pd.set_option('display.max_rows',100)
# pd.set_option('display.max_columns',100)

def getScore(file):
    df = pd.read_csv(file,error_bad_lines=False,sep=',')
    df = df[df.director.notnull()]
    df = df.drop_duplicates(subset=['title'], keep ='first')
    
    df_score = df.sort_values(by=['score'], ascending=False)
    df_score['title'] = df_score['title'].str[0:15]

    df_score_num = df.sort_values(by=['scoreNum'], ascending=False)
    df_score_num['title'] = df_score_num['title'].str[0:15]

    df_comment = df.sort_values(by=['smallCommentNum']+['longCommentNum'], ascending=False)
    df_comment['title'] = df_comment['title'].str[0:15]
    
    df_comment_sum = df_comment['smallCommentNum'] + df_comment['longCommentNum']

    print(df_comment_sum.tolist()[:20])

    print("\n============\n")
    print("评分top20的名字", df_score['title'].tolist()[:20])
    print("评分top20的名字的分数", df_score['score'].tolist()[:20])
    print("\n============\n")
    print("评分人数top20的名字", df_score_num['title'].tolist()[:20])
    print("评分人数top20的名字的数量", df_score_num['scoreNum'].tolist()[:20])
    print("评分人数top20的名字的分数", df_score_num['score'].tolist()[:20])
    print("\n============\n")
    print("评论人数top20的名字", df_comment['title'].tolist()[:20])
    print("评论人数top20的名字的数量", df_comment_sum.tolist()[:20])
    print("评论人数top20的名字的分数", df_comment['score'].tolist()[:20])

if __name__ == '__main__':
    getScore(path)