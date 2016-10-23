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

  $('.attending').on('change', function(e){
    if (this.value == 'yes') {
      $('#dinner_option').addClass('form-enabled').removeClass('form-disabled').prop('disabled', false);
    } else {
      $('#dinner_option').addClass('form-disabled').removeClass('form-enabled').prop('disabled', true);
    }
  });

  $('input').on('input', function(e) {
    $(e.target).removeClass('error');
  });

  $('select').on('change', function(e) {
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

      var attending = $(elem).find('.attending:checked');
      var dinnerOption = $(elem).find('#dinner_option');
      if (attending.length > 0 && attending[0].value == 'yes' && dinnerOption.val() == 'Select') {
        console.log(dinnerOption);
        dinnerOption.addClass('error');
        erred = true;
      }
    });

    if (erred) {
      e.preventDefault();
    } else {
      return true;
    }
  });
});
