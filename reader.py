##reader class for project Advanced programming

import pandas as pd
from abc import ABC, abstractmethod
from dataset import Dataset, Dataset_gff3


class Reader(ABC):
    @staticmethod
    @abstractmethod
    def read(file):
        pass


class Reader_gff3(Reader):
    @staticmethod
    def read(file):
        df = pd.read_table(file, delimiter="\t",
                           names=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
        # invece di pulire il df in Dataset, possiamo pulirlo direttamente quando lo leggiamo con : skiprows, quotechar

        return Dataset_gff3(df)