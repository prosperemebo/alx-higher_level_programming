function fetchTranslationHandler() {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  const languageCode = $('#language_code').val();

  $.get(apiUrl, { lang: languageCode }, function (data) {
    $('#hello').text(data.hello);
  });
}

function onKeyPressHandler(e) {
  if (e.which === 13) {
    fetchTranslationHandler();
  }
}

function main() {
  $('#btn_translate').click(fetchTranslationHandler);
  $('#language_code').keypress(onKeyPressHandler);
}

$(document).ready(main);
