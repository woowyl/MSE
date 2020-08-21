import pandas as pd

outputfile='./movie_url_file_2014_2014.csv'

print("正在对", outputfile, '去重')

def quchong(file):
    df = pd.read_csv(file,header=0,sep=',')
    df['title'] = df['title'].str.replace(",", " ", case = False)
    datalist = df.drop_duplicates(subset=['id'], keep ='first')
    datalist.to_csv(file)
    print('完成去重')

if __name__ == '__main__':
    quchong(outputfile)
 