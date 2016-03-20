jQuery(document).ready(function () {

    /*
     Fullscreen background
     */
    function randInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    var backgrounds = ["1", "2", "3", "4", "5"];
    var currentIndex = randInt(0, backgrounds.length - 1);


    $.backstretch("/static/img/login/backgrounds/" + backgrounds[currentIndex] + ".jpg");
    setInterval(function () {
        currentIndex = (currentIndex + 1) % backgrounds.length;
        $.backstretch("/static/img/login/backgrounds/" + backgrounds[currentIndex] + ".jpg", {speed: 2500});
        
    }, 5000);


    /*
     Login form validation
     */
    $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function () {
        $(this).removeClass('input-error');
    });

    $('.login-form').on('submit', function (e) {

        $(this).find('input[type="text"], input[type="password"], textarea').each(function () {
            if ($(this).val() == "") {
                e.preventDefault();
                $(this).addClass('input-error');
            }
            else {
                $(this).removeClass('input-error');
            }
        });

    });

    /*
     Registration form validation
     */
    $('.registration-form input[type="text"], .registration-form textarea').on('focus', function () {
        $(this).removeClass('input-error');
    });

    $('.registration-form').on('submit', function (e) {

        $(this).find('input[type="text"], textarea').each(function () {
            if ($(this).val() == "") {
                e.preventDefault();
                $(this).addClass('input-error');
            }
            else {
                $(this).removeClass('input-error');
            }
        });

    });


});
