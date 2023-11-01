function main() {
  const toggleHeader = $('#toggle_header');

  toggleHeader.click(function () {
    const header = $('header');

    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    }
  });
}

$(document).ready(main);
