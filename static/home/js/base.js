function add_active() {
  if(!$(this).hasClass('right') && !$(this).hasClass('toc')){
    $(this)
      .addClass('active')
      .closest('.ui.menu')
      .find('.item')
      .not($(this))
      .removeClass('active');
    }
};
$(document).ready(function() {
  // fix menu when passed
  $('.masthead')
    .visibility({
      once: false,
      onBottomPassed: function() {
        $('.fixed.menu').transition('fade in');
      },
      onBottomPassedReverse: function() {
        $('.fixed.menu').transition('fade out');
      }
    });
  // create sidebar and attach to menu ope
  $('.ui.sidebar').sidebar('attach events', '.toc.item');
  $('#side_bar .item, #page_bar .item').on('click', add_active());

});
