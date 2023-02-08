# Advanced programming project
# Reader and ReaderGff3 classes

import pandas as pd
from abc import ABC, abstractmethod
from dataset import DataSet, DataSetGff3


class Reader(ABC):
    ''' The Reader abstract class defines generally the procedure for reading a dataset '''
    @staticmethod     # decorating the 'read' method as a static method
    @abstractmethod   # decorating the 'read' method as an abstract method
    def read(file):
        pass


class ReaderGff3(Reader):
    ''' The ReaderGff3 class is specific for reading a GFF3 file '''
    @staticmethod
    def read(file):
        ''' The 'read' method takes as input a file (GFF3), creates a Pandas DataFrame out of it and returns that as an instance of the DataSetGff3 class '''
        df = pd.read_table(file, delimiter="\t", names=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
            # the 'read_table' method takes the file, uses the tabular space for delimiting the columns of the dataset and assignes to each column an element of the list 'names'
            # the output is assigned to the 'df' variable, which is a Pandas DataFrame
        return DataSetGff3(df) # the returned value is the dataset created as an instance of the class DataSetGff3
