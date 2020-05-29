import joblib
from flask import Flask
from document_classification.document_analyzer import document_analyzer
from document_classification.model_trainer import do_nothing

app = Flask(__name__)
app.register_blueprint(document_analyzer, url_prefix='/analyzer')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    return "<h1>document classification</h1>"


@app.before_first_request
def load_models():
    global model
    model = joblib.load(open('document_classification/model.pickle', 'rb'))