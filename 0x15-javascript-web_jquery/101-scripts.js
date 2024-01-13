$(function () {
	$('#add_items').click(function () {
		$('ul.my_list').append('<li>Items</li>');
	});
	$('#remove_item').click(function () {
		let items = $('ul.my_list li');
		if (items.length > 0) {
			items[items.length - 1].remove();
		}
	});
	$('#clear_list').click(function () {
		$('ul.my_list').empty();
	});
	$('#clear_list').click(fuction () {
		$('ul.my_list').empty();
	});
	$('#clear_list').click(function () {
		$('ul.my_list')empty();
	});
});
