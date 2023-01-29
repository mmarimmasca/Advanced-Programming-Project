##decorator and operations project Advanced programming

import pandas as pd
from dataset import Dataset, Dataset_gff3

# DECORATOR
# import inspect

global_l = ['column_info', 'list_seqids', 'list_types', 'count_features_in_source', 'count_entries_4type',
            'info_entirechroms', 'fraction_unassembled', 'new_havana', 'count_entries_new_havana', 'gene_name']


def split_rows(row):
    return str(row).split(';')[1].split('=')[1]
    
    
def isactive(f):
    def wrapper(*args):
        if f.__name__ in global_l:
            print('The function is marked as active, follow the results:')
            return f(*args)
        else:
            return ('Function not in the registry of active operations')

    return wrapper


class Operation:
    # 1
    @staticmethod
    @isactive
    def column_info(df):
        columns = pd.Series(dtype=object)
        types = pd.Series(dtype=object)
        for column in df:
            columns = columns.append(pd.Series(column))
            types = types.append(pd.Series(df[column].dtype))
        return Dataset(pd.DataFrame(data={'names of columns': columns, 'types': types}).reset_index(drop=True))

    # 2
    @staticmethod
    @isactive
    def list_seqids(df):
        return Dataset(pd.DataFrame({'seqIDs': df['seqid'].unique()}))

    # 3
    @staticmethod
    @isactive
    def list_types(df):
        return Dataset(pd.DataFrame({'types': df['type'].unique()}))

    # 4
    @staticmethod
    @isactive
    def count_features_in_source(df):
        group_source = df.groupby('source')
        return Dataset(pd.DataFrame({'source': group_source.groups.keys(), 'source count': group_source.size().array}))

    # 5
    @staticmethod
    @isactive
    def count_entries_4type(df):
        group_type = df.groupby('type')
        return Dataset(pd.DataFrame({'types': group_type.groups.keys(), 'types count': group_type.size().array}))

    # 6
    @staticmethod
    @isactive
    def info_entirechroms(df):
        return Dataset(df.loc[lambda df: df['source'] == 'GRCh38'].reset_index(drop=True))

    # 7
    @staticmethod
    @isactive
    def fraction_unassembled(df):
        count_df = Operation.info_entirechroms(df).get_data_frame()
        fract_df = count_df.loc[lambda df: df['type'] == 'supercontig']
        return Dataset(pd.DataFrame({'unassembled/entire chromosomes': [f"{fract_df.shape[0]}/{count_df.shape[0]}"]}))

    # 8
    @staticmethod
    @isactive
    def new_havana(df):
        new_df = pd.DataFrame(df[df['source'].isin(['ensembl', 'havana', 'ensembl_havana'])])
        return Dataset(new_df.reset_index(drop=True))

    # 9
    @staticmethod
    @isactive
    def count_entries_new_havana(df):
        df_havana = Operation.new_havana(df).get_data_frame()
        group_type = df_havana.groupby('type')
        return Dataset(pd.DataFrame({'type': group_type.groups.keys(), 'count': group_type.size().array}))

    # 10
    @staticmethod
    @isactive
    def gene_name(df):
        df_havana = Operation.new_havana(df).get_data_frame()
        genes = df[df['type'] == 'gene']['attributes']
        names = pd.DataFrame({'genes': genes.apply(split_rows)})
        return Dataset(names.reset_index(drop=True))
        
        
