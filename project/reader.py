# Advanced programming project
# Reader and ReaderGff3 classes

import pandas as pd
from abc import ABC, abstractmethod
from dataset import DataSet, DataSetGff3


class Reader(ABC):
    ''' The Reader abstract class defines generally the procedure for reading a generic tabular data '''
    @staticmethod    
    @abstractmethod  
    def read(file):
        pass


class ReaderGff3(Reader):
    ''' The ReaderGff3 class is specific for reading a GFF3 file '''
    @staticmethod
    def read(file):
        ''' The 'read' method takes as input a file (GFF3), creates a Pandas DataFrame out of it and returns that as an instance of the DataSetGff3 class '''
        df = pd.read_table(file, delimiter="\t", names=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
        return DataSetGff3(df) 
