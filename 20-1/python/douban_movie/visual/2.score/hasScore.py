import pandas as pd
import numpy as np

path = './data/movie_detail_2018.csv' # use your path
print("正在对", path, '去重')

pd.set_option('display.max_rows',10)
# pd.set_option('display.max_columns',100)

def getScore(file):
    df = pd.read_csv(file,error_bad_lines=False,sep=',')
    total = len(df)
    result = len(df.loc[df['score'] > 0])
    result2 = len(df.loc[df['score'].isna()])
    #print(result)
    print('总数是：',total, "   其中有评论的：", result, "没有评分的：", result2)
if __name__ == '__main__':
    getScore(path)