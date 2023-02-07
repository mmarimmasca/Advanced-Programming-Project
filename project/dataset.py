##Dataset class project Advanced programming
import pandas as pd


class DataSet:
    def __init__(self, df: pd.core.frame.DataFrame):
        ''' df:pd.core.frame.DataFrame così l'oggetto Dataset è in realtà un DataFrame di Pandas e possiamo farci le Operations sopra '''
        self.dataFrame = df

    def getDataFrame(self):
        ''' Questo metodo lo usiamo per ritornare l'attributo data_frame dato che è sempre meglio utilizzare un metodo invece di un attributo '''
        return self.dataFrame


class DataSetGff3(DataSet):
    def __init__(self, df: pd.core.frame.DataFrame):
        DataSet.__init__(self, df)

        ''' This part of code is supposed to 'clean' the Dataset, dropping the rows that start with ##,#! or ### '''
        df = df.drop(df[df['seqid'].str.contains('#')].index)  # rimosso tutte le righe che contengono #

        self.dataFrame = df.reset_index(drop=True)  # resettato indici dallo zero
        self.dataFrame = self.dataFrame.replace('.', 'NaN')  # sostituito empty values with NaN

    def getDataFrame(self):
        return self.dataFrame