# Advanced Programming project
# Main

from reader import ReaderGff3
import operations
from operations import *
from flask import Flask, render_template

app = Flask(__name__) # creating a Flask application named '???' associated with the variable 'app'

# Reading and cleaning of the 'Homo_sapiens.GRCh38.85.gff3' file and creation of the corresponding DataSet object
dataframe_gff3 = (ReaderGff3.read('Homo_sapiens.GRCh38.85.gff3')).getDataFrame() # reading the GFF3 file with ReaderGff3, then cleaning the resulting pd.DataFrame by using the class DataSetGff3 and finally returning it as pd.DataFrame
dataset = DataSet(dataframe_gff3) # casting the pd.DataFrame (of the GFF3 file) to a DataSet instance for performing the operations

# Section of code for marking as active/inactive the operations 
d = {} # creating an empty dictionary that will contain items of the type  name of the method : 'active'/'inactive'
cls = getattr(operations, 'Operation') # assigning the class 'Operation' to a variable
method_list = [method for method in dir(Operation) if method.startswith('__') is False] # getting the list of the names of the methods of the class 'Operation'

for e in method_list:      # for each of the methods' names :
    func = getattr(cls, e) # assigning to the variable the method of the class 'Operation' with the current name ('e')
    if type(func(dataset)) == str: # if the returned value of the current method is a string ...
        d[e] = 'inactive'          # ... the string 'inactive' becomes the value associated with the key of 'd' corresponding to the current method's name
    else:                          # otherwise ...
        d[e] = 'active'            # ... the string 'active' becomes the value associated with that key


# Flask : for each view function it's returned a template of HTML
# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Page with the registry of operations
@app.route('/registry_operations')
def registry_operations():
    return render_template('list_operations.html', active = d)

# Page displaying the output of the operation 1
@app.route('/column_info')
def column_info():
    df = Operation.columnInfo(dataset)
    if type(df) == str:
        return render_template('style_operations.html', title = '1. Information about columns', df = df)
    else:
        df = df.getDataFrame().to_html()
        return render_template('style_operations.html', title = '1. Information about columns', df = df)

# Page displaying the output of the operation 2 (preview)
@app.route('/list_seqids')
def list_seqids():
    df = Operation.listSeqIds(dataset)
    if type(df) == str:
        return render_template('style_operations.html', title = '2. List seqIDs', df = df)
    else:
        df = df.getDataFrame().to_html(justify='center',max_rows=20)
        return render_template('style_non_tot.html', title = '2. List seqIDs', df = df, redirect = '/list_seqids_tot')

# Page displaying the output of the operation 2 (complete)
@app.route('/list_seqids_tot')
def list_seqids_tot():
    df = Operation.listSeqIds(dataset).getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = '2. List seqIDs', df = df)

# Page displaying the output of the operation 3
@app.route('/list_types')
def list_types():
    df = Operation.listTypes(dataset)
    if type(df) == str:
        pass
    else:
        df = df.getDataFrame().to_html(justify='center',)
    return render_template('style_operations.html', title = '3. List of types', df = df)

# Page displaying the output of the operation 4
@app.route('/count_features_in_source')
def count_features_in_source():
    df = Operation.countFeaturesInSource(dataset)
    if type(df) == str:
        pass
    else:
        df = df.getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = "4. Count features in 'source'", df = df)

# Page displaying the output of the operation 5
@app.route('/count_entries_4type')
def count_entries_4type():
    df = Operation.countEntriesForType(dataset)
    if type(df) == str:
        pass
    else:
        df = df.getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = "5. Count entries in 'type'", df = df)

# Page displaying the output of the operation 6 (preview)
@app.route('/info_entirechroms')
def info_entirechroms():
    df = Operation.infoEntireChroms(dataset)
    if type(df) == str:
        return render_template('style_operations.html', title = '6. Information about entire chromosomes', df = df)
    else:
        df = df.getDataFrame().to_html(justify='center', max_rows=20)
        return render_template('style_non_tot.html', title = '6. Information about entire chromosomes', df = df, redirect = '/chroms_tot')

# Page displaying the output of the operation 6 (complete)
@app.route('/chroms_tot')
def chroms_tot():
    df = Operation.infoEntireChroms(dataset).getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = '6. Information about entire chromosomes', df = df)

# Page displaying the output of the operation 7
@app.route('/fraction_unassembled')
def fraction_unassembled():
    df = Operation.fractionUnassembled(dataset)
    if type(df) == str:
        pass
    else:
        df = df.getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = '7. Calculate the fraction of unassembled sequences', df = df)

# Page displaying the output of the operation 8 (preview)
@app.route('/new_havana')
def new_havana():
    df = Operation.newHavana(dataset)
    if type(df) == str:
        return render_template('style_operations.html', title = "8. Display entries from 'havana', 'ensembl', 'ensembl_havana'", df = df)
    else:
        df = df.getDataFrame().to_html(justify='center', max_rows=20)
        return render_template('style_non_tot.html', title = "8. Display entries from 'havana', 'ensembl', 'ensembl_havana'", df = df, redirect = '/new_havana_tot')

# Page displaying the output of the operation 8 (complete)
@app.route('/new_havana_tot')
def new_havana_tot():
    df = Operation.newHavana(dataset).getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = "8. Display entries from 'havana', 'ensembl', 'ensembl_havana'", df = df)

# Page displaying the output of the operation 9
@app.route('/count_entries_new_havana')
def count_entries_new_havana():
    df = Operation.countEntriesNewHavana(dataset)
    if type(df) == str:
        pass
    else:
        df = df.getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = "9. Count entries from 'havana', 'ensembl', 'ensembl_havana'", df = df)

# Page displaying the output of the operation 10 (preview)
@app.route('/gene_name')
def gene_name():
    df = Operation.geneName(dataset)
    if type(df) == str:
        return render_template('style_operations.html', title = '10. Genes names', df = df)
    else:
        df = df.getDataFrame().to_html(justify='center', max_rows=20)
        return render_template('style_non_tot.html', title = '10. Genes names', df = df, redirect = '/gene_name_tot')

# Page displaying the output of the operation 10 (complete)
@app.route('/gene_name_tot')
def gene_name_tot():
    df = Operation.geneName(dataset).getDataFrame().to_html(justify='center')
    return render_template('style_operations.html', title = '10. Genes names', df = df)

# Project specification page
@app.route('/projectspecification')
def projectspecification():
    return render_template('projectspecification.html', title= 'Project Specification')


app.run()
