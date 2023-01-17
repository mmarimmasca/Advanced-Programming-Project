from flask import Flask, request #'request' object represent the input of an html file 
#from tensorflow.core.profiler import 
webapp = Flask('web_application') #I create an obkect of the type 'Flask' that can deal with html inputs

@webapp.route('/custom') #path to follow to implement the html code
def homepage():

    givenname = request.args['givenname']
    
    return f'''
        <html>
            <header>
                <title>
                {givenname}'s Biography
                </title>
            </header>
            <body>
            <h1> {givenname}'s Biography </h1> 
            </body>
        </html>'''    

@webapp.route('/form')
def form():
    return f'''
        <html>
            <header>
                <title>
                Form
                </title>
            </header>
            <body>
                <form action='./custom'>
                    <p>Give name: <input type='text' name='givenname' /></p>
                    <input type='submit' name='send'/>
                </form>
            </body>
        </html>'''    

    
webapp.run()
