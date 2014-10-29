
$( document ).ready(function() {

	$('#suma').click(function()
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
});