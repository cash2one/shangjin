$(function() {
    var _wrap,_auto;
    var _scroll = 6;
    var _mycarouselLength = $(".proInfo .small li").length;
    if(_mycarouselLength>_scroll){
        _wrap = 'null';
        _auto = 0;
    }else{
        _wrap = 'null';
        _auto = 0;
    }
    $(".proInfo .small ul").jcarousel({
        wrap: _wrap,
        auto: _auto,
        scroll: _scroll,
        animation:500,
        initCallback: mycarousel_initCallback
    });

    $(".proInfo .small li:first").addClass("current");
    $(".proInfo .small li img").click(function(){
        $(".proInfo .small li").removeClass("current");
        $(this).parent().addClass("current");
        var _bigSrc = $(this).attr("bigImg");
        $(".proInfo .big img").stop(true,true).attr("src",_bigSrc).hide().fadeIn();
    });
});