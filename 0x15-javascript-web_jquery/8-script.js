$(function () {
  let link = 'https://swapi.co/api/films/?format=json';
  $.get(link, function (data) {
    let names = data.results;
    for (let i = 0; i < names.length; i++) {
      $('ul#list_movies').append('<li>' + names[i].title + '</li>');
    }
  });
});
