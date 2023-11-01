function main() {
  const toggleHeader = $('#toggle_header');
  const header = $('header');

  toggleHeader.click(function () {
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    }
  });
}

$(document).ready(main);
