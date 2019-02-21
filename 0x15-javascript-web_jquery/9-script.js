$.get('https://fourtonfish.com/hellosalut/?lang=' + $('html').attr('lang'), (data) => {
  $('#hello').html(data.hello);
});
