##file con i metodi per le operazioni per progetto Advanced Programming

from reader import Reader_gff3
from operations import Operation
from flask import Flask, render_template
app = Flask(__name__)

dataframe_gff3 = (Reader_gff3.read('Homo_sapiens.GRCh38.85.gff3')).get_data_frame()


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/active_operations')
def active_operations():
    return render_template('operations.html')


@app.route('/column_info')
def column_info():
    if type(Operation.column_info(dataframe_gff3)) == str:
        df = Operation.column_info(dataframe_gff3)
        return f'''<html>
            <head><title>1. Information about the dataset</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>1. Information about the dataset</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.column_info(dataframe_gff3).get_data_frame()).to_html()
        return f'''<html>
        <head><title>1. Information about the dataset</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>1. Information about the dataset</h2>
        <p>{df}</p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''


@app.route('/list_seqids')
def list_seqids():
    if type(Operation.list_seqids(dataframe_gff3)) == str:
        df = Operation.list_seqids(dataframe_gff3)
        return f'''<html>
            <head><title>2. List of seqIDs</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body >
            <h2>2. List of seqIDs</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
 
    else:
        df = (Operation.list_seqids(dataframe_gff3).get_data_frame()).to_html(justify='center',max_rows=20)
        return f'''<html>
            <head><title>2. List of seqIDs</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>2. List of seqIDs</h2>
            <p><cellspacing="3">{df}</p>
            <p style='border-left: 6px solid blue; background-color: #E0FFFF;line-height: 2;'>&nbsp Only the first and last 10 rows of the dataframe are displayed, if you want to see the entire table click <a href='/list_seqids_tot'>here</a></p>
            <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> 
            Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
            </body>
            </html>'''

@app.route('/list_seqids_tot')
def list_seqids_tot():
    df = (Operation.list_seqids(dataframe_gff3).get_data_frame()).to_html(justify='center')
    return f'''<html>
            <head><title>2. List of seqIDs</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    
    
@app.route('/list_types')
def list_types():
    if type(Operation.list_types(dataframe_gff3)) == str:
        df = Operation.list_types(dataframe_gff3)
        return f'''<html>
            <head><title>3. List of types</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>3. Lif of types</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.list_types(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>3. List of types </title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>3. List of types</h2>
        <p><cellspacing="3">{df}</p>
        <p style='border-left: 6px solid blue; background-color: #E0FFFF;line-height: 2;'>&nbsp Only the first and last 10 rows of the dataframe are displayed, if you want to see the entire table click <a href='/list_types_tot'>here</a></p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> 
            Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/list_types_tot')
def list_types_tot():
    df = (Operation.list_types(dataframe_gff3).get_data_frame()).to_html(justify='center')
    return f'''<html>
            <head><title>3. List of types</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''

