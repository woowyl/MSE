import pandas as pd

YEAR = 2014

outputfile='../data/movie_detail_{year}.csv'.format(year=str(YEAR))

print("正在对", outputfile, '去重')

def clearData(file):
    df = pd.read_csv(file,header=0,error_bad_lines=False,sep=',')
    df = df.drop_duplicates(subset=['title'], keep ='first')
    df['summary'] = df['summary'].str.replace(",", "，")
    df['summary'] = df['summary'].str.replace("/", "")
    df = df[df.score.notnull()]
    df.to_csv('./movie_detail_{year}_score.csv'.format(year=str(YEAR)))
    print('完成非空清理')

def clearData2(file):
    df = pd.read_csv(file,header=0,error_bad_lines=False,sep=',')
    df = df.drop_duplicates(subset=['title'], keep ='first')
    df['summary'] = df['summary'].str.replace(",", "，")
    df['summary'] = df['summary'].str.replace("/", "")
    df = df[df.title.notnull()]
    df.to_csv('./movie_detail_{year}.csv'.format(year=str(YEAR)))
    print('完成打分清理')
    
if __name__ == '__main__':
    clearData(outputfile)
    clearData2(outputfile)
    # removeSplit(outputfile)
 