import pandas as pd

df=pd.read_csv("athlete_events.csv")
region_df=pd.read_csv("noc_regions.csv")

def preprocess(df,region_df):

    #Filtering for summer olympics
    df=df[df["Season"]=="Summer"]
    #Merge with region_df
    df=df.merge(region_df[["NOC","region"]],on="NOC",how="left")
    #Dropping Duplicates
    df.drop_duplicates(inplace=True)
    #One hot encoding medals
    df=pd.concat([df,pd.get_dummies(df["Medal"])],axis=1)
    return df
