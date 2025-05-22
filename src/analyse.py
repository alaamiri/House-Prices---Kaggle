import pandas as pd
import matplotlib as plt

train_fn = "../data/train.csv"
test_fn = "../data/test.csv"

def readData(fname):
    df = pd.read_csv(fname)

    return df

def analyseDF(df):
    print(df.describe())
    df.info(False)
    #df.isnull.sum()
    #df.value_counts()


df = readData(train_fn)
analyseDF(df)