import pandas as pd
import matplotlib as plt
import seaborn as sns 
import sweetviz as sv

train_fn = "../data/train.csv"
test_fn = "../data/test.csv"

def readData(fname):
    df = pd.read_csv(fname)

    return df

def analyseDF(df):
    print(df.describe())
    df.info(False)
    #heatmap correlation
    print(df.corr())
    #sns.pairplot(df)
    #sns.heatmap(df.corr(), annot=True)
    #plt.show()
     

df = readData(train_fn)
analyseDF(df)