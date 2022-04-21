// toggles class of <header> element when user clicks DIV#toggle_header tag

$('DIV#toggle_header').click(function () {
  $('header').addClass(function (index, currentClass) {
    let addedClass;
    if (currentClass === 'red') {
      addedClass = 'green';
    }
  });
});
