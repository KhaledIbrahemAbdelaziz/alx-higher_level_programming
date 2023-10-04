$('document').ready(function () {
  $('INPUT#btn_translate').click(trans);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        trans();
      }
    });
  });
});

function trans () {
  const uRL = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(uRL + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
