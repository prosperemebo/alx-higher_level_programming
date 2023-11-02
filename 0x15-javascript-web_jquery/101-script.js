function main() {
  const addItem = $('#add_item');
  const removeItem = $('#remove_item');
  const clearList = $('#clear_list');

  addItem.click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  removeItem.click(function () {
    const list = $('ul.my_list');
    if (list.children('li').length > 0) {
      list.children('li:last').remove();
    }
  });

  clearList.click(function () {
    $('ul.my_list').empty();
  });
}

$(document).ready(main);
