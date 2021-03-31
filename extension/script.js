//alert("testando");

/*Links que me ajudaram a resolver:
https://www.docow.com/1230/onclick-na-extensao-do-chrome-nao-funciona.html
https://stackoverflow.com/questions/36324333/refused-to-execute-inline-event-handler-because-it-violates-csp-sandbox/36349056#36349056
*/

document.addEventListener('DOMContentLoaded', function(){document.getElementById("botao").addEventListener("click", fetchMl);}); // The handler also must go in a .js file function handler() 



function fetchMl(){
	//var tipo;
	var palavra;
	palavra = document.getElementById('array').value;
	//tipo = document.getElementById('valor').value;
	

	//Leio os valores e armazeno na var values
	//exemplo original,  const url = 'http://localhost:5000/predict?features=[2.5, 1.2, 3.4, 4.5]'
	//const url = 'http://localhost:5000/predict?features=['+valores+']'//URL da API junto com os valores para requisição
	//const url = 'http://127.0.0.1:5000?word='+palavra+'&model='+tipo;
	const url = 'http://127.0.0.1:5000?array='+palavra;
	//Método Fetch
	fetch(url)//mando por parametro minha url da API
	   .then(response => response.json())//resposta da promisse convertida em JSON
	   .then(n => {//visualização no console 
		console.log(n);
		//console.log(typeof(n))
		
		document.getElementById('result').innerHTML = n;
	   }) 
}


/*
function capturar(){
	var capturando="";
	capturando = document.getElementById('valor').value;
	document.getElementById('result').innerHTML = capturando
}*/
//fetchMl()//Chamando a função