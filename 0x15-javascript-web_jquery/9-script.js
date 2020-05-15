window.onload = function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (greeting) {
      $('div#hello').text(greeting.hello);
    }
  });
};
