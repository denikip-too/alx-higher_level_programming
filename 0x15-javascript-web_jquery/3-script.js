// adds class red to <header> element when user clicks DIV#red_header tag

$('DIV#red_header').click(function () {
  $('header').addClass('red');
});
