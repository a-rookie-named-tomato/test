$(document).ready(function(){
    function register() {
      var username = $("#username").val();
      var password = $("#password").val();
      var confirmPassword = $("#confirmPassword").val();
  
      if(username === "" || password === "" || confirmPassword === "") {
        alert("请输入所有必填字段。");
        return;
      }
  
      if(password !== confirmPassword) {
        alert("两次输入的密码不一致。");
        return;
      }
  
      $.ajax({
        url: 'http://127.0.0.1:12345/client/register',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({
          "username": username,
          "password": password
        }),
        success: function (data) {
          console.log("Success Response:", data);
          if (data.code === 200) {
            alert('用户 ' + data.username + ' 注册成功');
            window.location.href = 'login.html';
          } else {
            alert('注册失败: ' + data.message);
          }
        },
        error: function () {
          console.error("Error occurred");
          alert('An error occurred');
        }
      });
    }
  
    $("#registerBtn").on("click", register);
  });
  