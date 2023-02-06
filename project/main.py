##file con i metodi per le operazioni per progetto Advanced Programming

from reader import Reader_gff3
import operations
from operations import *
from flask import Flask, render_template
app = Flask(__name__)

dataframe_gff3 = (Reader_gff3.read('Homo_sapiens.GRCh38.85.gff3')).get_data_frame() #cleaned the dataframe by using the class Dataset_gff3
dataframe = Dataset(dataframe_gff3).get_data_frame() #casted the dataframe from gff3 to a normal dataset for operations


d = {}
cls = getattr(operations, 'Operation') #assign the class 'Operation' to a variable
method_list = [method for method in dir(Operation) if method.startswith('__') is False] #get list of the names of the methods in 'Operation'

for e in method_list:
    func = getattr(cls, e) #assign the method of the class 'Operation' with name equal to the variable e
    if type(func(dataframe)) == str:
        d[e] = 'inactive'
    else:
        d[e] = 'active'


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/active_operations')
def active_operations():
    return render_template('list_operations.html', active = d)


@app.route('/column_info')
def column_info():
    df = Operation.column_info(dataframe)
    if type(df) == str:
        return render_template('style_operations.html', title = '1. Information about columns', df = df)
    else:
        df = (df.get_data_frame()).to_html()
        return render_template('style_operations.html', title = '1. Information about columns', df = df)


@app.route('/list_seqids')
def list_seqids():
    df = Operation.list_seqids(dataframe)
    if type(df) == str:
        return render_template('style_operations.html', title = '2. List seqIDs', df = df)
    else:
        df = (df.get_data_frame()).to_html(justify='center',max_rows=20)
        return render_template('style_non_tot.html', title = '2. List seqIDs', df = df, redirect = '/list_seqids_tot')


@app.route('/list_seqids_tot')
def list_seqids_tot():
    df = (Operation.list_seqids(dataframe).get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = '2. List seqIDs', df = df)

    
    
@app.route('/list_types')
def list_types():
    df = Operation.list_types(dataframe)
    if type(df) == str:
        pass
    else:
        df = (df.get_data_frame()).to_html(justify='center',)
    return render_template('style_operations.html', title = '3. List of types', df = df)


@app.route('/count_features_in_source')
def count_features_in_source():
    df = Operation.count_features_in_source(dataframe)
    if type(df) == str:
        pass
    else:
        df = (df.get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = "4. Count features in 'source'", df = df)
        
        
@app.route('/count_entries_4type')
def count_entries_4type():
    df = Operation.count_entries_4type(dataframe)
    if type(df) == str:
        pass
    else:
        df = (df.get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = "5. Count entries in 'type'", df = df)
        
        
@app.route('/info_entirechroms')
def info_entirechroms():
    df = Operation.info_entirechroms(dataframe)
    if type(df) == str:
        return render_template('style_operations.html', title = '6. Information about entire chromosomes', df = df)
    else:
        df = (df.get_data_frame()).to_html(justify='center', max_rows=20)
        return render_template('style_non_tot.html', title = '6. Information about entire chromosomes', df = df, redirect = '/chroms_tot')


@app.route('/chroms_tot')
def chroms_tot():
    df = (Operation.info_entirechroms(dataframe).get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = '6. Information about entire chromosomes', df = df)


@app.route('/fraction_unassembled')
def fraction_unassembled():
    df = Operation.fraction_unassembled(dataframe)
    if type(df) == str:
        pass
    else:
        df = (df.get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = '7. Calculate the fraction of unassembled sequences', df = df)

@app.route('/new_havana')
def new_havana():
    df = Operation.new_havana(dataframe)
    if type(df) == str:
        return render_template('style_operations.html', title = "8. Display entries from 'havana', 'ensembl', 'ensembl_havana'", df = df)

    else:
        df = (df.get_data_frame()).to_html(justify='center', max_rows=20)
        return render_template('style_non_tot.html', title = "8. Display entries from 'havana', 'ensembl', 'ensembl_havana'", df = df, redirect = '/new_havana_tot')


@app.route('/new_havana_tot')
def new_havana_tot():
    df = (Operation.new_havana(dataframe).get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = "8. Display entries from 'havana', 'ensembl', 'ensembl_havana'", df = df)


@app.route('/count_entries_new_havana')
def count_entries_new_havana():
    df = Operation.count_entries_new_havana(dataframe)
    if type(df) == str:
        pass
    else:
        df = (df.get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = '9. Count entries from new_havana', df = df)


@app.route('/gene_name')
def gene_name():
    df = Operation.gene_name(dataframe)
    if type(df) == str:
        return render_template('style_operations.html', title = '10. Genes names', df = df)
    else:
        df = (df.get_data_frame()).to_html(justify='center', max_rows=20)
        return render_template('style_non_tot.html', title = '10. Genes names', df = df, redirect = '/gene_name_tot')


@app.route('/gene_name_tot')
def gene_name_tot():
    df = (Operation.gene_name(dataframe).get_data_frame()).to_html(justify='center')
    return render_template('style_operations.html', title = '10. Genes names', df = df)


app.run()
