# Advanced-Programming-Project
Collaborators: Mascagni Marianna, Ruggiero Alessia, Vincenzi Francesca
## Main aim
<!-- what is the aim of the software, what it does, in very general terms -->
## The gff3 file
The data on which the software works is stored in a GFF3 file, which stands for Generic Feature Format Version 3, called 'Homo_sapiens.GRCh38.85.gff3.gz'. This file contains the annotation of the sequences and for this reason it's only 37 MB large; actually this is the compressed form of the file (.gz).

GFF3 files are nine-column, tab-delimited, plain text files; they're actually conceived as tabular data. In the head of the file is usually present many metadata lines which start with:
- \## (meaning it's stable metadata)
- #! (meaning experimental metadata)
- \###
- \# (for human readable comments)

All these metadata have to be ignored and removed from the file for its analysis.
*In the next section it will be described how and where.*

Also, for each line, the empty columns are denoted with a '.' .

The nine columns, also called fields, are the following: seqid, source, type, start, end, score, strand, phase, attribute (which contains a list of seven features in the form tag=value separated by semicolumns).

## Data access
In order to work and deal with the annotation data, the GFF3 file is transformed into a DataFrame object of Pandas (a Python library for dealing with tabular data).
For the realization of this purpose, the class **Reader_gff3** behaves as a dataset reader which takes the dataset in GFF3 format and creates a correspondant Pandas DataFrame. This one is actually returned by the Reader_gff3 function as an instance of the class Dataset_gff3.
The Reader_gff3 class is a subclass of the abstract class *Reader*, which is a general abstract interface.
> argomenta di più ?

As stated before, the Reader_gff3 class returns a Dataset_gff3 instance, that has as input the Pandas DataFrame corresponding to the original GFF3 file. The class **Dataset_gff3** is a subclass of the **Dataset** class: the first one is peculiar for the GFF3 case; whereas the second one is a class defining a generic tabular data . Then, the Dataset_gff3 class takes a Pandas DataFrame (that's actually deriving from the GFF3 file) as input and modifies it to make it properly structured for the obtaining of the insights over data.
> detta male casomai riguardaci

In particular, the modifications are:
- removing of all the metadata
- replace the missing values (labeled with '.') with NaN values

Once the modifications are done, the Pandas DataFrame resulting from Dataset_gff3 becomes an instance of its superclass Dataset.
Then the Dataset object corresponding to the cleaned GFF3 file can be used to get the insights from the annotation file.


## Dataset operations
The software allows to get a number of insights over the annotation data. These are:
1. Information about columns : get the basic information about the dataset
2. List seqIDs : obtain the list of unique sequence IDs available in the dataset
3. List of types : obtain the list of unique type of operations available in the dataset
4. Count features in 'source' : count the number of features provided by the same source
5. Count entries in 'type' : count the number of entries for each type of operation
6. Information about entire chromosomes : derive a new dataset containing only the information about entire chromosomes
7. Calculate the fraction of unassembled sequences : calculate the fraction of unassembled sequences from source GRCh38
8. Display entries from 'havana', 'ensembl', 'ensembl_havana' : obtain a new dataset containing only entries from source 'ensembl', 'havana' and 'ensembl_havana'
9. Count entries from new_havana : count the number of entries for each type of operation for the dataset containing containing only entries from source 'ensembl', 'havana'and 'ensembl_havana'
10. Genes names : return the gene names from the dataset containing containing only entries from source 'ensembl', 'havana' and 'ensembl_havana'

<!-- what are these, how they work (what are the input and the output), describe briefly what each of them do -->
## User interface
<!-- web pages, how it is built, Flask -->
