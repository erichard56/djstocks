$('document').ready(function() {
	$('form[name=edit-item]').submit(function(evt) {
		evt.preventDefault();
		
		var id = $(this).data('id');
		var name = $('input[name=item-name]').val();
		var desc = $('textarea[name=item-descrp]').val();
		var cat = $('select[name=item-category]').val();
		var price = $('input[name=item-price]').val();
		var price_venta = $('input[name=item-price_venta]').val();
		
		if(name == '') {
			alert('Por favor, introduzca un nombre');
			return false;
		}else if(price == '') {
			alert('Por favor, inserte un precio');
			return false;
		}else if(price_venta == '') {
			alert('Por favor, inserte un precio de venta');
			return false;
		}
		
		$.post('edit-item.php', {
			'act':'1',
			'itemid':id,
			'name':name,
			'desc':desc,
			'cat':cat,
			'price':price,
			'price_venta':price_venta
		},function(data) {
			if(data == '1') {
				alert('Se han realizado cambios con éxito');
				location.href = 'items.php';
			}else{
				alert('190 Algo salió mal. Por favor, inténtelo de nuevo');
				return false;
			}
		});
	});
	
	$('textarea[name=item-descrp]').keyup(function(evt) {
		var count = $(this).val().length;
		var limit = 400;
		var val = $(this).val();
		var t = $(this);
		
		if(count > limit){
			t.val(val.substr(0,400));
			var dif = 0;
		}else
			var dif = limit-count;
		$('span.item-desc-left').html('Descripción ('+dif+' caracteres restantes):');
	});
	
	$('input[name=item-price]').keyup(function(evt) {
		var val = $(this).val();
		var re = /^\d*\.{0,1}\d{0,2}$/;
		var t = $(this);
		
		if((re.test(val)) == false)
			t.val(val.substr(0, val.length - 1));
		return;
	});
	
	$('input[name=item-price_venta]').keyup(function(evt) {
		var val = $(this).val();
		var re = /^\d*\.{0,1}\d{0,2}$/;
		var t = $(this);
		
		if((re.test(val)) == false)
			t.val(val.substr(0, val.length - 1));
		return;
	});
});