$('document').ready(() => {
  $('#add_item').click(() => {
    $('<li>Item</li>').appendTo('.my_list');
  });
  $('#remove_item').click(() => {
    let lastItem = $('li:last');
    if (lastItem) {
      lastItem.remove();
    }
  });
  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
