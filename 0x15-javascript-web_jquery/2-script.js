function main() {
  const redHeader = $('#red_header')
  redHeader.click(function () {
    $('header').css('color', '#FF0000');
  });
}

$(document).ready(main);
