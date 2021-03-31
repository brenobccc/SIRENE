# encoding: utf-8
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin#CORS


app = Flask(__name__)
cors = CORS(app)#CORS
app.config['CORS_HEADERS'] = 'Content-Type'#CORS
 

@app.route('/')#rota padrão.
def predict():
	
	array = request.args.get('array')#pega as informações
	words_array=array.split(' ')#irá mandar as informações que estão entre um espaço' ' para a criação do array OUTPUT.
	print(words_array)#printo o array de palavras
	
	#print(type(words_array))	
	return jsonify(words_array)



if __name__ == '__main__':
    print('Loading model...')
 
    app.run(debug=True) 