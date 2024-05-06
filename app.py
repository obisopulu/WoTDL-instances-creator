import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import ontospy

app = Flask(__name__)

def console():
    model = ontospy.Ontospy('ontology/ontology.x', verbose=True)
    with open('ontology/ontology.x') as f:
        contents = f.read()
    
    return str(contents)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'image/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')
    


@app.route('/ui')
def ui():
    return render_template('ui.html')


############################################### 
# UPLOAD ONTOLOGY #
###############################################
UPLOAD_FOLDER = 'ontology'
ALLOWED_EXTENSIONS = {'txt', 'rdf', 'owl', 'ttl', 'xml', 'obo', 'json', 'SPARQL', 'n3', 'nt', 'nq'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadOntology', methods=['POST'])
def uploader():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '': 
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #fileextension = secure_filename(file.filename).split(".")[1]
            #filename = "ontology." + fileextension
            filename = "ontology.x"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    printer = ''.join([str(item) for item in console()])
    return jsonify(results = printer)

############################################### 
# UPLOAD ONTOLOGY #
################################################

@app.route('/generate', methods = ['POST'])
def get_generate():
    jsdata = request.form['gen_data']

    with open('ontology/ontology.rdf', 'w') as f:
        f.write(jsdata)
        
    return jsdata


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)