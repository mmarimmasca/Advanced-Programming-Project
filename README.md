# Insights over the human genome
Collaborators: Mascagni Marianna, Ruggiero Alessia, Vincenzi Francesca <br>
Advanced Programming porject, Genomics 2022/2023
## Main aim
The software allows to adress some questions on the human genome by performing a series of operations on a GFF3 file, which is a genome annotation file.
## The gff3 file
The data on which the software works is stored in a GFF3 file, which stands for Generic Feature Format Version 3, called 'Homo_sapiens.GRCh38.85.gff3'. This file contains the annotation of the sequences.<br>
The file can be downloaded here : [link to file in Google Drive](https://drive.google.com/file/d/1AAke_vEC7LK0uasCoXE3Ge-KHeSYOWwK/view?usp=share_link)

GFF3 files are nine-column, tab-delimited, plain text files; they're actually conceived as tabular data. In the head of the file there usually are many metadata lines which start with:
- \## (meaning it's stable metadata)
- #! (meaning experimental metadata)
- \###
- \# (for human readable comments)

All these metadata have to be ignored and removed from the file for its analysis.
*In the next section it will be described how and where.* <br>
Also, for each line, the empty columns are denoted with a '.' .

The nine columns, also called fields, are the following: seqid, source, type, start, end, score, strand, phase, attribute (which contains a list of seven features in the form tag=value separated by semicolumns).

## Data access
In order to work and deal with the annotation data, the GFF3 file is transformed into a DataFrame object of Pandas (a Python library for dealing with tabular data).
For the realization of this purpose, a dataset reader specific for the GFF3 format (a class called ReaderGFF3) is implemented, based on a general abstract interface.<br>
The dataset reader returns a dataset object specific for the GFF3 format (an instance of the class DataSetGFF3), which is then modified in order to make it properly structured for the obtaining of the insights over data.

The modifications applied to the dataset are:
- removal of all the metadata
- replacement of the missing values (labeled with '.') with NaN values

The resulting object becomes an instance of its parent class DataSet, which will be then used to get the insights over the data contained.

A more detailed description of the software implementation can be visionated in the project specification.

## Dataset operations
The software allows to get some insights over the annotation data by performing a number of operations on the dataset. These are:
1. Information about columns : get the basic information about the dataset
2. List seqIDs : obtain the list of unique sequence IDs available in the dataset
3. List of types : obtain the list of unique type of operations available in the dataset
4. Count features in 'source' : count the number of features provided by the same source
5. Count entries in 'type' : count the number of entries for each type of operation
6. Information about entire chromosomes : derive a new dataset containing only the information about entire chromosomes
7. Calculate the fraction of unassembled sequences : calculate the fraction of unassembled sequences from source GRCh38
8. Display entries from 'havana', 'ensembl', 'ensembl_havana' : obtain a new dataset containing only entries from source 'ensembl', 'havana' and 'ensembl_havana'
9. Count entries from 'havana', 'ensembl', 'ensembl_havana' : count the number of entries for each type of operation for the dataset containing containing only entries from source 'ensembl', 'havana' and 'ensembl_havana'
10. Genes names : return the gene names from the dataset containing containing only entries from source 'ensembl', 'havana' and 'ensembl_havana'

These operations are contained in a registry of operations. Among those, the ones labeled as *active* can be executed over the dataset.

## User interface
The software can be accessed by users through a web page, supported on Flask. <br>
The homepage presents briefly the software and from there the registry of operations and the project specification can be accessed. <br>
The registry of operations opens in another page view where all the possible operations are listed and by selecting one of them another page view is opened where the result is displayed. <br>
For some of the operations (number 2, 6, 8, 10) the resulting dataset displayed is a preview of the complete one containing only the first and last 10 rows; the complete one can be accessed from the same page view. <br>
The project specification page view displays the description of the project in terms of software analysis, design and implementation, including CRC cards and UML class diagrams and their description.
