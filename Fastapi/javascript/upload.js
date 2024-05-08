function uploadImage() {
    var id = $("#imageId").val();
    var fileInput = $("#imageFile")[0];
    var formData = new FormData();
    formData.append('id', id);
    formData.append('file', fileInput.files[0]);

    $.ajax({
        url: 'http://127.0.0.1:12345/client/upload',
        type: 'post',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            alert('Upload successful, ID: ' + response.id + ', Filename: ' + response.filename);
        },
        error: function(xhr, status, error) {
            alert('Upload failed: ' + status + ' - ' + error);
        }
    });
}



