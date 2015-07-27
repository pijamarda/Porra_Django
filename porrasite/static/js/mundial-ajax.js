
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

	$('.edit_ajax').click(function()
	{
		console.log("actualizando partido");
		var partidoid;
		var local;
		var visitante;
		partidoid = $(this).attr("data-partidoid");
		id_local = '#gol_local_' + partidoid;
		id_visitante = '#gol_visitante_' + partidoid;
		//console.log('Partidoid: ' + partidoid + ' local: '+local + ' visitante: ' + visitante);
		local = $(id_local).val();
		visitante = $(id_visitante).val();
		console.log('nuevo local:' + local);
		console.log('nuevo visitante:' + visitante);
		$.get('/mundial/edita_partido_ajax/', {partido_id: partidoid,
												local: local,
												visitante: visitante,
												}, function(data)
		{
			//console.log("llego dentro del get del javascript");
			var etiqueta_ida = '#gol_local_' + partidoid;
			var etiqueta_vuelta = '#gol_visitante_' + partidoid;
			//console.log(etiqueta);
			//console.log(data.ida);
			//console.log(data.vuelta);
			//#console.log(data[1]);
			$(etiqueta_ida).html(local);
			$(etiqueta_vuelta).html(visitante);		
		});
	});
});