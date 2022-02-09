$(function () {
  let link = 'https://swapi.co/api/people/5/?format=json';
  $.get(link, function (data) {
    $('#character').html(data.name);
  });
});
