function AddCar() {
    var id = $("#id").val();
    var model = $("#model").val();
    var make = $("#make").val();
    var color = $("#color").val();
    var year = $("#year").val();
    var price = parseFloat($("#price").val());
    var owner_name = $("#owner_name").val();
    var phone = $("#phone").val();
    var s_id = $("#s_id").val();
    var sale_time = $("#sale_time").val();
    var sale_price = $("#sale_price").val();
    $.ajax({
        url: 'http://127.0.0.1:12345/client/add',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({
            "id": id,
            "model": model,
            "make": make,
            "color": color,
            "year": year,
            "price": price,
            "owner_name": owner_name,
            "phone": phone,
            "s_id": s_id,
            "sale_time":sale_time,
            "sale_price":sale_price
        }),
        success: function (data) {
            alert('Car created: ' + data.id);
        },
        error: function () {
            alert('An error occurred while creating the car');
        }
    });
}
