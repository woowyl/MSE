import pandas as pd

outputfile='./data/movie_url_file_2019.csv'

print("正在对", outputfile, '去重')

def quchong(file):
    df = pd.read_csv(file,header=0)
    datalist = df.drop_duplicates(subset=['id'], keep ='first')
    datalist.to_csv(file)
    print('完成去重')
def removeSplit(file) :
    df = pd.read_csv(file,header=0)
    df['url'] = df['url'].map(lambda x: x.replace(",", ' '))
    print('完成去重')

if __name__ == '__main__':
    quchong(outputfile)
    removeSplit(outputfile)
 