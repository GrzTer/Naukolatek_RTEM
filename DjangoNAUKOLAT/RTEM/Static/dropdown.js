$(document).ready(function () {
    $('.nav-link').on('click', function () {
        $('.nav-link').removeClass('active-nav-link');
        $(this).addClass('active-nav-link');
    });
});