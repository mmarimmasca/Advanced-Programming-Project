##decorator and operations project Advanced programming

import pandas as pd
from dataset import DataSet, DataSetGff3

# DECORATOR
# import inspect

global_l = ['columnInfo', 'listSeqIds', 'listTypes', 'countFeaturesInSource', 'countEntriesForType',
            'infoEntireChroms', 'fractionUnassembled', 'newHavana', 'countEntriesNewHavana', 'geneName']


def split_rows(row):
    return str(row).split(';')[1].split('=')[1]
    
    
def isactive(f):
    def wrapper(*args):
        if f.__name__ in global_l:
            return f(*args)
        else:
            return ('Function not in the registry of active operations')

    return wrapper


class Operation:
    # 1
    @staticmethod
    @isactive
    def columnInfo(df : DataSet):
        return DataSet(pd.DataFrame(data={'names of columns': df.columns, 'types': [df[column].dtype for column in df.columns ]}).reset_index(drop=True))

    # 2
    @staticmethod
    @isactive
    def listSeqIds(df : DataSet):
        df = df.getDataFrame()
        return DataSet(pd.DataFrame({'seqIDs': df['seqid'].unique()}))

    # 3
    @staticmethod
    @isactive
    def listTypes(df : DataSet):
        df = df.getDataFrame()
        return DataSet(pd.DataFrame({'types': df['type'].unique()}))

    # 4
    @staticmethod
    @isactive
    def countFeaturesInSource(df : DataSet):
        df = df.getDataFrame()
        group_source = df.groupby('source')
        return DataSet(pd.DataFrame({'source': group_source.groups.keys(), 'source count': group_source.size().array}))

    # 5
    @staticmethod
    @isactive
    def countEntriesForType(df : DataSet):
        df = df.getDataFrame() 
        group_type = df.groupby('type')
        return DataSet(pd.DataFrame({'types': group_type.groups.keys(), 'types count': group_type.size().array}))

    # 6
    @staticmethod
    @isactive
    def infoEntireChroms(df : DataSet):
        df = df.getDataFrame() 
        return DataSet(df.loc[lambda df: df['source'] == 'GRCh38'].reset_index(drop=True))

    # 7
    @staticmethod
    @isactive
    def fractionUnassembled(df : DataSet):
        count_df = Operation.infoEntireChroms(df).getDataFrame()
        fract_df = count_df.loc[lambda df: df['type'] == 'supercontig']
        return DataSet(pd.DataFrame({'unassembled/entire chromosomes': [f"{fract_df.shape[0]}/{count_df.shape[0]}"]}))

    # 8
    @staticmethod
    @isactive
    def newHavana(df : DataSet):
        df = df.getDataFrame()
        new_df = pd.DataFrame(df[df['source'].isin(['ensembl', 'havana', 'ensembl_havana'])])
        return DataSet(new_df.reset_index(drop=True))

    # 9
    @staticmethod
    @isactive
    def countEntriesNewHavana(df : DataSet):
        df_havana = Operation.newHavana(df).getDataFrame()
        group_type = df_havana.groupby('type')
        return DataSet(pd.DataFrame({'type': group_type.groups.keys(), 'count': group_type.size().array}))

    # 10
    @staticmethod
    @isactive
    def geneName(df : DataSet):
        df_havana = Operation.newHavana(df).getDataFrame()
        genes = df_havana[df_havana['type'] == 'gene']['attributes']
        names = pd.DataFrame({'genes': genes.apply(split_rows)})
        return DataSet(names.reset_index(drop=True))
        
        
