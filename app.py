from flask import Flask, request
from flask_cors import CORS, cross_origin#CORS: serve para quando eu for requisitar algo.


app = Flask(__name__) #instanciando e inicializando a aplicação FLASK

cors = CORS(app)#CORS
app.config['CORS_HEADERS'] = 'Content-Type'#CORS


@app.route('/test')
def teste():
	return 'teste2'

@app.route('/')#rota padrão
def predict():
	return '<h1>teste</h1>'
             

if __name__ == "__main__": #passo final
	app.run(debug=True,port="3000")	 
   







