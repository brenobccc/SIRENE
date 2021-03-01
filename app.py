from flask import Flask#importando o flask

app = Flask(__name__)#instanciando e inicializando a aplicação FLASK


#__________________________________________

@app.route('/')#rota para demonstração
def teste():
	return "<h1>testando</h1>"#retorna uma tag html com o nome testando


@app.route('/teste2')#2 rota para demonstração
def teste2():
	return "<br><h1>testando2</h1>"#retorna uma tag html com o nome testando

#__________________________________________



if __name__ == "__main__": #passo final
	app.run(debug=True,port="3000")	