@app.route('/count_features_in_source')
def count_features_in_source():
    if type(Operation.count_features_in_source(dataframe_gff3)) == str:
        df = Operation.count_features_in_source(dataframe_gff3)
        return f'''<html>
            <head><title>4. Count features in 'source'</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>4. Count features in 'source'</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.count_features_in_source(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>4. Count features in 'source'</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>4. Count features in 'source'</h2>
        <p><cellspacing="3">{df}</p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/count_entries_4type')
def count_entries_4type():
    if type(Operation.count_entries_4type(dataframe_gff3)) == str:
        df = Operation.count_entries_4type(dataframe_gff3)
        return f'''<html>
            <head><title>5. Count entries in 'type'</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>5. Count entries in 'type'</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.count_entries_4type(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>5. Count entries in 'type'</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>5. Count entries in 'type'</h2>
        <p><cellspacing="3">{df}</p>
        <p style='border-left: 6px solid blue; background-color: #E0FFFF;line-height: 2;'>&nbsp Only the first and last 10 rows of the dataframe are displayed, if you want to see the entire table click <a href='/type_tot'>here</a></p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/type_tot')
def type_tot():
    df = (Operation.count_entries_4type(dataframe_gff3).get_data_frame()).to_html(justify='center')
    return f'''<html>
            <head><title>5. Count entries in 'type'</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''

@app.route('/info_entirechroms')
def info_entirechroms():
    if type(Operation.info_entirechroms(dataframe_gff3)) == str:
        df = Operation.info_entirechroms(dataframe_gff3)
        return f'''<html>
            <head><title>6. Information about entire chromosomes</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>6. Information about entire chromosomes</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.info_entirechroms(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>6. Information about entire chromosomes</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>6. Information about entire chromosomes</h2>
        <p><div style="overflow-x:auto;"><cellspacing="3">{df}</div></p>
        <p style='border-left: 6px solid blue; background-color: #E0FFFF;line-height: 2;'>&nbsp Only the first and last 10 rows of the dataframe are displayed, if you want to see the entire table click <a href='/chroms_tot'>here</a></p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/chroms_tot')
def chroms_tot():
    df = (Operation.info_entirechroms(dataframe_gff3).get_data_frame()).to_html(justify='center')
    return f'''<html>
            <head><title>6. Information about entire chromosomes</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <p><div style="overflow-x:auto;"><cellspacing="3">{df}</div></p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''

@app.route('/fraction_unassembled')
def fraction_unassembled():
    if type(Operation.fraction_unassembled(dataframe_gff3)) == str:
        df = Operation.fraction_unassembled(dataframe_gff3)
        return f'''<html>
            <head><title>7. Calculate the fraction of unassembled sequences</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>7. Calculate the fraction of unassembled sequences</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.fraction_unassembled(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>7. Calculate the fraction of unassembled sequences</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>7. Calculate the fraction of unassembled sequences</h2>
        <p><cellspacing="3">{df}</p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
            <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/new_havana')
def new_havana():
    if type(Operation.new_havana(dataframe_gff3)) == str:
        df = Operation.new_havana(dataframe_gff3)
        return f'''<html>
            <head><title>8. Entries from 'havana', 'ensembl' and 'ensembl_havana</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>8. Display entries from 'havana', 'ensembl' and 'ensembl_havana'</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.new_havana(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>8. Entries from 'havana', 'ensembl', 'ensembl_havana'</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>8. Display entries from 'havana', 'ensembl' and 'ensembl_havana'</h2>
        <p><div style="overflow-x:auto;"><cellspacing="3">{df}</div></p>
        <p style='border-left: 6px solid blue; background-color: #E0FFFF;line-height: 2;'>&nbsp Only the first and last 10 rows of the dataframe are displayed, if you want to see the entire table click <a href='/new_havana_tot'>here</a></p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
        <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/new_havana_tot')
def new_havana_tot():
    df = (Operation.new_havana(dataframe_gff3).get_data_frame()).to_html(justify='center')
    return f'''<html>
            <head><title>8. Entries from 'havana', 'ensembl' and 'ensembl_havana'</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <p><div style="overflow-x:auto;"><cellspacing="3">{df}</div></p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''

@app.route('/count_entries_new_havana')
def count_entries_new_havana():
    if type(Operation.count_entries_new_havana(dataframe_gff3)) == str:
        df = Operation.column_info(dataframe_gff3)
        return f'''<html>
            <head><title>9. Count entries from new_havana</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>9. Count entries from new_havana/h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.column_info(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>9. Count entries from new_havana</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>9. Count entries from new_havana</h2>
        <p><cellspacing="3">{df}</p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
        <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/gene_name')
def gene_name():
    if type(Operation.gene_name(dataframe_gff3)) == str:
        df = Operation.gene_name(dataframe_gff3)
        return f'''<html>
            <head><title>10. Genes names</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <h2>10. Genes names</h2>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
    else:
        df = (Operation.gene_name(dataframe_gff3).get_data_frame()).to_html(justify='center', max_rows=20)
        return f'''<html>
        <head><title>10. Genes names</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
        <body>
        <h2>10. Genes names</h2>
        <p><cellspacing="3">{df}</p>
        <p style='border-left: 6px solid blue; background-color: #E0FFFF;line-height: 2;'>&nbsp Only the first and last 10 rows of the dataframe are displayed, if you want to see the entire table click <a href='/gene_name_tot'>here</a></p>
        <p> If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
        <div style="position:relative">
        <p style="position:fixed;bottom:2px;width:100%;font-size:14px;font-color:#696969:;text-align:center; background-color:white; "> Advanced Programming project, Genomics 2022/2023 - Ruggiero Alessia, Vincenzi Francesca, Mascagni Marianna  </p></div>
        </body>
        </html>'''

@app.route('/gene_name_tot')
def gene_name_tot():
    df = (Operation.gene_name(dataframe_gff3).get_data_frame()).to_html(justify='center')
    return f'''<html>
            <head><title>10. Genes names</title>
            <link rel="stylesheet" type="text/css" href="/static/styles/main.css" /></head>
            <body>
            <p><cellspacing="3">{df}</p>
            </p>If you want to access other operations, click <a href='active_operations'>here</a>, otherwise go back to <a href='/'>Homepage</a></p>
            </body></html>'''
app.run()
