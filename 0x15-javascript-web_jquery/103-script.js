$('document').ready(() => {
  function getHello () {
    let code = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + code, (data) => {
      $('#hello').html(data.hello);
    });
  }
  $('#btn_translate').click(getHello);
  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  });
});
