$('#btn_translate').click(translateHello);

$('#language-code').keypress(function(event) {
	//check if the key pressed is Enter key (code 13)
	if (event.which === 13) {
		translateHello();
	}
});

function translateHello() {
	const langCode = $('#language_code').val();

	$.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: langCode }, function(data) {
		$('#hello').text(data.hello);
	});
}
