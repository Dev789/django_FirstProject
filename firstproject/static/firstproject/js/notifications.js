$(document).ready(function () {
    fetch_notifications();
    $(".notifications").click(function () {
        $.ajax({
            url: notify_read,
            type: "GET",
            success: function (result) {

            }
        });
    });
    setInterval(fetch_notifications, 30000);
});

function fetch_notifications() {
    $.ajax({
        url: header_notification,
        type: "GET",
        success: function (result) {
            $("#notify_container").html(result);
        }
    });
}
