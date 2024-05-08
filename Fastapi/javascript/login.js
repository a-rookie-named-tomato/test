$(document).ready(function () {
    function login() {
        var username = $("#username").val();
        var password = $("#password").val();

        $.ajax({
            url: 'http://127.0.0.1:12345/client/login',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                "username": username,
                "password": password
            }),
            success: function (data) {
                console.log("Success Response:", data);
                if (data.code === 200) {
                    alert('Username: ' + data.username + '登录成功');
                    window.location.href = 'dispose.html';
                } else {
                    alert('登录失败: ' + data.message);
                }
            },
            error: function () {
                console.log("Error occurred");
                alert('An error occurred');
            }
        });
    }

    $("#submitBtn").on("click", login);
});
