
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
		console.log("local " + local);
		console.log("visitante " + visitante);

		$.get('/euro2016/edita_partido_ajax/', {partido_id: partidoid,
												local: local,
												visitante: visitante,
												}
		//Voy a intentar que al usuario le aparezca un feedback de las modificaciones
		, function()
		{							
			var botonedit = '#b_edit_' + partidoid;
			//location.reload();
			/*
			$(botonedit).animate(
	            {"opacity": "0.15"},
	            "fast")
                .animate(
	            {"opacity": "1"},
	            "fast", function()
	            {
	            	$(this).html("Ok*");
	            	var tr = '#tr_' + partidoid;
	            	$(tr).css("background-color", "lightblue");
	            	var td = '#td_actualizar_' + partidoid;
	            	$(td).show();
	            	location.reload();
	            });
	        */

		});
	});

	/*
		Voy a intentar que una funcion me actualice todo el cuadro en formato tabla
	*/
	$('.list_partido_ajax').click(function()
	{
		console.log("pulso listado");
		//me traigo el usuario
		usuario = $(this).attr("data-usuario");
		console.log("me traigo el user id " + usuario);
		$.getJSON('/euro2016/list_partido_ajax/', {usuario: usuario}
		, function(data)
		{							
			console.log("me traigo los datos de list");
			//console.log(data);
			for (var key in data)
			{
				if (data.hasOwnProperty(key))
				{
					
					var partidoid;
					var local;
					var visitante;
					partidoid = data[key]
					id_local = '#gol_local_' + partidoid;
					id_visitante = '#gol_visitante_' + partidoid;
					local = $(id_local).val();
					visitante = $(id_visitante).val();
					
					$.get('/euro2016/edita_partido_ajax/', {partido_id: partidoid,
												local: local,
												visitante: visitante,
					});
					
					console.log(partidoid+" "+local+" "+visitante);
				}				
			}
			console.log("terminoy recargo");
			location.reload();
		});
		
	});

	$(".b_refresh").click(function() {
		console.log("refresco");
        location.reload();
	});

});