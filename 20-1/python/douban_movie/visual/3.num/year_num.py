import pandas as pd
import numpy as np
import json

path = './data/movie_2010_2020.csv' # use your path
print("正在对", path, '分数分布')

pd.set_option('display.max_rows',10)
# pd.set_option('display.max_columns',100)

def getScore(file):
    df = pd.read_csv(file,error_bad_lines=False,sep=',')
    df_year = df[df['year'].apply(str).str.contains("2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020")==True]
    print(len(df[df['year'].apply(str).str.contains("2016")==True]))
    emptyDict = {
        "2010.0": 0,
        "2011.0": 0,
        "2012.0": 0,
        "2013.0": 0,
        "2014.0": 0,
        "2015.0": 0,
        "2016.0": 0,
        "2017.0": 0,
        "2018.0": 0,
        "2019.0": 0,
        "2020.0": 0
    } 

    df_year_cn = df_year[df_year['country'].apply(str).str.contains("中国大陆")==True]
    df_year_gat = df_year[df_year['country'].apply(str).str.contains("台湾|香港|澳门")==True]
    df_year_ind = df_year[df_year['country'].apply(str).str.contains("印度")==True]
    df_year_usa = df_year[df_year['country'].apply(str).str.contains("美国")==True]
    df_year_kor = df_year[df_year['country'].apply(str).str.contains("韩国")==True]
    df_year_jpa = df_year[df_year['country'].apply(str).str.contains("日本")==True]


    yearDict = {**emptyDict, **json.loads(df_year.loc[:,'year'].value_counts().to_json())}

    yearDict_cn = {**emptyDict, **json.loads(df_year_cn.loc[:,'year'].value_counts().to_json())}
    yearDict_gat = {**emptyDict, **json.loads(df_year_gat.loc[:,'year'].value_counts().to_json())}
    yearDict_ind = {**emptyDict, **json.loads(df_year_ind.loc[:,'year'].value_counts().to_json())}
    yearDict_usa = {**emptyDict, **json.loads(df_year_usa.loc[:,'year'].value_counts().to_json())}
    yearDict_kor = {**emptyDict, **json.loads(df_year_kor.loc[:,'year'].value_counts().to_json())}
    yearDict_jpa = {**emptyDict, **json.loads(df_year_jpa.loc[:,'year'].value_counts().to_json())}


    sortedDict = sorted(yearDict.items(), key=lambda x:x[0])
    # print(sortedDict)

    sortedDict_cn = sorted(yearDict_cn.items(), key=lambda x:x[0])
    sortedDict_gat = sorted(yearDict_gat.items(), key=lambda x:x[0])
    sortedDict_ind = sorted(yearDict_ind.items(), key=lambda x:x[0])
    sortedDict_usa = sorted(yearDict_usa.items(), key=lambda x:x[0])
    sortedDict_kor = sorted(yearDict_kor.items(), key=lambda x:x[0])
    sortedDict_jpa = sorted(yearDict_jpa.items(), key=lambda x:x[0])

    print("============\n")
    print("所有国家年份变化: ",[num for( _, num) in sortedDict])
    print("============\n")
    print("中国年份变化: ",[num for( _, num) in sortedDict_cn])
    print("============\n")
    print("港澳台年份变化: ",[num for( _, num) in sortedDict_gat])
    print("============\n")
    print("印度年份变化: ",[num for( _, num) in sortedDict_ind])
    print("============\n")
    print("美国年份变化: ",[num for( _, num) in sortedDict_usa])
    print("============\n")
    print("韩国年份变化: ",[num for( _, num) in sortedDict_kor])
    print("============\n")
    print("日本年份变化: ",[num for( _, num) in sortedDict_jpa])

if __name__ == '__main__':
    getScore(path)