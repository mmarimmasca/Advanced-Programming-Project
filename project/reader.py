##reader class for project Advanced programming

import pandas as pd
from abc import ABC, abstractmethod
from dataset import DataSet, DataSetGff3


class Reader(ABC):
    @staticmethod
    @abstractmethod
    def read(file):
        pass


class ReaderGff3(Reader):
    @staticmethod
    def read(file):
        df = pd.read_table(file, delimiter="\t",
                           names=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
        # invece di pulire il df in Dataset, possiamo pulirlo direttamente quando lo leggiamo con : skiprows, quotechar

        return DataSetGff3(df)