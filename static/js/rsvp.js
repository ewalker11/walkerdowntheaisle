Zepto(function($){
  $('#num_guests').on('change', function(e){
    console.log(e.target.value);
    while ($('.rsvp_row:not(.hidden-rsvp-row)').length < e.target.value) {
      $('.hidden-rsvp-row').first().removeClass('hidden-rsvp-row')
    }
    while ($('.rsvp_row:not(.hidden-rsvp-row)').length > e.target.value) {
      $('.rsvp_row:not(.hidden-rsvp-row)').last().addClass('hidden-rsvp-row')
    }
  });
});
