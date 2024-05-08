function changeCar() {
    var id = $("#id").val();
    var owner_name = $("#owner_name").val();
    var phone = $("#phone").val();
    var sale_time = $("#sale_time").val();
    var sale_price = $("#sale_price").val();
    
    if (!id || !owner_name || !phone || !sale_time || !sale_price) {
        alert('Please fill in all fields');
        return;
    }
    
    $.ajax({
        url: 'http://127.0.0.1:12345/client/edit',
        type: 'put',
        contentType: 'application/json',
        data: JSON.stringify({
            "id": id,
            "owner_name": owner_name,
            "phone": phone,
            "sale_time": sale_time,
            "sale_price": sale_price
        }),
        success: function (data) {
            alert('Car changed: ' + data.id);
        },
        error: function () {
            alert('An error occurred while changing the car');
        }
    });
}
