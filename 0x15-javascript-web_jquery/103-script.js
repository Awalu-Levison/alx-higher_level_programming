// A avaScript script that fetches and prints
// how to say “Hello” depending on the language
$('document').ready(function () {
  $('INPUT#btn_translat').click(translate);
  $('INPUT#language_code').focus(function () {
      $(this).keydown(function (e) {
       if (e.keycode === 13) {
	       translate();
       }
      });
  });
});

// translation function to be called upon
function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
};
