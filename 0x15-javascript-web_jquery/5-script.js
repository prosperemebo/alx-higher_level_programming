function main() {
  const addItem = $('#add_item');

  addItem.click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
}

$(document).ready(main);
