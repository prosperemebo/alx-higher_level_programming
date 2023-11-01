function main() {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function (data) {
    const movieList = data.results;
    const ulList = $('#list_movies');

    $.each(movieList, function (index, movie) {
      ulList.append($('<li>').text(movie.title));
    });
  });
}

$(document).ready(main);
