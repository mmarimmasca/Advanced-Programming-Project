# Advanced Programming project
# Decorator @isactive, Operation class

import pandas as pd
from dataset import DataSet, DataSetGff3

''' The 'global_l' variable lists the active operations among the registry of operations.
    Therefore, 'global_l' is the list of names of methods currently active. '''
global_l = ['columnInfo', 'listSeqIds', 'listTypes', 'countFeaturesInSource', 'countEntriesForType', 'infoEntireChroms', 'fractionUnassembled', 'newHavana', 'countEntriesNewHavana', 'geneName']


# Function splitting rows used in the method 'geneName'
def split_rows(row):
    return str(row).split(';')[1].split('=')[1]

# Decorator @isactive
''' The '@isactive' decorator allows the execution only of the methods marked as active.
    In practice, it checks whether the name of the method to which is applied is present in the list of active operations (global_l) or not.
    In the case it's present, it executes the method on the dataset, otherwise it returns an error message. '''
def isactive(f):
    def wrapper(*args):
        if f.__name__ in global_l: 
            return f(*args)       
        else:                     
            return ('Function not in the registry of active operations') 
    return wrapper


# Operation class
class Operation:
    ''' The Operation class contains the methods required for implementing the insights over the dataset.
        Each of the methods is decorated both with the @staticmethod decorator and with the @isactive decorator.
        Each of the methods takes as input one parameter ('df'), which must be of the DataSet type, and returns another DataSet object, containing the results of the insight.
        The first line of code of each method re-sets the value of 'df' through the DataSet.getDataFrame() method to retrieve the Pandas DataFrame to perform the operations. '''
    # 1
    @staticmethod
    @isactive
    def columnInfo(df : DataSet):
        ''' This method returns a two-column dataset where the names of the columns and the respective type are listed. '''
        df = df.getDataFrame()
        return DataSet(pd.DataFrame(data={'names of columns': df.columns, 'types': [df[column].dtype for column in df.columns ]}).reset_index(drop=True))

    # 2
    @staticmethod
    @isactive
    def listSeqIds(df : DataSet):
        ''' This method returns a single-column dataset where the single features present in the 'seqid' column are listed. '''
        df = df.getDataFrame()
        return DataSet(pd.DataFrame({'seqIDs': df['seqid'].unique()}))

    # 3
    @staticmethod
    @isactive
    def listTypes(df : DataSet):
        ''' This method returns a single-column dataset where the single features present in the 'type' column are listed. '''
        df = df.getDataFrame()
        return DataSet(pd.DataFrame({'types': df['type'].unique()}))

    # 4
    @staticmethod
    @isactive
    def countFeaturesInSource(df : DataSet):
        ''' This method returns a two-column dataset where the single features of the 'source' column and the respective count of entries are listed. '''
        df = df.getDataFrame()
        group_source = df.groupby('source')
        return DataSet(pd.DataFrame({'source': group_source.groups.keys(), 'source count': group_source.size().array}))

    # 5
    @staticmethod
    @isactive
    def countEntriesForType(df : DataSet):
        ''' This method returns a two-column dataset where the single features of the 'type' column and the respective count of entries are listed. '''
        df = df.getDataFrame() 
        group_type = df.groupby('type')
        return DataSet(pd.DataFrame({'types': group_type.groups.keys(), 'types count': group_type.size().array}))

    # 6
    @staticmethod
    @isactive
    def infoEntireChroms(df : DataSet):
        ''' This method returns a selection of the original dataset where only the entries in which the value of the 'source' column equal to 'GRCh38' are displayed. '''
        df = df.getDataFrame() 
        return DataSet(df.loc[lambda df: df['source'] == 'GRCh38'].reset_index(drop=True))

    # 7
    @staticmethod
    @isactive
    def fractionUnassembled(df : DataSet):
        ''' This method returns a single-column and single-row dataset with the ratio between the entries where the value 
        in the column 'type' is 'superconting' and the total entries of the 'infoEntireChroms' '''
        count_df = Operation.infoEntireChroms(df).getDataFrame()
        fract_df = count_df.loc[lambda df: df['type'] == 'supercontig']
        return DataSet(pd.DataFrame({'unassembled/entire chromosomes': [f"{fract_df.shape[0]}/{count_df.shape[0]}"]}))

    # 8
    @staticmethod
    @isactive
    def newHavana(df : DataSet):
        ''' This method returns a selection of the original dataset where only the entries in which the values
        of the 'source' column are either 'ensembl', 'havana' or 'ensembl_havana' are displayed. '''
        df = df.getDataFrame()
        new_df = pd.DataFrame(df[df['source'].isin(['ensembl', 'havana', 'ensembl_havana'])])
        return DataSet(new_df.reset_index(drop=True))

    # 9
    @staticmethod
    @isactive
    def countEntriesNewHavana(df : DataSet):
        ''' This method returns a two-column dataset where data are retrieved by the dataset resulting from the 'newHavana' method.
            The dataset lists the single features of the 'type' column and the respective number of entries for each feature. '''
        df_havana = Operation.newHavana(df).getDataFrame()
        group_type = df_havana.groupby('type')
        return DataSet(pd.DataFrame({'type': group_type.groups.keys(), 'count': group_type.size().array}))

    # 10
    @staticmethod
    @isactive
    def geneName(df : DataSet):
        ''' This method returns a single-column dataset where data are retrieved by the dataset resulting from the 'newHavana' method.
            The dataset lists the different gene names present in the 'attributes' column '''
        df_havana = Operation.newHavana(df).getDataFrame()
        genes = df_havana[df_havana['type'] == 'gene']['attributes']
        names = pd.DataFrame({'genes': genes.apply(split_rows)})
        return DataSet(names.reset_index(drop=True))
