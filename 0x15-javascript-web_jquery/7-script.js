$get('https://swapi-api.alx-tools.com/api/people/5/?format=json') function(data) {
	const star_war = data.name
	$('#character').text(star_war)
};
