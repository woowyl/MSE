# coding: utf-8
import pandas as pd

outputfile='./data/movie_url_file_2016_2016.csv'

print("正在对", outputfile, '去重')

def urlquchong(file):
    df = pd.read_csv(file,header=0,sep=',')
    datalist = df.drop_duplicates(subset=['id'], keep ='first')
    df['title'] = df['title'].str.replace(",", " ", case = False)
    datalist.to_csv(file)
    print('完成去重')


if __name__ == '__main__':
    #quchong(outputfile)
    urlquchong(outputfile)
 