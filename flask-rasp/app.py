from flask import Flask
from functions.import_data import import_data
from database.database import save_data, return_data

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Navegue para a rota /rasp</h1>'

@app.route('/rasp')
def rasp():
    
    data = import_data()
    
    save_data(data)
    
    return '<h1>Os dados foram salvos ! </h1>'


@app.route('/rasp/all')
def rasp_all():

    return return_data()
    
if __name__ == '__main__':
    app.run()
