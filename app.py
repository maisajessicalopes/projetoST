from flask import Flask #, request, render_template
from flask_restful import Api
from resources.hotel import Hoteis, Hotel


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ubuntu:1234@localhost:5432/ubuntu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # como falso para para de dar aviso e não sobrecarregar a aplicação e continua fazendo as alterações
api = Api(app)

@app.before_first_request # antes da primeira requisicão
def cria_banco():
    banco.create_all()

#@app.route("/index")    
#@app.route("/")
#def index():
#   return render_template('index.html')
      
#@app.route("/post")    
#def cadastrar():
#    return render_template('post.html')
      
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
# api.add_resource(Hotel, '/hoteis/cadastro')

if __name__ == '__main__':
    from sql_alchemy import banco                                                                   
    banco.init_app(app) # o import esta sendo importado aqui para não ser executado se for chamado de outro arquivo
    app.run(debug=True)
