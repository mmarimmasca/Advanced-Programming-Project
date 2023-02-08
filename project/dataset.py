# Advanced Programming Project
# DataSet and DataSetGff3 classes

import pandas as pd

class DataSet:
    def __init__(self, df: pd.core.frame.DataFrame):
        ''' The method constructor defines the initialization of a DataSet object.
            It takes as input a parameter, 'df', which should be of type 'pd.core.fram.DataFrame',therefore a Pandas DataFrame '''
        self.dataFrame = df

    def getDataFrame(self):
        ''' This method returns the self.dataFrame attribute '''
        return self.dataFrame


class DataSetGff3(DataSet):
    def __init__(self, df: pd.core.frame.DataFrame):
        DataSet.__init__(self, df) # call the constructor of the superclass DataSet

        ''' This section of code cleans the Dataset, making it more suitable for the operations to be carried out '''
        df = df.drop(df[df['seqid'].str.contains('#')].index)  # dropping rows that contain in the 'seqid' column the character '#', common to all metadata
        self.dataFrame = df.reset_index(drop=True)             # reset indexes from 0
        self.dataFrame = self.dataFrame.replace('.', 'NaN')    # replace empty values ('.') with NaN values

    def getDataFrame(self):
        ''' This method returns the self.dataFrame attribute '''
        return self.dataFrame
