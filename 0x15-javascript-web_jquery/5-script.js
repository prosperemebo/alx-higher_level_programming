function main() {
  const addItem = $('#add_item');
  const newItem = $('<li>Item</li>');

  addItem.click(function () {
    $('ul.my_list').append(newItem);
  });
}

$(document).ready(main);
