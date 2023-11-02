function main() {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  const translateButton = $('#btn_translate');

  translateButton.click(function () {
    const languageCode = $('#language_code').val();

    $.get(url, { lang: languageCode }, function (data) {
      $('#hello').text(data.hello);
    });
  });
}

$(document).ready(main);
