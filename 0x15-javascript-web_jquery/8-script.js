$.get('https://swapi.co/api/films?format=json', function (data) {
  let allMovies = data.results;

  for (let i = 0; i < allMovies.length; i++) {
    console.log(allMovies[i]);
    $('UL#list_movies').append('<li>' + allMovies[i].title + '</li>');
  }
});
