$('document').ready(() => {
  $('#btn_translate').click(() => {
    let code = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + code, (data) => {
      $('#hello').html(data.hello);
    });
  });
});
