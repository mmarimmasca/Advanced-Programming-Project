##Dataset class project Advanced programming
import pandas as pd


class Dataset:
    def __init__(self, df: pd.core.frame.DataFrame):
        ''' df:pd.core.frame.DataFrame così l'oggetto Dataset è in realtà un DataFrame di Pandas e possiamo farci le Operations sopra '''
        self.data_frame = df

    def get_data_frame(self):
        ''' Questo metodo lo usiamo per ritornare l'attributo data_frame dato che è sempre meglio utilizzare un metodo invece di un attributo '''
        return self.data_frame


class Dataset_gff3(Dataset):
    def __init__(self, df: pd.core.frame.DataFrame):
        Dataset.__init__(self, df)

        ''' This part of code is supposed to 'clean' the Dataset, dropping the rows that start with ##,#! or ### '''
        df = df.drop(df[df['seqid'].str.contains('#')].index)  # rimosso tutte le righe che contengono #

        self.data_frame = df.reset_index(drop=True)  # resettato indici dallo zero
        self.data_frame = self.data_frame.replace('.', 'NaN')  # sostituito empty values with NaN

    def get_data_frame(self):
        return self.data_frame