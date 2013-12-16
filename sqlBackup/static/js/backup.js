$(document).ready(function(){

$( '.accion').click(function() {
		var padre = $(this).attr('name');
  		$(padre).slideToggle( "slow" );
	});

});