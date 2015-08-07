
$( document ).ready(function() {

	$('.sumaClass').click(function()
	{
		console.log("tramito el jquery");
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/mundial/suma_puntos/', {category_id: catid}, function(data)
		{
			console.log("llego dentro del get del javascript");
			$('#suma_puntos').html(data);			
		});
	});

	/*
		Funcion especifica para la edicion de los partidos de la euro2016
	*/
	$('.euro2016_edit_ajax').click(function()
	{
		//console.log("actualizando partido");
		var partidoid;
		var local;
		var visitante;

		/*
			Primero cojemos el atributo partidoid, que viene incluido en el template 
			grupo_equipos.html en la parte del boton.
			Cuando creamos el boton incluimos un parametro llamado data-partidoid
			y le pasamos el dato en formato django {{partidoid}}
		*/
		partidoid = $(this).attr("data-partidoid");

		/*
			Creamos 2 variables que almacenen las etiquetas correctas para saber de donde se tiene
			que traer los valores a cambiar,
			Estos identificadores se han puesto en el template grupo_equipos al declarar los input
			tambien con el tag del tipo django {{tag}}
		*/
		id_local = '#gol_local_' + partidoid;
		id_visitante = '#gol_visitante_' + partidoid;
		
		// Obtenemos ahora los nuevos valores del resultado del partido que queremos modificar
		local = $(id_local).val();
		visitante = $(id_visitante).val();
		
		/*
			Ahora llamamos a la URL declarada en django em urls.py con tipo: get
			y le pasamos como parametros get:
				- El id del partido
				- Los nuevos goles del local y del visitante
		*/

		$.get('/euro2016/edita_partido_ajax/', {partido_id: partidoid,
												local: local,
												visitante: visitante,
												});
		/*, function(data)
		{
			
				lo que hacemos aqui es actualizar los propios elementos input con los nuevos valores
				aunque yo creo que no haria falta...
			
			var etiqueta_ida = '#gol_local_' + partidoid;
			var etiqueta_vuelta = '#gol_visitante_' + partidoid;
			//console.log(etiqueta);
			//console.log(data.ida);
			//console.log(data.vuelta);
			//#console.log(data[1]);
			$(etiqueta_ida).html(local);
			$(etiqueta_vuelta).html(visitante);		
		});
		*/
	});
});