// fetch from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML
$('document').ready(function () {
	$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
		$('DIV#hello').text(data.hello);
	});
});
