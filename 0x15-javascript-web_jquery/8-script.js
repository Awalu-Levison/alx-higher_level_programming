//  fetch and list the title for all movies by using this URL:
//  https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
	$('UL#list_movies').append(...data.results.map(movie => '<li>${movie.title}</li>'));
});
