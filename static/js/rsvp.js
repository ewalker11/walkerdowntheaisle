Zepto(function($){
  $('#num_guests').on('change', function(e){
    while ($('.rsvp-row:not(.hidden)').length < e.target.value) {
      var hiddenRow = $('.hidden').first();
      hiddenRow.removeClass('hidden').addClass('visible');
    }
    while ($('.rsvp-row:not(.hidden)').length > e.target.value) {
      var hiddenRow = $('.rsvp-row:not(.hidden)').last();
      hiddenRow.removeClass('visible').addClass('hidden');
    }
  });

  $('input').on('input', function(e) {
    $(e.target).removeClass('error');
  });
  
  $('#rsvp-form').on('submit', function(e){
    var erred = false;
    $('.rsvp-row:not(.hidden)').each(function(idx, elem) {
      var firstName = $(elem).find('#first_name');
      var lastName = $(elem).find('#last_name');
e
      if ($(elem).find('.attending:checked').length == 0) {
        $(elem).find('.attending').addClass('error');
        console.log('shit not set');
        erred = true;
      }

      if (!firstName.val()) {
        firstName.addClass('error');
        erred = true;
      }

      if (!lastName.val()) {
        lastName.addClass('error');
        erred = true;
      }
    });

    if (erred) {
      console.log('erred');
      e.preventDefault();
    } else {
      return true;
    }
  });
});
