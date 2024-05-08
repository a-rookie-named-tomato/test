function deleteCar() {
    var id = $("#id").val();
    $.ajax({
        url: 'http://127.0.0.1:12345/client/delete',
        type: 'delete',
        contentType: 'application/json',
        data: JSON.stringify({
            "id": id,
        }),
        success: function (data) {
            alert('Car deleted: ' + data.message);
        },
        error: function () {
            alert('An error occurred while deleting the car');
        }
    });
}
