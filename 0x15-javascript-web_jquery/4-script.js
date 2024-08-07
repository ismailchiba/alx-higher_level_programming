$('DIV#toggle_header').on('click', function () {
  const element = $('header');
  if (element.hasClass('red')) { element.removeClass('red').addClass('green'); } else if (element.hasClass('green')) { element.removeClass('green').addClass('red'); } else element.addClass('red');
});
