import pandas as pd

outputfile='./movie_detail_2017.csv'

print("正在对", outputfile, '去重')

def clearData(file):
    df = pd.read_csv(file,header=0,error_bad_lines=False,sep=',')
    df = df.drop_duplicates(subset=['title'], keep ='first')
    df['summary'] = df['summary'].str.replace(",", "，")
    df['summary'] = df['summary'].str.replace("/", "")
    df = df[df.score.notnull()]
    df.to_csv('./movie_detail_2017_score.csv')
    print('完成去重')

def clearData2(file):
    df = pd.read_csv(file,header=0,error_bad_lines=False,sep=',')
    df = df.drop_duplicates(subset=['title'], keep ='first')
    df['summary'] = df['summary'].str.replace(",", "，")
    df['summary'] = df['summary'].str.replace("/", "")
    df = df[df.title.notnull()]
    df.to_csv('./movie_detail_2017.csv')
    print('完成去重')
    
if __name__ == '__main__':
    clearData2(outputfile)
    # removeSplit(outputfile)
 