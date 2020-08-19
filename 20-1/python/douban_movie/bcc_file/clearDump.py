import pandas as pd

outputfile='./data/movie_url_file_2018.csv'

print("正在对", outputfile, '去重')

def quchong(file):
    df = pd.read_csv(file,header=0)
    df['title'] = df['title'].str.replace(",", " ", case = False)
    datalist = df.drop_duplicates(subset=['id'], keep ='first')
    datalist.to_csv(file)
    print('完成去重')

if __name__ == '__main__':
    quchong(outputfile)
 