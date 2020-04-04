$(function () {
    setTimeout(function () {
        $('.load').addClass('hide-it');
        $("html, body").removeAttr("style");
        $('#page, #bdy').removeClass('blank');       
    }, 2500);
    
})
// ]]>
$(document).ready(function () {
    $('#logo img').click(function () {
        var url = $(this).attr('src');
        $('.pop img').attr('src', url)
        $('.pop').show();
    });
    $(document).on('click', 'a', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top - $('#fixtop').height() || $(hash).offset().top
            }, 700, function () {
                window.location.hash = hash;
            });
        }
    });
    $(document).on('click', '#fixtop .top-logo', function (event) {
        $('html, body').animate({
            scrollTop: 0
        }, 700, function () {
        });
    });
    $('.pop a.clox').click(function () {
        $('.pop').hide();
    });
    $('ul.port-lists li').click(function (eve) {
        eve.stopPropagation();
        $(this).addClass('active').siblings().removeClass('active');
        $(this).children('ul').slideDown();
        $(this).siblings().children('ul').hide(250);
        var getid = $(this).attr('ref-id');
        $('#' + getid).show().css('width', '100%').siblings().hide();

    });

    $('.slider ul li').click(function () {
        var buchiki = '#' + $(this).attr('class-for');
        $(buchiki).show().siblings().hide('slide', {
            direction: 'top'
        });
    });

    $('.desc img').click(function () {
        $('.desc span').show();
        setTimeout(function () {
            $('.desc span').hide();
        }, 2000);
    });



    $('.forms input, .forms textarea, .forms select').each(function () {
        tmpval = $(this).val();
        if (tmpval != '') {
            $(this).next().addClass('trans');
        }
    });
    $('.forms input, .forms textarea, .forms select').focus(function () {
        $(this).next().addClass('trans');

    }).blur(function () {
        if ($(this).val() == '') {
            $(this).next().removeClass('trans');
        }
    });


    $('header #myNavbar .nav-menu li a').click(function () {
        $('#myNavbar.in').removeClass('in');
        $('header .navbar-header button.navbar-toggle').attr('aria-expanded', 'false').addClass('collapsed');
    });

    $('header #myNavbar > .navbar-toggle').click(function () {
        $(this).toggleClass('menu-open').siblings().toggleClass('slide');
    });
    $('#logo-div .row > div').click(function () {
        $('#logo-div').addClass('fix-it');
        $('.logo-list li').show();
        $('.cc-slider').slick({
            dots: true,
            infinite: true,
            speed: 300,
            slidesToShow: 1,
            adaptiveHeight: true
        });
        var click_count = $(this).index();
        console.log(click_count);
        $(".cc-slider .slick-dots li:nth-child("+click_count+")").click();
        $('.unslcik').show();
    });
    $('.unslcik').click(function () {
        if ($('.cc-slider').hasClass('slick-slider')) {
            $('.cc-slider').slick('unslick');
            $('.unslcik').hide();
            $('#logo-div').removeClass('fix-it');
        } else {
            $('.logo-list li').removeAttr('style').show();
        }
    });
    $('button[type="submit"]').click(function () {
        if ($('#myform input').val() == '' || $('#myform textarea').val() == '') {
            $(this).addClass('err-red');
        }
        setTimeout(function () {
            $('button[type="submit"]').removeClass('err-red');
        }, 2000);
    });
    $('.subscribe input, .subscribe textarea, .subscribe select').each(function () {
        tmpval = $(this).val();
        if (tmpval != '') {
            $(this).prev().addClass('trans');
        }
    });
    $('.subscribe input, .subscribe textarea, .subscribe select').focus(function () {
        $(this).prev().addClass('trans');

    }).blur(function () {
        if ($(this).val() == '') {
            $(this).prev().removeClass('trans');
        }
    });
    $(document).on('click', '#header ul.nav-menu li a', function(){
        $(this).addClass('add-color').parent().siblings().find('a').removeClass('add-color');
    });
    var color_array = ['#ff0000','#ffbc00','#10ff00','#6e00ff','#c328a2']
    $(document).on('mouseover', '#header ul.nav-menu li', function(){
        var svgid = $(this).attr('class') + '-icon';
        /*$('.menu-icon').css('background',color_array[$(this).index()-1]);*/
        $('.menu-icon svg#'+svgid).addClass('active').siblings().removeClass('active');
    });
    if ($(window).width() < 767) {
        $('#header ul.nav-menu li').each(function(){
            var append_id = '#'+$(this).attr('class')+'-icon'
            $(this).find('a').append($(append_id));
        });
    };

    $('ul.icon').hide();
    $('.exp-list-item').click(function(){
        $(this).find('.plus').toggleClass('opened');
        $(this).find('ul.icon').toggle(100);
    });
    $('.skill-list li').each(function(){
        var m_width = $(this).attr('title');
        $(this).find('b').css('width',m_width);
    });
    $('.skill-list li b').each(function(i){
        var rand = ['#fb4c4c','#ff8c25','#ffcc00','#52ab09', '#25aaff', '#bf25ff','#fb4c4c','#ff8c25','#ffcc00'];
        $(this).css('backgroundColor',rand[i]);
    });
    

});
