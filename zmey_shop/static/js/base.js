function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}


function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}


$(function ($) {
    $('.manage_favourite').submit(function (e) {
        if (e.target.querySelector('.heart')) {
            $(this).toggleClass('active_heart');
        }
        else {
            $(this).toggleClass('active_favourite_heart');
        }
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            success: function (response) {
                console.log("Данные успешно отправлены!");
            },
            error: function (error) {
                console.error("Ошибка при отправке данных: ", error);
            },
        });
    });

});