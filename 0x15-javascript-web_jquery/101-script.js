function addItemHandler() {
  const newItem = $('<li>Item</li>');
  $('ul.my_list').append(newItem);
}

function removeItemHandler() {
  const list = $('ul.my_list');
  if (list.children('li').length > 0) {
    list.children('li:last').remove();
  }
}

function clearListHandler() {
  $('ul.my_list').empty();
}

function main() {
  const addItem = $('#add_item');
  const removeItem = $('#remove_item');
  const clearList = $('#clear_list');

  addItem.click(addItemHandler);
  removeItem.click(removeItemHandler);
  clearList.click(clearListHandler);
}

$(document).ready(main);
