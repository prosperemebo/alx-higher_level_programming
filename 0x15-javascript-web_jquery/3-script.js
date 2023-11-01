function main() {
  const redHeader = $('#red_header')

  redHeader.click(function () {
    $('header').addClass('red');
  });
}

$(document).ready(main);
