##Dataset class project Advanced programming
import pandas as pd


class Dataset:
    def __init__(self, df: pd.core.frame.DataFrame):
        self.data_frame = df

    def get_data_frame(self):
        return self.data_frame


class Dataset_gff3(Dataset):
    def __init__(self, df: pd.core.frame.DataFrame):
        Dataset.__init__(self, df)
        
        df = df.drop(df[df['seqid'].str.contains('#')].index)
        self.data_frame = df.reset_index(drop=True)
        self.data_frame = self.data_frame.replace('.', 'NaN')

    def get_data_frame(self):
        return self.data_frame
