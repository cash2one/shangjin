// JavaScript Document
$(document).ready(function(){
	banner();
});

function banner(){
	var len = $("#pic ul li").length;
	var s = len - 1;
	$("#pic ul li").eq(0).show();
	$("#ben_Text ul li").eq(0).show();
	(function(){
		var curr = 0;
		$("#ben ul li").each(function(i){
			$(this).click(function(){
				curr = i;
				$("#pic ul li").eq(i).fadeIn(1000).siblings("li").fadeOut(1000);
				$("#ben_Text ul li").eq(i).fadeIn(1000).siblings("li").fadeOut(1000);
				$(this).siblings("li").removeClass("bCur").end().addClass("bCur");
				return false;
			});
		});
		
		var pg = function(flag){
			if (flag) {
				if (curr == 0) {
					todo = s;
				} else {
					todo = (curr - 1) % len;
				}
			} else {
				todo = (curr + 1) % len;
			}
			$("#ben ul li").eq(todo).click();
		};

		$("#ben_perv").click(function(){
			pg(true);
			return false;
		});

		$("#ben_next").click(function(){
			pg(false);
			return false;
		});

		var timer = setInterval(function(){
			todo = (curr + 1) % len;
			$("#ben ul li").eq(todo).click();
		},5000);
		
		$("#pic,#ben_Text,#ben_perv,#ben_next,#ben ul li").hover(function(){
				clearInterval(timer);
			},
			function(){
				timer = setInterval(function(){
					todo = (curr + 1) % len;
					$("#ben ul li").eq(todo).click();
				},5000);			
			}
		);
	})();
};

$(function() {
	$('#jcarousel').jcarousel({
		wrap: 'circular', //circular 循环
		auto: 2,
		scroll: 2,
		animation: 800
	});
});


