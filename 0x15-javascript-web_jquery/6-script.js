function main() {
  const updateHeader = $('#update_header')
  
 updateHeader .click(function () {
    $('header').text('New Header!!!');
  });
}

$(document).ready(main);
