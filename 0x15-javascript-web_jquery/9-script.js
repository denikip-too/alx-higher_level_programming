// fetches from URL and displays the value of hello in the HTML tag DIV#hello

const fourtonFish = $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
