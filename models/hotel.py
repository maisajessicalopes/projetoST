from sql_alchemy import banco

class HotelModel(banco.Model): 
    __tablename__ = 'hoteis'
   
    hotel_id = banco.Column(banco.String, primary_key=True) # mapeando par o SQLAlchemy que essa classe é uma tabela no db
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40)) 
    
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade): #criando construtor init, self o proprio objeto
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def json(self): # pegar o objeto e transformar em dicionario que será convertido para json
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }    
     
    @classmethod    
    def find_hotel(cls, hotel_id): # metodo de classe, só acessa o id
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()# select * from hoteis where  hotel id = hotel id pegando o primeiro
        if hotel:
            return hotel
        return None   
    
    def save_hotel(self): # adicionando o próprio objeto ao banco
        banco.session.add(self)
        banco.session.commit()
        
    def update_hotel(self, nome, estrelas, diaria, cidade):   
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def delete_hotel(self):
          banco.session.delete(self)
          banco.session.commit() 