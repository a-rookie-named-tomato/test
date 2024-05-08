// function selectCar() {
//     var id = $("#id").val();
//     $.ajax({
//         url: 'http://127.0.0.1:12345/client/select',
//         type: 'post',
//         data: { id: id },
//         success: function (data) {
//             if (data.message) {
//                 alert(data.message);
//             } else {
//                 displayCarInfo(data);
//             }
//         },
//         error: function () {
//             alert('An error occurred while selecting the car');
//         }
//     });
// }

// function displayCarInfo(carList) {
//     var infoHtml = '<h2>Car Information</h2>';
//     for (var i = 0; i < carList.length; i++) {
//         var carInfo = carList[i];
//         infoHtml += '<p>ID: ' + carInfo.id + '</p>';
//         infoHtml += '<p>Model: ' + carInfo.model + '</p>';
//         infoHtml += '<p>Make: ' + carInfo.make + '</p>';
//         infoHtml += '<p>Color: ' + carInfo.color + '</p>';
//         infoHtml += '<p>Year: ' + carInfo.year + '</p>';
//         infoHtml += '<p>Price: $' + carInfo.price + '&#x4E07;' +'</p>';
//         infoHtml += '<p>Owner Name: ' + carInfo.owner_name + '</p>';
//         infoHtml += '<p>Phone: ' + carInfo.phone + '</p>';
//         infoHtml += '<p>Shop ID: ' + carInfo.shop_id + '</p>';
//         infoHtml += '<p>Sale Time: ' + carInfo.sale_time + '</p>';
//         infoHtml += '<p>Sale Price: $' + carInfo.sale_price + '&#x4E07;'+ '</p>';
//         infoHtml += '<p>Sold: ' + carInfo.sold + '</p>';
//         infoHtml += '<hr>';
//     }
//     $("#carInfoContainer").html(infoHtml);
// }




function selectCar() {
    var id = $("#id").val();
    $.ajax({
        url: 'http://127.0.0.1:12345/client/select',
        type: 'post',
        data: { id: id },
        success: function (data) {
            if (data.message) {
                alert(data.message);
            } else {
                displayCarInfo(data);
            }
        },
        error: function () {
            alert('An error occurred while selecting the car');
        }
    });
}

function displayCarInfo(carList) {
    var infoHtml = '<h2>Car Information</h2>';
    for (var i = 0; i < carList.length; i++) {
        var carInfo = carList[i];
        infoHtml += '<p>ID: ' + carInfo.id + '</p>';
        infoHtml += '<p>Model: ' + carInfo.model + '</p>';
        infoHtml += '<p>Make: ' + carInfo.make + '</p>';
        infoHtml += '<p>Color: ' + carInfo.color + '</p>';
        infoHtml += '<p>Year: ' + carInfo.year + '</p>';
        infoHtml += '<p>Price: $' + carInfo.price + '&#x4E07;' + '</p>';
        infoHtml += '<p>Owner Name: ' + carInfo.owner_name + '</p>';
        infoHtml += '<p>Phone: ' + carInfo.phone + '</p>';
        infoHtml += '<p>Shop ID: ' + carInfo.shop_id + '</p>';
        infoHtml += '<p>Sale Time: ' + carInfo.sale_time + '</p>';
        infoHtml += '<p>Sale Price: $' + carInfo.sale_price + '&#x4E07;' + '</p>';
        infoHtml += '<p>Sold: ' + carInfo.sold + '</p>';

        // Check if image data is available
        if (carInfo.image_data) {
            // Display the image using base64 encoding
            infoHtml += '<img src="data:image/png;base64,' + carInfo.image_data + '" alt="Car Image" style="max-width: 300px; max-height: 200px;">';
        }

        infoHtml += '<hr>';
    }
    $("#carInfoContainer").html(infoHtml);
}
