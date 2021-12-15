from flask import Flask #, render_template
from flask_restful import Resource, reqparse
from models.hotel import HotelModel
     
class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}# select
        
class Hotel(Resource):
    argumentos = reqparse.RequestParser() #definindo o construtor, recebendo valor do json os dados declarados abaixo
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
     
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel não encontrado.'}, 404 # erro http que inf q alguma coisa não foi encontrada
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' já existe.".format(hotel_id)}, 400 # restringindo id
        
        dados = Hotel.argumentos.parse_args()# chamando o construtor
        hotel = HotelModel(hotel_id, **dados) 
        hotel.save_hotel()
        return hotel.json(), 200
        #return render_template('post.html', hotel.json()), 200
       
    def put(self, hotel_id):# se passar um id que já existe ele altera, senão existir ele cria um novo
        dados = Hotel.argumentos.parse_args()# chave e valor de todos os argumentos passados
        hotel_encontrado = HotelModel.find_hotel(hotel_id)   
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados) 
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200 # ok
        hotel = HotelModel(hotel_id, **dados) # desempacotando dados
        hotel.save_hotel()
        return hotel.json(), 201 # criado  
    
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel excluído.'}, 200
        return {'message': 'Hotel não encontrado.'}, 404