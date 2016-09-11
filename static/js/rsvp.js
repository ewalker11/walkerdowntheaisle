Zepto(function($){
  $('#num_guests').on('change', function(e){
    while ($('.rsvp_row:not(.hidden-rsvp-row)').length < e.target.value) {
      $('.hidden-rsvp-row').first().removeClass('hidden-rsvp-row')
    }
    while ($('.rsvp_row:not(.hidden-rsvp-row)').length > e.target.value) {
      $('.rsvp_row:not(.hidden-rsvp-row)').last().addClass('hidden-rsvp-row')
    }
  });

  $('input').on('input', function(e) {
    $(e.target).removeClass('error');
  });
  
  $('#rsvp-form').on('submit', function(e){
    var erred = false;
    $('.rsvp_row:not(.hidden-rsvp-row)').each(function(idx, elem) {
      var firstName = $(elem).find('#first_name');
      var lastName = $(elem).find('#last_name');

      if ($(elem).find('.attending:checked').empty()) {
        $(elem).find('.attending').addClass('error');
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
      e.preventDefault();
    }
  });
});
