from pymongo import MongoClient
import json

def save_data(data) :

    client = MongoClient("mongodb+srv://isaac:Ppw72YR3iv.WqLC@cluster0.fx6ekbw.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database('data_raspberry')

    records = db.data_raspberry

    records.insert_one(data)
    
    print("Dados gravados no banco !")
    
def return_data() :
    
    dados = []
    
    client = MongoClient("mongodb+srv://isaac:Ppw72YR3iv.WqLC@cluster0.fx6ekbw.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database('data_raspberry')
    
    records = db.data_raspberry
    
    data_mongo = (list(records.find()))
    
    for data in data_mongo :
        data.pop('_id')
        dados.append(data)

   # Verificar o número de documentos atualizados
    return dados