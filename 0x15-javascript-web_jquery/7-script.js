$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('#character').html(data.name);
});
