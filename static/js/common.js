// JavaScript Document

$(function() {
	$(".nav_li").not(":first-child,:eq(1),:eq(2),:eq(5)").hover(
		  function() {
			  $(this).addClass("nav_li_hover");
			  $(this).parent().parent().next(".subnavbg").show();
		  },
		  function() {
			  $(this).removeClass("nav_li_hover");
			  $(this).parent().parent().next(".subnavbg").hide();
		  })
});
