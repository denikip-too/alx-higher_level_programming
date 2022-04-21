// fetches the character name from a URL using JQuery API

const name = $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
