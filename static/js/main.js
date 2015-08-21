// Navigation Scripts to Show Header on Scroll-Up
jQuery(document).ready(function($) {
    var MQL = 1170;

    //primary navigation slide-in effect
    if ($(window).width() > MQL) {
        var headerHeight = $('.navbar-custom').height();
        $(window).on('scroll', {
            previousTop: 0
        },
                     function() {
                         var currentTop = $(window).scrollTop();
                         //check if user is scrolling up
                         if (currentTop < this.previousTop) {
                             //if scrolling up...
                             if (currentTop > 0 && $('.navbar-custom').hasClass('is-fixed')) {
                                 $('.navbar-custom').addClass('is-visible');
                             } else {
                                 $('.navbar-custom').removeClass('is-visible is-fixed');
                             }
                         } else {
                             //if scrolling down...
                             $('.navbar-custom').removeClass('is-visible');
                             if (currentTop > headerHeight && !$('.navbar-custom').hasClass('is-fixed')) $('.navbar-custom').addClass('is-fixed');
                         }
                         this.previousTop = currentTop;
                     });
    }
    
    // Readmore
    $('article').readmore({
        speed: 85,
        maxHeight: 500,
        embedCsSS: false,
        moreLink: '<a href="#">Read More</a>',
	    lessLink: '<a href="#">Close</a>'
    });
    
});
