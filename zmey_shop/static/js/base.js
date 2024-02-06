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

function showImage() {
    document.getElementById("myImage").style.display = "block";  
}