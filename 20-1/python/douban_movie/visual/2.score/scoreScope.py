import pandas as pd
import numpy as np
import json

path = './data/movie_2010_2020.csv' # use your path
print("正在对", path, '分数分布')

pd.set_option('display.max_rows',10)
# pd.set_option('display.max_columns',100)

def getScore(file):
    df = pd.read_csv(file,error_bad_lines=False,sep=',')
    emptyDict = {
        "0.0": 0,
        "0.1": 0,
        "0.2": 0,
        "0.3": 0,
        "0.4": 0,
        "0.5": 0,
        "0.6": 0,
        "0.7": 0,
        "0.8": 0,
        "0.9": 0,
        "1.0": 0,
        "1.1": 0,
        "1.2": 0,
        "1.3": 0,
        "1.4": 0,
        "1.5": 0,
        "1.6": 0,
        "1.7": 0,
        "1.8": 0,
        "1.9": 0,
        "2.0": 0,
        "2.1": 0,
        "2.2": 0,
        "2.3": 0,
        "2.4": 0,
        "2.5": 0,
        "2.6": 0,
        "2.7": 0,
        "2.8": 0,
        "2.9": 0,
        "3.0": 0,
        "3.1": 0,
        "3.2": 0,
        "3.3": 0,
        "3.4": 0,
        "3.5": 0,
        "3.6": 0,
        "3.7": 0,
        "3.8": 0,
        "3.9": 0,
        "4.0": 0,
        "4.1": 0,
        "4.2": 0,
        "4.3": 0,
        "4.4": 0,
        "4.5": 0,
        "4.6": 0,
        "4.7": 0,
        "4.8": 0,
        "4.9": 0,
        "5.0": 0,
        "5.1": 0,
        "5.2": 0,
        "5.3": 0,
        "5.4": 0,
        "5.5": 0,
        "5.6": 0,
        "5.7": 0,
        "5.8": 0,
        "5.9": 0,
        "6.0": 0,
        "6.1": 0,
        "6.2": 0,
        "6.3": 0,
        "6.4": 0,
        "6.5": 0,
        "6.6": 0,
        "6.7": 0,
        "6.8": 0,
        "6.9": 0,
        "7.0": 0,
        "7.1": 0,
        "7.2": 0,
        "7.3": 0,
        "7.4": 0,
        "7.5": 0,
        "7.6": 0,
        "7.7": 0,
        "7.8": 0,
        "7.9": 0,
        "8.0": 0,
        "8.1": 0,
        "8.2": 0,
        "8.3": 0,
        "8.4": 0,
        "8.5": 0,
        "8.6": 0,
        "8.7": 0,
        "8.8": 0,
        "8.9": 0,
        "9.0": 0,
        "9.1": 0,
        "9.2": 0,
        "9.3": 0,
        "9.4": 0,
        "9.5": 0,
        "9.6": 0,
        "9.7": 0,
        "9.8": 0,
        "9.9": 0,
        # "10.0": 0
    }   
    df_cn = df[df['country'].apply(str).str.contains("中国") == True]
    df_foreign = df[df['country'].apply(str).str.contains("中国") == False]

    scoreDict_cn = json.loads(df_cn.loc[:,'score'].value_counts().to_json())
    scoreDict_foreign = json.loads(df_foreign.loc[:,'score'].value_counts().to_json())

    result_cn = {**emptyDict, **scoreDict_cn}
    result_foreign = {**emptyDict, **scoreDict_foreign}

    sortedResult_cn = sorted(result_cn.items(), key=lambda x:x[0])
    sortedResult_foreign = sorted(result_foreign.items(), key=lambda x:x[0])
    print(sortedResult_cn)
    print("============\n")
    print("国内评分：",[num for( _, num) in sortedResult_cn])
    print("============\n")
    print("国外评分：",[num for( _, num) in sortedResult_foreign])

if __name__ == '__main__':
    getScore(path)