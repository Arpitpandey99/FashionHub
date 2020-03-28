(function ($) {
"use strict";

/*----- Mobile Menu -----*/
$('.mobile-menu nav').meanmenu({
	meanScreenWidth: "990",
	meanMenuContainer: ".mobile-menu",
});

/*----- main slider -----*/	
$('#mainSlider').nivoSlider({
	directionNav: true,
	animSpeed: 500,
	slices: 18,
	pauseTime: 7000,
	pauseOnHover: false,
	controlNav: false,
	prevText: '<i class="fa fa-angle-left nivo-prev-icon"></i>',
	nextText: '<i class="fa fa-angle-right nivo-next-icon"></i>'
});

/*----- Propular Product Slider -----*/
$(".propular-slider").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		992:{items:4,},
		768:{items:3,},
		480:{items:2,},
		0:{items:1,},
	}
});

/*----- Feature Product Slider -----*/
$(".feature-slider").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		992:{items:3,},
		768:{items:2,},
		0:{items:1,},
	}
});

/*----- Testimonial Slider -----*/
$(".testimonial-slider").owlCarousel({
	items: 1,
	autoplay: false,
	loop: true,
	nav: false,
	dots: true,
});

/*----- Propular Sidebar Slider -----*/
$(".propular-sidebar-slider").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		992:{items:1,},
		480:{items:2,},
		0:{items:1,},
	}
});

/*----- Feature Sidebar Slider -----*/
$(".feature-sidebar-slider").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		992:{items:1,},
		768:{items:2,},
		0:{items:1,},
	}
});

/*----- Blog Slider -----*/
$(".blog-slider").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		0:{items:1,},
		750:{items:2,},
		992:{items:3,},
	}
});

/*----- Blog Slider -----*/
$(".blog-slider-2").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		0:{items:1,},
		750:{items:2,},
		992:{items:2,},
	}
});

/*----- Blog Match Height -----*/
$('.single-blog').matchHeight();

/*----- Brand Slider -----*/
$(".brand-slider").owlCarousel({
	autoplay: false,
	loop: true,
	nav: true,
	margin: 30,
	navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	dots: false,
	responsive:{
		0:{items:2,},
		750:{items:4,},
		950:{items:5,},
		1170:{items:6,},
	}
});
/*----- Scroll Up -----*/
$.scrollUp({
	scrollText: '<i class="fa fa-chevron-up"></i>',
	easingType: 'linear',
	scrollSpeed: 900,
	animation: 'fade'
});

/*----- Category Sidebar Treeview -----*/
$("#cat-treeview ul").treeview({
	animated: "normal",
	persist: "location",
	collapsed: true,
	unique: true,
});

/*----- Check Out Accordion -----*/
$(".panel-heading a").on("click", function(){
	$(".panel-heading a").removeClass("active");
	$(this).addClass("active");
});

/*----- Cart Plus Minus Button -----*/	
$(".pro-quantity").prepend('<span class="dec qtybutton">-</span>');
$(".pro-quantity").append('<span class="inc qtybutton">+</span>');
$(".qtybutton").on("click", function() {
	var $button = $(this);
	var oldValue = $button.parent().find("input").val();
	if ($button.text() == "+") {
	  var newVal = parseFloat(oldValue) + 1;
	} else {
	   // Don't allow decrementing below zero
	  if (oldValue > 0) {
		var newVal = parseFloat(oldValue) - 1;
		} else {
		newVal = 0;
	  }
	  }
	$button.parent().find("input").val(newVal);
});	

/*----- Simple Lens -----*/	
$('.simpleLens-lens-image').simpleLens({
	loading_image: 'img/loading.gif'
});

/*----- Price Slider -----*/	
$( "#slider-range" ).slider({
   range: true,
   min: 0,
   max: 800,
   values: [ 50, 550 ],
   slide: function( event, ui ) {
	$( "#price-amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
   }
  });
$( "#price-amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
   " - $" + $( "#slider-range" ).slider( "values", 1 ) );  

	
})(jQuery);	